from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    return result
    result_dic = json.loads(result)

    if result_dic['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
