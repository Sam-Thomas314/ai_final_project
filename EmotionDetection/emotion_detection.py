import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers = headers)

    formatted_response = json.loads(response.text)

    score_dictionary = {}

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    score_dictionary["anger"] = anger_score

    disgust_score  = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    score_dictionary["disgust"] = disgust_score

    fear_score  = formatted_response['emotionPredictions'][0]['emotion']['fear']
    score_dictionary["fear"] = fear_score

    joy_score  = formatted_response['emotionPredictions'][0]['emotion']['joy']
    score_dictionary["joy"] = joy_score

    sadness_score  = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    score_dictionary["sadness"] = sadness_score

    dominant_emotion = max(score_dictionary, key=score_dictionary.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        "dominant_emotion": dominant_emotion,
        }
