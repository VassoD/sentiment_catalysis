# Description: Sentiment Analysis with Coherence

from flask import Flask, render_template, request, jsonify
import cohere
from cohere.classify import Example
from config import API_KEY
import os
app = Flask(__name__)
co = cohere.Client(API_KEY)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        feedback = data['feedback']
        inputs = [feedback]
        response = co.classify(
            # model='de75337f-360c-41a7-a07a-ddcc026f6a2e-ft',
            model='edf20e4f-1466-4000-a319-4f008c3d7b7f-ft',
            inputs=inputs,
            # examples=examples,
        )
        for classification in response.classifications:
            prediction = classification.prediction
            break
        return jsonify({'prediction': prediction})
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
