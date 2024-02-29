from tiktokscraper.TiktokScraper import TiktokScraper

# create TiktokScraper object
TS = TiktokScraper()

# ========================================================
# using the following functions is possible without login
# ========================================================

# get comments from single video
comments = TS.get_comments("https://www.tiktok.com/@google/video/7291741762278739242", limit_comments=50)

# get comments from several different videos
result = TS.get_comments(["https://www.tiktok.com/@google/video/7291741762278739242", "https://www.tiktok.com/@google/video/7286921045720730926"], limit_comments=50)

# print comment texts
for video in result:
    for comment in video:
        print(comment.text)

# get video details
video_details = TS.get_video_details(["https://www.tiktok.com/@google/video/7291741762278739242", "https://www.tiktok.com/@google/video/7286921045720730926"])

# print video details
for video in video_details:
    print(video.description, video.play_count)

# get followers for user
# can only use secUid for user. Use get_profile_details first to get this information
# Here is an example for Google
secUid = "MS4wLjABAAAABqImMisT8O3jtr2Ufg4t7wTYypL4gPC9rWRrIkkThwCgCVMRJW6ls-n2T6bmDMZb"
followers = TS.get_followers_for_user(secUid, limit=30)
for follower in followers:
    print(follower.follower_count)

# ====================================================================================
# for the following functions you need to either be logged in or manually get msTokens
# ====================================================================================
    
# used to log in
# if use_browser_cookies is set to True, cookies from your browser are used and you dont have
# to do anything additionally
TS._initialize_browser(use_browser_cookies=True)

# Profile details
profiles = TS.get_profile_details(["google", "microsoft"])
for profile in profiles:
    print(profile.follower_count)

# videos of user
videos = TS.get_videos_of_user("google")
for video in videos:
    print(video.id, video.description)
    # example to download video
    # video.download(f"{video.id}.mp4")

# get recommended / trending videos
videos = TS.get_trending_videos(limit_videos=5)

# get videos for keyword
videos = TS.get_videos_for_keyword("google", limit=24)
