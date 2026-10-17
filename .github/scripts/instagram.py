"""드리움 인스타그램 게시 스크립트 (메타 공식 Graph API)

사용법 (GitHub Actions 에서 실행)
  python instagram.py check                      토큰 확인 + 연결된 인스타 계정 표시
  python instagram.py post _insta/02-xxx.json    게시물 1건 올리기

게시물 파일(_insta/*.json) 형식
  {
    "caption": "본문 + 해시태그",
    "images": ["https://gyeolnbit.co.kr/images/insta/02-xxx/1.jpg", ...]   # 1~10장, JPG
  }

토큰은 GitHub Secrets 의 IG_ACCESS_TOKEN 에서만 읽습니다.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://graph.facebook.com/v23.0"
TOKEN = os.environ.get("IG_ACCESS_TOKEN", "")
IG_USERNAME = os.environ.get("IG_USERNAME", "").lstrip("@").lower()


def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(f"{API}/{path}?{data.decode()}")
    else:
        req = urllib.request.Request(f"{API}/{path}", data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace").replace(TOKEN, "***")
        sys.exit(f"API 오류 {e.code} ({path}): {body}")


def ig_accounts():
    pages = call("GET", "me/accounts",
                 fields="name,instagram_business_account{id,username}")["data"]
    return [p["instagram_business_account"] for p in pages
            if p.get("instagram_business_account")]


def pick_account():
    accounts = ig_accounts()
    if IG_USERNAME:
        accounts = [a for a in accounts if a["username"].lower() == IG_USERNAME]
    if len(accounts) != 1:
        names = ", ".join("@" + a["username"] for a in ig_accounts()) or "없음"
        sys.exit(f"게시할 인스타 계정을 하나로 정할 수 없습니다. 연결된 계정: {names}")
    return accounts[0]


def wait_ready(container_id):
    for _ in range(30):
        status = call("GET", container_id, fields="status_code")["status_code"]
        if status == "FINISHED":
            return
        if status in ("ERROR", "EXPIRED"):
            sys.exit(f"사진 처리 실패 ({status}): {container_id}")
        time.sleep(5)
    sys.exit("사진 처리 시간이 너무 오래 걸립니다.")


def check():
    for a in ig_accounts():
        print(f"연결된 인스타 계정: @{a['username']}")
    print(f"게시 대상: @{pick_account()['username']}")


def post(path):
    with open(path, encoding="utf-8") as f:
        item = json.load(f)
    images, caption = item["images"], item["caption"]
    if not 1 <= len(images) <= 10:
        sys.exit("사진은 1~10장이어야 합니다.")
    for url in images:
        with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=30) as r:
            if r.status != 200:
                sys.exit(f"사진이 아직 홈페이지에 없습니다: {url}")

    account = pick_account()
    uid = account["id"]
    if len(images) == 1:
        container = call("POST", f"{uid}/media", image_url=images[0], caption=caption)["id"]
    else:
        children = []
        for url in images:
            cid = call("POST", f"{uid}/media", image_url=url, is_carousel_item="true")["id"]
            wait_ready(cid)
            children.append(cid)
        container = call("POST", f"{uid}/media", media_type="CAROUSEL",
                         children=",".join(children), caption=caption)["id"]
    wait_ready(container)
    media_id = call("POST", f"{uid}/media_publish", creation_id=container)["id"]
    link = call("GET", media_id, fields="permalink").get("permalink", "")
    print(f"@{account['username']} 게시 완료: {link}")


if __name__ == "__main__":
    if not TOKEN:
        sys.exit("IG_ACCESS_TOKEN 이 등록되지 않았습니다 (GitHub Secrets).")
    if sys.argv[1:2] == ["check"]:
        check()
    elif sys.argv[1:2] == ["post"] and len(sys.argv) == 3:
        post(sys.argv[2])
    else:
        sys.exit(__doc__)
