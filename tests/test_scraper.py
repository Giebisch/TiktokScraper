import unittest
from argparse import Namespace
from tiktokscraper.TiktokScraper import TiktokScraper

class TestComment(unittest.TestCase):
    def test_comment(self):
        target_comment = "#TeamPixel"
        args = Namespace(video="https://www.tiktok.com/@google/video/7291741762278739242", profile=None, web=False)

        comments = TiktokScraper(args).get_comments()

        found = False
        for comment in comments:
            if comment.text == target_comment:
                found = True
                break
        self.assertTrue(found)

class TestProfile(unittest.TestCase):
    def test_profile(self):
        target_profile = "https://www.tiktok.com/@google"
        args = Namespace(video=None, profile=target_profile, web=False)

        profile = TiktokScraper(args).get_profile_details()

        self.assertGreater(profile.follower_count > 10)
        self.assertGreater(profile.heart_count > 10)
        self.assertEqual(profile.nickname, "Google")
        self.assertTrue(profile.verified)