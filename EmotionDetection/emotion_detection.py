import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    input_json = {
        'raw_document': {
            'text': text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=input_json)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        emotion_predictions_list = response_json.get('emotionPredictions', [])
        emotion_predictions_dict = emotion_predictions_list[0]
        emotion_dict = emotion_predictions_dict.get('emotion', {})
        
        emotions = {}
        for emotion, value in emotion_dict.items():
            emotions[emotion] = value
        
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
        
        return emotions
    else:
        return f"Error: {response.status_code}, {response.text}"