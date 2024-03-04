import pprint
from threading import Thread
import logging
from flask import Flask, render_template, request
from .TiktokScraper import TiktokScraper

logger = logging.getLogger(__name__)

app = Flask(__name__)
TS = TiktokScraper()
TS._initialize_browser(use_browser_cookies=True)

@app.route("/")
def index():
    return render_template("main.html")

@app.route('/api', methods=['GET'])
def get_result():
    global TS
    feature = request.args.get("feature")
    id = request.args.get("id")
    # format = request.args.get("format")

    if feature == "comments":
        comments = TS.get_comments(**{"videos": id})[0]
        return render_template('comments.html', comments=comments)
    
    if feature == "videos":
        videos = TS.get_videos_for_keyword(id)
        return render_template('videos.html', videos=videos)
    
    if feature == "profile":
        p = [x.strip() for x in id.split(",")]
        print(p)
        try:
            args = {"profiles": p}
            profiles = TS.get_profile_details(**args)
        except Exception as e:
            print("Somethings wrong")
            print(e)
        print(profiles)
        return render_template('profile_details.html', profiles=profiles)

app.run(host="0.0.0.0", port=5100)