import unittest
from argparse import Namespace
from tiktokscraper.TiktokScraper import TiktokScraper
import logging
import asyncio
import pytest

# pytest_plugins = ('pytest_asyncio',)

logger = logging.getLogger(__name__)

# class TestCommentSingleVideo(unittest.TestCase):
#     def test_comment(self):
#         args = {"videos": "https://www.tiktok.com/@google/video/7291741762278739242"}
#         comments = TiktokScraper().get_comments(**args)
#         for comment in comments[0]:
#             print(comment.text)
#         self.assertTrue(len(comments[0]) > 0)

# class TestCommentMultipleVideos(unittest.TestCase):
#     def test_comment(self):
#         args = {"videos": ["https://www.tiktok.com/@google/video/7291741762278739242", "https://www.tiktok.com/@google/video/7286921045720730926"]}
#         comments = TiktokScraper().get_comments(**args)

#         self.assertTrue(len(comments[0]) > 0)

# class TestProfile(unittest.TestCase):
#     async def test_profile(self):
#         TS = TiktokScraper()
#         await TS._initialize_browser(use_browser_cookies=True)
#         args = {"profiles": ["google", "microsoft"]}
#         profile = await TS.get_profile_details(**args)

#         logger.debug(profile)
#         logger.debug(profile[0].__dict__)

#         self.assertGreater(profile[0].follower_count, 10)
#         self.assertGreater(profile[0].heart_count, 10)
#         self.assertEqual(profile[0].nickname, "Google")
#         self.assertTrue(profile[0].verified)

#         profile = await TS.get_profile_details(**{"profiles": ["samsung"]})
                                            
#         logger.debug(profile)
#         self.assertEqual(profile[0].nickname, "Samsung")

# class TestVideosOfUser(unittest.TestCase):
#     async def test_videos(self):
#         TS = TiktokScraper()
#         await TS._initialize_browser(use_browser_cookies=True)
#         videos = await TS.get_videos_of_user("microsoft")

#         logger.debug(videos)
#         logger.debug(videos[0].__dict__)

#         self.assertGreater(len(videos), 10)
#         self.assertGreater(videos[0].play_count, 10)

#         for video in videos:
#             if video.download_url is None:
#                 logger.debug(video.__dict__)    

# class TestVideoDetails(unittest.TestCase):
#     async def test_video_details(self):
#         TS = TiktokScraper()
#         await TS._initialize_browser(use_browser_cookies=True)
#         video_urls = [
#             "https://www.tiktok.com/@google/video/7333724070804032811",
#             "https://www.tiktok.com/@google/video/7327746022120099115",
#             "https://www.tiktok.com/@google/video/7327016920472079662"
#         ]
#         videos = await TS.get_video_details(video_urls)

#         logger.debug(videos[0].__dict__)
#         for video in videos:
#             self.assertGreater(video.play_count, 100)

class TestGetTrending(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_get_trending_videos(self):
        TS = TiktokScraper()
        await TS._initialize_browser(use_browser_cookies=True)
        videos = await TS.get_trending_videos()

        logger.debug("Videos: ", videos)
        
        self.assertGreater(len(videos), 0)
        self.assertGreater(videos[0].play_count, 10)

        return videos

# class TestGetFollowersForUser(unittest.TestCase):
#     def test_get_followers(self):
#         TS = TiktokScraper()
#         # secUid: Google
#         secUid = "MS4wLjABAAAABqImMisT8O3jtr2Ufg4t7wTYypL4gPC9rWRrIkkThwCgCVMRJW6ls-n2T6bmDMZb"
#         followers = TS.get_followers_for_user(secUid, limit=100)

#         self.assertEqual(len(followers), 100)

# class TestGetVideosForKeyword(unittest.TestCase):
#     async def test_get_videos_for_keyword(self):
#         TS = TiktokScraper()
#         await TS._initialize_browser(use_browser_cookies=True)
#         videos = await TS.get_videos_for_keyword("google", limit=24)

#         self.assertEqual(len(videos), 24)
