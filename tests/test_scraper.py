import unittest
from argparse import Namespace
from tiktokscraper.TiktokScraper import TiktokScraper

class TestCommentSingleVideo(unittest.TestCase):
    def test_comment(self):
        args = {"video": "https://www.tiktok.com/@google/video/7291741762278739242"}
        comments = TiktokScraper(**args).get_comments()
        self.assertTrue(len(comments) > 0)

class TestCommentMultipleVideos(unittest.TestCase):
    def test_comment(self):
        args = {"video": ["https://www.tiktok.com/@google/video/7291741762278739242", "https://www.tiktok.com/@google/video/7286921045720730926"]}
        comments = TiktokScraper(**args).get_comments()

        self.assertTrue(len(comments) > 0)

class TestProfile(unittest.TestCase):
    def test_profile(self):
        target_profile = "https://www.tiktok.com/@google"
        args = Namespace(video=None, profile=target_profile, web=False)

        profile = TiktokScraper(args).get_profile_details()

        self.assertGreater(profile.follower_count > 10)
        self.assertGreater(profile.heart_count > 10)
        self.assertEqual(profile.nickname, "Google")
        self.assertTrue(profile.verified)