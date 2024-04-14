import requests
import logging
import urllib
import json

from .models import Comment, Profile, Video

from tiktokscraper.xbogus.xbogus import calculate_xbogus
from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)
SESSION = None

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

async def get_profile_detail(context, profile):
    """
    Return profile details for given unique ID
    """
    if profile.startswith("@"):
        profile = profile[1:]
    elif profile.endswith("/"):
        profile = profile.split("/")[-2][1:]
    elif "/" in profile:
        profile = profile.split("/")[-1][1:]

    page = await context.new_page()
    api_request_context = context.request

    url = f"https://www.tiktok.com/api/user/detail/?WebIdLastTime=1707251748&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7332590289297786400&device_platform=web_pc&focus_state=true&from_page=user&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=DE&screen_height=1080&screen_width=1920&tz_name=Europe%2FBerlin&uniqueId={profile}&webcast_language=en&msToken="
    
    xbogus = await calculate_xbogus(page, url, None)
    final_url = url + "&X-Bogus=" + xbogus

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    response = await api_request_context.get(final_url, headers=headers)

    try:
        data = await response.json()
    except Exception as e:
        logger.debug(e)
        logger.debug(final_url)
        logger.debug(response.text())
        return None, []

    return context, Profile(**data)

async def get_videos_for_user(context, secUid):
    """
    Returns videos for user using their secUid. If secUid is not available, use get_profile_detail() first
    """
    page = await context.new_page()
    # api_request_context = context.request

    url = f"https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1701172473&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&device_id=7306480092313388577&device_platform=web_pc&focus_state=true&from_page=user&history_len=1&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=DE&referer=&region=DE&screen_height=1080&screen_width=1920&secUid={secUid}&tz_name=Europe%2FBerlin&verifyFp=verify_lpcd5t5g_uud5fNlz_2Qyz_4mwf_B8vu_No3ej4Amte7Z&webcast_language=en&msToken="

    xbogus = await calculate_xbogus(page, url, None)
    final_url = url + "&X-Bogus=" + xbogus

    response = await page.goto(final_url)

    try:
        data = await response.json()
    except Exception as e:
        logger.debug(e)
        logger.debug(response.text())

    videos = []

    for video in data["itemList"]:
        videos.append(Video(**video))

    return context, videos

async def get_trending_videos(context):
    url = "https://www.tiktok.com/api/explore/item_list/?WebIdLastTime=1707869418&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36&categoryType=119&channel=tiktok_web&cookie_enabled=true&count=16&device_platform=web_pc&focus_state=true&from_page=&history_len=2&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=DE&screen_height=1080&screen_width=1920&tz_name=Europe%2FBerlin&webcast_language=en"

    page = await context.new_page()
    response = await page.goto(url)
    j = await response.json()

    logger.debug(j)
    videos = []
    for video in j['itemList']:
        videos.append(Video(**video))

    return videos

def get_followers_for_user(secUid, limit=0):
    minimum_count = 0
    maximum_count = 0
    
    user_set = set()
    users = []

    while True:
        url = f"https://www.tiktok.com/api/user/list/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F122.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=30&device_id=7306480092313388577&device_platform=web_pc&focus_state=true&from_page=user&history_len=3&is_fullscreen=false&is_page_visible=true&maxCursor={maximum_count}&minCursor={minimum_count}&os=mac&priority_region=DE&referer=&region=DE&scene=67&screen_height=1080&screen_width=1920&secUid={secUid}&tz_name=Europe%2FBerlin&webcast_language=en&msToken="
        
        res = requests.get(url)
        data = res.json()
        count = len(user_set)

        if "userList" not in data:
            break
        for user in data["userList"]:
            if user["user"]["id"] not in user_set:
                user_set.add(user["user"]["id"])
                users.append(user)
        if len(user_set) == count or len(user_set) >= limit:
            break

        minimum_count = data["minCursor"]
        maximum_count = data["maxCursor"]

    return [Profile(**{"userInfo": user}) for user in users[:limit]]

async def get_video_for_keyword(context, keyword, limit=10):
    offset = 0
    videos = []

    search_id = ""
    while len(videos) < limit:
        url = f"https://www.tiktok.com/api/search/general/full/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F122.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7306480092313388577&device_platform=web_pc&device_type=web_h264&focus_state=true&from_page=search&history_len=2&is_fullscreen=false&is_page_visible=true&keyword={keyword}&offset={offset}&os=mac&priority_region=DE&referer=&region=DE&screen_height=1080&screen_width=1920{search_id}&search_source=normal_search&tz_name=Europe%2FBerlin&verifyFp=verify_lpcd5t5g_uud5fNlz_2Qyz_4mwf_B8vu_No3ej4Amte7Z&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=en&msToken="

        page = await context.new_page()
        response = await page.goto(url)
        response = await response.json()

        logger.debug(url)
        for video in response['data']:
            if video["type"] != 1:
                continue
            videos.append(Video(**video["item"]))
        offset = response["cursor"]
        search_id = "&search_id=" + response["extra"]["logid"]
        logger.debug(len(videos))
        if response["has_more"] == 0:
            break

    return videos