from __future__ import annotations
from typing import List
import json
import logging

from .models import Comment, Profile, Video
from .scraping import get_comments_from_video

logger = logging.getLogger(__name__)

class TiktokScraper():
    """Instantiates TiktokScraper object used for gathering various Tiktok data
    """
    def __init__(self, **kwargs) -> TiktokScraper:
        self.videos = None
        self.profiles = None

        # check if we want to scrape one video or several
        if "video" in kwargs:
            video_kwargs = kwargs["video"]
            if type(video_kwargs) == str:
                self.videos = [video_kwargs]
            else:
                self.videos = video_kwargs
        
        # check if we want to scrape one profile or several
        if "profile" in kwargs:
            profile_kwargs = kwargs["profile"]
            if type(profile_kwargs) == str:
                self.profiles = [profile_kwargs]
            else:
                self.profiles = profile_kwargs
        
        
    def get_comments(self, limit_comments=50) -> List[Comment]:
        """Scrape comments from a specific video. Provide video url or video id
        """
        if self.videos is None:
            logger.warning("No video IDs given")
            return
        
        comments = []
        for video in self.videos:
            comments.append(get_comments_from_video(video, limit_comments))
        return comments

    def get_profile_details(self, profile: str) -> Profile:
        """Scrape all information regarding a specific profile. Provide profile url or username
        """
        return None
    def get_video_details(self, video_url: str) -> Video:
        """Scrape all relevant details from a specific video. Provide video url or video id
        """
        return None
