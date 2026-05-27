import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    res = response.json()['emotionPredictions']
    dictresponse =  res[0]['emotion']
    
    anger_score = dictresponse['anger']
    disgust_score = dictresponse['disgust']
    fear_score = dictresponse['fear']
    joy_score = dictresponse['joy']
    sadness_score = dictresponse['sadness']
    dom_key = ''
    max_score = 0.0
    for key in dictresponse.keys():
        if dictresponse[key] >= max_score:
            dom_key = key
            max_score = dictresponse[key]

    dominant_emotion = dom_key
    
    return {'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dom_key
    }
