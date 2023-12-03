import unittest
from argparse import Namespace
from tiktokscraper.TiktokScraper import TiktokScraper

class TestCommentSingleVideo(unittest.TestCase):
    def test_comment(self):
        args = {"videos": "https://www.tiktok.com/@google/video/7291741762278739242"}
        comments = TiktokScraper().get_comments(**args)
        self.assertTrue(len(comments[0]) > 0)

class TestCommentMultipleVideos(unittest.TestCase):
    def test_comment(self):
        args = {"videos": ["https://www.tiktok.com/@google/video/7291741762278739242", "https://www.tiktok.com/@google/video/7286921045720730926"]}
        comments = TiktokScraper().get_comments(**args)

        self.assertTrue(len(comments[0]) > 0)

class TestProfile(unittest.TestCase):
    def test_profile(self):
        args = {"profiles": "https://www.tiktok.com/@google"}

        profile = TiktokScraper().get_profile_details(**args)
        print(profile)
        assert len(profile[0]) > 0, profile
        self.assertTrue(len(profile[0]) > 0)
        self.assertGreater(profile.follower_count > 10)
        self.assertGreater(profile.heart_count > 10)
        self.assertEqual(profile.nickname, "Google")
        self.assertTrue(profile.verified)