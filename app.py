from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models import save_event, get_latest_events
from utils import format_event

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.json
    event = format_event(event_type, payload)

    if event:
        save_event(event)
        return jsonify({"message": "Event saved"}), 200
    else:
        return jsonify({"message": "Unsupported event"}), 400

@app.route("/events", methods=["GET"])
def events():
    events = get_latest_events()
    for e in events:
        e["_id"] = str(e["_id"])
        e["timestamp"] = e["timestamp"].strftime("%d %b %Y - %I:%M %p UTC")
    return jsonify(events)

if __name__ == "__main__":
    app.run(port=5000)
