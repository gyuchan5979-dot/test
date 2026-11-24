"""드리움 스레드 게시 (Threads API).

  python3 threads.py check          토큰과 연결된 스레드 계정 확인 (게시 안 함)
  python3 threads.py next           _insta/threads/posts 에서 아직 안 올린 첫 글 게시 (매일 자동 실행용)
  python3 threads.py post FILE      FILE(json: {"text": "...", "images": ["https://..."]}) 게시
                                    images 0장 = 글만, 1장 = 사진 1장, 2장 이상 = 여러 장 묶음

토큰: THREADS_ACCESS_TOKEN (GitHub Secrets). 값은 로그에 출력하지 않음.
"""
import json, os, sys, time, urllib.parse, urllib.request, urllib.error

API = "https://graph.threads.com/v1.0"
TOKEN = os.environ.get("THREADS_ACCESS_TOKEN", "").strip()


def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{API}/{path}"
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace").replace(TOKEN, "***") if TOKEN else ""
        sys.exit(f"API 오류 {e.code} ({path}): {body}")


UID = "me"


def container(**p):
    return call("POST", f"{UID}/threads", **p)["id"]


def wait_ready(cid):
    for _ in range(20):
        st = call("GET", cid, fields="status,error_message")
        if st.get("status") in ("FINISHED", "PUBLISHED"):
            return
        if st.get("status") in ("ERROR", "EXPIRED"):
            sys.exit(f"사진 처리 실패: {st}")
        time.sleep(6)
    sys.exit("사진 처리가 너무 오래 걸려요")


def refresh():
    """60일 토큰 연장 (발급 24시간 이후부터 가능). 실패해도 게시는 계속."""
    url = "https://graph.threads.com/refresh_access_token?" + urllib.parse.urlencode(
        {"grant_type": "th_refresh_token", "access_token": TOKEN})
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            d = json.load(r)
        days = int(d.get("expires_in", 0)) // 86400
        same = d.get("access_token") == TOKEN
        print(f"토큰 연장: 앞으로 약 {days}일 유효" + ("" if same else " (새 토큰이 발급됨 — 기존 토큰도 만료 전까지 사용 가능)"))
    except Exception as e:
        print(f"토큰 연장은 건너뜀 ({type(e).__name__})")


def main():
    if not TOKEN:
        sys.exit("THREADS_ACCESS_TOKEN 이 등록되지 않았어요 (Settings → Secrets → Actions)")
    global UID
    me = call("GET", "me", fields="id,username")
    UID = me["id"]
    print(f"연결된 스레드 계정: @{me.get('username')}")
    refresh()
    if sys.argv[1] == "check":
        return
    path = sys.argv[2] if sys.argv[1] == "post" else None
    if sys.argv[1] == "next":
        import glob
        for f in sorted(glob.glob("_insta/threads/posts/*.json")):
            if not json.load(open(f, encoding="utf-8")).get("posted"):
                path = f
                break
        if not path:
            print("올릴 글이 없어요 (대기열이 비었어요)")
            return
    print(f"게시할 글: {path}")
    post = json.load(open(path, encoding="utf-8"))
    if post.get("posted"):
        sys.exit("이미 게시된 글이에요 (posted: true)")
    text, imgs = post.get("text", ""), post.get("images", [])
    if len(text) > 500:
        sys.exit(f"글이 500자를 넘어요 ({len(text)}자)")
    if not imgs:
        cid = container(media_type="TEXT", text=text)
    elif len(imgs) == 1:
        cid = container(media_type="IMAGE", image_url=imgs[0], text=text)
    else:
        kids = [container(media_type="IMAGE", image_url=u, is_carousel_item="true") for u in imgs[:20]]
        for k in kids:
            wait_ready(k)
        cid = container(media_type="CAROUSEL", children=",".join(kids), text=text)
    time.sleep(30)  # Meta 안내: 게시 전 약 30초 대기
    wait_ready(cid)
    res = call("POST", f"{UID}/threads_publish", creation_id=cid)
    print(f"게시 완료: media id {res.get('id')}")
    post["posted"] = True
    post["posted_at"] = time.strftime("%Y-%m-%d %H:%M", time.gmtime(time.time() + 9 * 3600))
    post["media_id"] = res.get("id")
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(post, fp, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
