import pprint
from threading import Thread
from flask import Flask, render_template, request
from .TiktokScraper import TiktokScraper

app = Flask(__name__)
TS = TiktokScraper()

@app.route("/")
def index():
    return render_template("main.html")

@app.route('/api', methods=['GET'])
def get_result():
    global TS
    feature = request.args.get("feature")
    id = request.args.get("id")
    format = request.args.get("format")

    if feature == "comments":
        comments = TS.get_comments(**{"videos": id})[0]
        if format == "JSON":
            json = [pprint.pformat(c.json()).replace("\n", "<br>") for c in comments]
            json = "<br>".join(json)
            return render_template('json.html', json=json)
        return render_template('comments.html', comments=comments)
    
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