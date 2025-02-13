'''This is the server'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def self_analyzer():
    '''Analyze the answer to determine if the reponse was valid or not, print answer to webpage'''
    emotion_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(emotion_to_detect)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if anger is None:
        return "Invalid text! Please try again"
    return f"""
    For the given statement, the system response is anger {anger}, disgust {disgust},
    fear {fear}, joy {joy}, and sadness {sadness}.
    The dominanty emotion is {dominant_emotion}
    """

@app.route("/")
def render_index_page():
    '''Render home page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)
