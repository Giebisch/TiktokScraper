import requests

from .models import Comment

def get_comments_from_video(user_agent, proxies, video_link, limit_comments):
    if "vm.tiktok.com" in video_link or "vt.tiktok.com" in video_link:
        video_link = requests.head(video_link, stream=True, allow_redirects=True, timeout=5, proxies=proxies).url.split("/")[5].split("?", 1)[0]
    else:
        video_link = video_link.split("/")[5].split("?", 1)[0]

    cursor = 0
    comments = []

    while limit_comments > cursor:
        try:
            headers = {
                'user-agent': user_agent,
                'referer': f'https://www.tiktok.com/@x/video/{video_link}',
            }

            response = requests.get(f"https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id={video_link}&count=9999999&cursor={cursor}", headers=headers, proxies=proxies).json()

            for comment in response["comments"]:
                comments.append(Comment(**comment))

            cursor += 50
        except:
            break
    return comments

def get_profile_details(user_agent, proxies, profile):
    res = []

    if profile.startswith("@"):
        profile = profile[1:]
    elif profile.endswith("/"):
        profile = profile.split("/")[-2][1:]
    else:
        profile = profile.split("/")[-1][1:]

    headers = {
        'user-agent': user_agent,
        'referer': f'https://www.tiktok.com/@{profile}'
    }

    url = f"https://www.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_pc&uniqueId={profile}"
    response = requests.get(url, headers=headers, proxies=proxies)

    try:
        if response.status_code == 200:
            res = response.json()
    except Exception as e:
        return url

    return url
