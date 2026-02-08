import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP Emotion Detection endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Payload with the text to analyze
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Required headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send POST request
    response = requests.post(url, json=myobj, headers=header)
    
    try:
        # Parse JSON response
        formatted_response = json.loads(response.text)
        
        # Extract emotions dictionary
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Collect required emotions
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        
        # Find dominant emotion
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return formatted dictionary
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    
    except Exception as e:
        return {'error': str(e), 'response': response.text}