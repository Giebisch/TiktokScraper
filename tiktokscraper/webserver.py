import pprint
from flask import Flask, render_template, request
from .TiktokScraper import TiktokScraper

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route('/api', methods=['GET'])
def get_result():
    feature = request.args.get("feature")
    id = request.args.get("id")
    format = request.args.get("format")

    if feature == "comments":
        comments = TiktokScraper().get_comments(**{"videos": id})[0]
        if format == "JSON":
            json = [pprint.pformat(c.json()).replace("\n", "<br>") for c in comments]
            json = "<br>".join(json)
            return render_template('json.html', json=json)
        return render_template('comments.html', comments=comments)

app.run(host="0.0.0.0", port=5100)