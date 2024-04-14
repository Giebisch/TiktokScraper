from __future__ import annotations
from typing import List
import json
import logging
import time
import re

from .models import Comment, Profile, Video
from .scraping import get_comments_from_video, get_profile_detail, get_videos_for_user, get_trending_videos, get_followers_for_user, get_video_for_keyword

from playwright.async_api import async_playwright
import rookiepy
import requests

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

        self.playwright_storage = None
    
    async def _initialize_browser(self, use_browser_cookies=False, browser="firefox") -> None:
        """Opens browser to initialize context, also used to sign in.

        :rtype: None
        """
        if self.playwright_storage is not None:
            return
        p = await async_playwright().start()
        if use_browser_cookies:
            if browser == "firefox":
                cookies = rookiepy.firefox(["tiktok"])
            elif browser == "safari":
                cookies = rookiepy.safari(["tiktok"])
            else:
                cookies = rookiepy.chrome(["tiktok"])
            browser = await p.chromium.launch(headless=True)
            formatted_cookies = []
            for cookie in cookies:
                if cookie["expires"] is None:
                    cookie.pop("expires", None)
                formatted_cookies.append(cookie)
            logger.debug(formatted_cookies)
            context = await browser.new_context()
            await context.add_cookies(formatted_cookies)
        else:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
            page = await context.new_page()
            
            await page.goto("https://www.tiktok.com/@google")
            with await page.expect_response(lambda response: "verification-i18n.tiktok.com/captcha/verify?" in response.url) as response_info:
                time.sleep(155)
        self.playwright_storage = await context.storage_state()
        await browser.close()
        await p.stop()
        
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

    async def get_profile_details(self, profiles) -> List[Profile]:
        """Scrape all information regarding a specific profile. Provide profile url(s) or username(s)
        
        :param List[str] profiles: Provide profile url(s) or profile id(s). Can be a single string or list of strings
        :returns: :class:`tiktokscraper.models.Profile`
        :rtype: list
        """
        if type(profiles) == str:
            profiles = [profiles]

        await self._initialize_browser()

        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=self.playwright_storage)

        profile_details = []
        for profile in profiles:
            context, profile_detail = await get_profile_detail(context, profile)
            profile_details.append(profile_detail)

        self.playwright_storage = await context.storage_state()

        await browser.close()
        await p.stop()

        return profile_details

    async def get_video_details(self, videos) -> List[Video]:
        """Scrape all relevant details from a specific video. Provide video urls

        :param List[str] videos: Provide video urls.
        :returns: :class:`tiktokscraper.models.Video`
        :rtype: list
        """

        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        video_details = []
        for video in videos:
            response = await page.goto(video)
            await page.wait_for_function('document.documentElement.outerHTML.includes("__UNIVERSAL_DATA_FOR_REHYDRATION__")')

            item_info = re.compile(r'webapp\.video-detail":{"itemInfo":(.*}),"shareMeta"')
            result = re.findall(item_info, await response.text())
            if result:
                result_dict = json.loads(result[0])["itemStruct"]
                video_details.append(Video(**result_dict))

        await browser.close()
        await p.stop()

        return video_details

    async def get_videos_of_user(self, user: str) -> List[Video]:
        """Return all relevant video ids for a specific user. Provide username

        :param user: Provide username
        :returns: List of videos of user
        :rtype: list
        """

        # Todo: option to provide secUid instead of username

        await self._initialize_browser()

        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=self.playwright_storage)

        context, profile = await get_profile_detail(context, user)

        context = await browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
        context, videos = await get_videos_for_user(context, profile.secUid)

        self.playwright_storage = await context.storage_state()
        await browser.close()
        await p.stop()

        return videos

    async def get_videos_for_keyword(self, keyword: str, limit=10) -> List[str]:
        """Return video ids for a specific keyword.

        :param keyword: Provide keyword
        :param int limit_videos: Maximum amount of videos
        :returns: List of video ids for keyword
        :rtype: list
        """
        await self._initialize_browser()
        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=self.playwright_storage)

        videos = await get_video_for_keyword(context, keyword, limit=limit)
        await browser.close()
        await p.stop()

        return videos
    
    async def get_trending_videos(self, limit_videos=10) -> List[Video]:
        """Return video ids for current trending videos.

        :returns: List of video ids of trending videos
        :rtype: list
        """
        await self._initialize_browser()
        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=self.playwright_storage)

        videos = await get_trending_videos(context)
        await browser.close()
        await p.stop()

        return videos
    
    def get_followers_for_user(self, secUid, limit=5) -> List[Profile]:
        """Return followers for user. Provide secUid and optional limit

        :param str secUid: secUid
        :param int limit: Limit number of followers
        :returns: List of Profiles
        :rtype: list
        """
        profiles = get_followers_for_user(secUid, limit=limit)
        return profiles
