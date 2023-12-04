from __future__ import annotations
from typing import List
import json
import logging

from .models import Comment, Profile, Video
from .scraping import get_comments_from_video, get_profile_details

logger = logging.getLogger(__name__)

class TiktokScraper():
    """Instantiates TiktokScraper object used for gathering various Tiktok data

    :ivar str user_agent: Provide custom user_agent
    :ivar List[str] proxies: Provide custom proxies
    :returns: Instantiated object
    :rtype: :class:`TiktokScraper`
    """
    def __init__(self, **kwargs) -> TiktokScraper:
        self.user_agent = kwargs["user-agent"] if "user-agent" in kwargs else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        self.proxies = kwargs["proxies"] if "proxies" in kwargs else []

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
        
        
    def get_comments(self, videos, limit_comments=50) -> List[Comment]:
        """Scrape comments from a specific video. Provide video url(s) or video id(s)

        :param List[str] videos: Provide video url(s) or video id(s). Can be a single string or list of strings
        :param int limit_comments: Maximum amount of comments
        :returns: :class:`tiktokscraper.models.Comment`
        :rtype: list
        """
        if type(videos) == str:
            videos = [videos]
        else:
            videos = videos
        
        comments = []
        for video in videos:
            comments.append(get_comments_from_video(self.user_agent, self.proxies, video, limit_comments))
        return comments

    def get_profile_details(self, profiles) -> List[Profile]:
        """Scrape all information regarding a specific profile. Provide profile url(s) or username(s)
        
        :param List[str] profiles: Provide profile url(s) or profile id(s). Can be a single string or list of strings
        :returns: :class:`tiktokscraper.models.Profile`
        :rtype: list
        """
        if type(profiles) == str:
            profiles = [profiles]
        else:
            profiles = profiles

        profile_details = []
        for profile in profiles:
            profile_details.append(get_profile_details(self.user_agent, self.proxies, profile))
        return profile_details

    def get_video_details(self, videos) -> List[Video]:
        """Scrape all relevant details from a specific video. Provide video url(s) or video id(s)

        :param List[str] videos: Provide video url(s) or video id(s). Can be a single string or list of strings
        :returns: :class:`tiktokscraper.models.Video`
        :rtype: list
        """
        return None

    def get_video_ids_of_user(self, user: str) -> List[str]:
        """Return all relevant video ids for a specific user. Provide user url or id

        :param user: Provide user url or id
        :returns: List of video ids of user
        :rtype: list
        """
        return None

    def get_videos_for_keyword(self, keyword: str, limit_videos=10) -> List[str]:
        """Return video ids for a specific keyword.

        :param keyword: Provide keyword
        :param int limit_videos: Maximum amount of videos
        :returns: List of video ids for keyword
        :rtype: list
        """
        return None

    def get_trending_videos(self, limit_videos=10) -> List[str]:
        """Return video ids for current trending videos.

        :param int limit_videos: Maximum amount of videos
        :returns: List of video ids of trending videos
        :rtype: list
        """
        return None
    
    def get_followers_for_user(self, user) -> List[str]:
        """Return followers for user. Provide user id or url

        :param str user: User id or url
        :returns: List of follower ids
        :rtype: list
        """
        return None
    
    def get_user_following(self, user) -> List[str]:
        """Return profiles the user is following. Provide user id or url

        :param str user: User id or url
        :returns: List of following ids
        :rtype: list
        """
        return None
