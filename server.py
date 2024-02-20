"""
Emotion detection web app
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Endpoint for inedx page
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Endpoint for emotion detector
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return f"For the given statement, the system response is 'anger': {anger},\
     'disgust': {disgust},'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
     The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
