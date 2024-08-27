"""
Emotion detection server
"""
import json
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    index page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
    emotion detection function
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    result_dic = json.loads(result)

    if result_dic['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
