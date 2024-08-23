from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    ordered_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
    ordered_result = {key: result.get(key) for key in ordered_keys}

    return jsonify(ordered_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
