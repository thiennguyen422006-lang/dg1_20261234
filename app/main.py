import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Lấy cấu hình từ biến môi trường
PORT = int(os.environ.get("PORT", 5000))
MSSV = os.environ.get("MSSV", "20261234")
DATA_FILE = "app/data/students.json"

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "OK",
        "mssv": MSSV
    }), 200

@app.route('/api/students', methods=['GET'])
def get_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
                return jsonify(data), 200
            except Exception:
                return jsonify({"error": "Loi doc du lieu"}), 500
    return jsonify({"error": "File không tồn tại"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
