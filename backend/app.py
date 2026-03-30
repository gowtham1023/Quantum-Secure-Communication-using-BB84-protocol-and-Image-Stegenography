from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

from utils.encrypt import encrypt_message
from utils.decrypt import decrypt_message
from utils.stego import hide_data, extract_data

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
STEGO_PATH = "stego.png"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# 🔐 ENCRYPT ROUTE
@app.route("/encrypt", methods=["POST"])
def encrypt():
    try:
        file = request.files["image"]
        message = request.form["message"]

        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(image_path)

        # Encrypt message
        encrypted_hex, key_bits = encrypt_message(message)

        # Store key + encrypted message
        data_to_hide = key_bits + "::" + encrypted_hex

        # Hide inside image
        hide_data(image_path, data_to_hide, STEGO_PATH)

        return jsonify({
            "key": key_bits,
            "bitString": key_bits,
            "stego_image": "http://127.0.0.1:5000/stego"
        })

    except Exception as e:
        print("ERROR (ENCRYPT):", e)
        return jsonify({"error": "Encryption failed"}), 500


# 🖼 STEGO IMAGE ROUTE
@app.route("/stego")
def get_stego():
    return send_file(STEGO_PATH, mimetype='image/png')


# 🔓 DECRYPT ROUTE
@app.route("/decrypt", methods=["POST"])
def decrypt():
    try:
        if "image" not in request.files:
            return jsonify({"error": "Image not provided"}), 400

        file = request.files["image"]
        key = request.form.get("bitString")

        if not key:
            return jsonify({"error": "Key not provided"}), 400

        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(image_path)

        # Extract hidden data
        extracted_data = extract_data(image_path)

        if not extracted_data:
            return jsonify({"error": "No hidden data found"}), 400

        if "::" not in extracted_data:
            return jsonify({"error": "Corrupted data"}), 400

        stored_key, encrypted_hex = extracted_data.split("::", 1)

        # ❌ Key validation
        if stored_key != key:
            return jsonify({"error": "Invalid Key"}), 400

        # ✅ Decrypt
        message = decrypt_message(encrypted_hex, key)

        return jsonify({"message": message})

    except Exception as e:
        print("ERROR (DECRYPT):", e)
        return jsonify({"error": "Server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)