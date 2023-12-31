import datetime
import json

class Comment():
    """Entails all relevant data concerning a specific comment

    :ivar str comment_language: Comment language
    :ivar str text: Comment content
    :ivar str user_id: Unique username
    :ivar str user_nickname: User nickname (not unique)
    :ivar datetime.datetime create_time: Create time
    :ivar int reply_comment_total: Number of replies to the comment
    :ivar List[Comment] reply_comment: Replies
    """
    def __init__(self, **kwargs):
        self.comment_language = kwargs["comment_language"]
        self.text = kwargs["text"]
        self.user_id = kwargs["user"]["unique_id"]
        self.user_nickname = kwargs["user"]["nickname"]
        self.create_time = datetime.datetime.fromtimestamp(kwargs["create_time"])
        self.reply_comment_total = kwargs["reply_comment_total"]
        # further processing necessary
        self.reply_comment = self._process_reply_comments(kwargs["reply_comment"])
    
    def _process_reply_comments(self, reply_comments):
        if reply_comments:
            return [Comment(comment) for comment in reply_comments]
        return None
    
    def json(self):
        return json.dumps(self, default=lambda o: o.isoformat() if (isinstance(o, datetime.datetime)) else o.__dict__, 
            sort_keys=True, indent=4)

class Profile():
    """Entails all relevant data concerning a profile

    :ivar int follower_count: Follower count
    :ivar int following_count: Following count
    :ivar int friend_count: Friend count
    :ivar int heart: Heart
    :ivar int heart_count: Heart count
    :ivar int video_count: Video count
    :ivar bool commerce_user: Is commerce user True/False
    :ivar str nickname: Nickname
    :ivar bool private_account: Is private account True/False
    :ivar str signature: Signature
    :ivar bool verified: Is verified True/False
    """
    def __init__(self, **kwargs):
        api = api["userInfo"]
        self.follower_count = kwargs["stats"]["followerCount"]
        self.following_count = kwargs["stats"]["followingCount"]
        self.friend_count = kwargs["stats"]["friendCount"]
        self.heart = kwargs["stats"]["heart"]
        self.heart_count = kwargs["stats"]["heartCount"]
        self.video_count = kwargs["stats"]["videoCount"]
        self.commerce_user = bool(kwargs["user"]["commerceUserInfo"]["commerceUser"])
        self.nickname = kwargs["user"]["nickname"]
        self.private_account = bool(kwargs["user"]["privateAccount"])
        self.signature = kwargs["user"]["signature"]
        self.verified = bool(kwargs["user"]["verified"])

class Video():
    """Entails all relevant data concerning a video

    :ivar str video_id: Video ID
    :ivar str description: Description
    """
    def __init__(self, **kwargs):
        self.video_id = kwargs["video_id"]
        self.description = kwargs["description"]
