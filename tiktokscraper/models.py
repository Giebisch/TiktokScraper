class Comment():
    """Entails all relevant data concerning a specific comment

    :ivar str comment_language: Comment language
    :ivar str text: Comment content
    :ivar str user: Username
    :ivar int reply_comment_total: Number of replies to the comment
    :ivar List[Comment] reply_comment: Replies
    """
    def __init__(self, api):
        self.comment_language = api["comment_language"]
        self.text = api["text"]
        self.user = api["user"]
        self.reply_comment_total = api["reply_comment_total"]

        # further processing necessary
        self.reply_comment = self._process_reply_comments(api["reply_comment"])
    
    def _process_reply_comments(self, reply_comments):
        return [Comment(comment) for comment in reply_comments]

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
    def __init__(self, api):
        api = api["userInfo"]
        self.follower_count = api["stats"]["followerCount"]
        self.following_count = api["stats"]["followingCount"]
        self.friend_count = api["stats"]["friendCount"]
        self.heart = api["stats"]["heart"]
        self.heart_count = api["stats"]["heartCount"]
        self.video_count = api["stats"]["videoCount"]
        self.commerce_user = bool(api["user"]["commerceUserInfo"]["commerceUser"])
        self.nickname = api["user"]["nickname"]
        self.private_account = bool(api["user"]["privateAccount"])
        self.signature = api["user"]["signature"]
        self.verified = bool(api["user"]["verified"])

class Video():
    """Entails all relevant data concerning a video

    :ivar str video_id: Video ID
    :ivar str description: Description
    """
    def __init__(self, api):
        self.video_id = api["video_id"]
        self.description = api["description"]
