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
    content_type = request.headers.get("Content-Type", "").lower()
    if "json" not in content_type:
        print(f"Rejected Content-Type: {content_type}")  # Debug print
        return jsonify({"message": "Unsupported Media Type"}), 415

    event_type = request.headers.get("X-GitHub-Event")
    payload = request.get_json(force=True, silent=True)

    if not payload:
        print("Invalid JSON received")  # Debug print
        return jsonify({"message": "Invalid JSON"}), 400

    event = format_event(event_type, payload)

    if event:
        save_event(event)
        print("✅ Event saved")  # Debug print
        return jsonify({"message": "Event saved"}), 200
    else:
        print("❌ Unsupported event type")  # Debug print
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
