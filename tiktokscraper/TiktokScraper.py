from __future__ import annotations
from typing import List

from .models import Comment, Profile, Video

class TiktokScraper():
    """Instantiates TiktokScraper object used for gathering various Tiktok data
    """
    def __init__(self, args) -> TiktokScraper:
        # arg commands
        self.video = args.video
        self.profile = args.profile
        # parsed data
        self._comments = None
        self._video = None
        self._profile_details = None
    def get_comments(self, video_url: str) -> List[Comment]:
        """Scrape comments from a specific video. Provide video url or video id
        """
        return None
    def get_profile_details(self, profile: str) -> Profile:
        """Scrape all information regarding a specific profile. Provide profile url or username
        """
        return None
    def get_video_details(self, video_url: str) -> Video:
        """Scrape all relevant details from a specific video. Provide video url or video id
        """
        return None
