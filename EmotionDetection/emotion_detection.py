import requests
import json 

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    
    myobj = { "raw_document": { "text": text_to_analyze } } 
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header)  

    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_name = None
    else:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        dominant_emotion_name = "anger"
        max_score = anger_score

        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        if max_score < disgust_score:
            dominant_emotion_name = "disgust"
            max_score = disgust_score

        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        if max_score < fear_score:
            dominant_emotion_name = "fear"
            max_score = fear_score

        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        if max_score < joy_score:
            dominant_emotion_name = "joy"
            max_score = joy_score

        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        if max_score < sadness_score:
            dominant_emotion_name = "sadness"
            max_score = sadness_score

    return {'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion':dominant_emotion_name}