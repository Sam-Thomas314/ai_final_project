import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers = headers)

    formatted_response = json.loads(response.text)

    score_dictionary = {}
  
    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

        score_dictionary["anger"] = anger_score
        score_dictionary["disgust"] = disgust_score
        score_dictionary["fear"] = fear_score
        score_dictionary["joy"] = joy_score
        score_dictionary["sadness"] = sadness_score
        score_dictionary["dominant_emotion"] = dominant_emotion
    else:
        dominant_emotion = max(score_dictionary, key=score_dictionary.get)

        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score  = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score  = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score  = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score  = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        score_dictionary["anger"] = anger_score
        score_dictionary["disgust"] = disgust_score
        score_dictionary["fear"] = fear_score
        score_dictionary["joy"] = joy_score
        score_dictionary["sadness"] = sadness_score

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        "dominant_emotion": dominant_emotion,
        }
