import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = input_json, headers=header)
    formatted_response = json.loads(response.text)
    emotionSet = formatted_response['emotionPredictions'][0]['emotion']
    return emotionSet

def emotion_predictor(text_to_analyze):
        anger_score = emotionSet['anger']
        disgust_score = emotionSet['disgust']
        fear_score = emotionSet['fear']
        joy_score = emotionSet['joy']
        sadness_score = emotionSet['sadness']
        max_emotion = max(emotionSet, key=emotionSet.get)
        formatted_emotion_response = {
                                        'anger': anger_score,
                                        'disgust': disgust_score,
                                        'fear': fear_score,
                                        'joy': joy_score,
                                        'sadness': sadness_score,
                                        'dominant_emotion': max_emotion
                                    }
        return formatted_emotion_response
