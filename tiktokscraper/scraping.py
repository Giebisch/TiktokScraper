import requests

from .models import Comment

def get_comments_from_video(video_link, limit_comments):
    if "vm.tiktok.com" in video_link or "vt.tiktok.com" in video_link:
        video_link = requests.head(video_link, stream=True, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
    else:
        video_link = video_link.split("/")[5].split("?", 1)[0]

    cursor = 0
    comments = []

    while limit_comments > cursor:
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'referer': f'https://www.tiktok.com/@x/video/{video_link}',
            }

            response = requests.get(f"https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id={video_link}&count=9999999&cursor={cursor}", headers=headers).json()

            for comment in response["comments"]:
                comments.append(Comment(**comment))

            cursor += 50
        except:
            break
    return comments
