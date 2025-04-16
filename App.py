from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    temperature = data.get("temperature")
    heart_rate = data.get("heart_rate")
    motion_level = data.get("motion_level")

    # Dummy Logic (replace with ML model later if needed)
    if temperature > 100 or heart_rate > 150 or motion_level > 18:
        risk = "HIGH"
    else:
        risk = "LOW"

    return jsonify({"seizure_risk": risk})

if __name__ == '__main__':
    app.run(debug=True)
