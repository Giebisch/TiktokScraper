class TiktokScraper():
    def __init__(self, args):
        # arg commands
        self.video = args.video
        self.profile = args.profile
        # parsed data
        self._comments = None
        self._video = None
        self._profile_details = None
    def get_comments(self):
        return None
    def get_video_details(self):
        return None
    def get_profile_details(self):
        return None