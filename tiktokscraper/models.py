class Comment():
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
