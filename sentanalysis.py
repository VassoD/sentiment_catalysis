# Description: Sentiment Analysis with Coherence

from flask import Flask, render_template, request
from flask import jsonify
import cohere
from cohere.classify import Example
from config import API_KEY

app = Flask(__name__)
co = cohere.Client(API_KEY)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        feedback = data['feedback']
        examples = [
            Example("The order came 5 days early", "positive"),
            Example("The item exceeded my expectations", "positive"),
            Example("I ordered more for my friends", "positive"),
            Example("I would buy this again", "positive"),
            Example("I like the product", "positive"),
            Example("It was good", "positive"),
            Example("I would recommend this to others", "positive"),
            Example("The package was damaged", "negative"),
            Example("The order is 5 days late", "negative"),
            Example("The order was incorrect", "negative"),
            Example("I want to return my item", "negative"),
            Example("The item\'s material feels low quality", "negative"),
            Example("The product was okay", "neutral"),
            Example("I received five items in total", "neutral"),
            Example("I bought it from the website", "neutral"),
            Example("I used the product this morning", "neutral"),
            Example("The product arrived yesterday", "neutral"),
        ]
        inputs = [feedback]
        response = co.classify(
            model='large',
            inputs=inputs,
            examples=examples,
        )
        for classification in response.classifications:
            prediction = classification.prediction
            break
        return jsonify({'prediction': prediction})
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
