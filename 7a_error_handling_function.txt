import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    emotion_dict = {'anger': None, 'disgust': None, 'fear': None,
    'joy': None, 'sadness': None, 'dominant_emotion': None }
    
    if response.status_code == 400 :
        return emotion_dict

    res = response.json() 
    res = res['emotionPredictions'][0]

    dictresponse =  res['emotion']
    
    emotion_dict['anger'] = dictresponse['anger']
    emotion_dict['disgust'] = dictresponse['disgust']
    emotion_dict['fear'] = dictresponse['fear']
    emotion_dict['joy'] = dictresponse['joy']
    emotion_dict['sadness'] = dictresponse['sadness']
    dom_key = ''
    max_score = 0.0
    for key in dictresponse.keys():
        if dictresponse[key] >= max_score:
            dom_key = key
            max_score = dictresponse[key]

    emotion_dict['dominant_emotion'] = dom_key
    
    return emotion_dict
