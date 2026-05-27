from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def send_analizer():
    text_to_analize = request.args.get('textToAnalize')
    response = emotion_detector(text_to_analize)
    txt = f"""For the given statement, the system response is 'anger': {response['anger']}, 
    'disgoust': {response['disgoust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}
    The dominant emotion is {response['dominant_emotion']}."""   
    return text


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
