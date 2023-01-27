// Get the form, result, and cat-images elements
const form = document.querySelector('form');
const result = document.querySelector('#result');
const catImages = document.querySelector('#cat-images');


// Add a submit event listener to the form
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the value of the feedback textarea
    const feedback = form.querySelector('textarea').value;

    // Send a POST request to the server with the feedback data
    fetch('/', {
        method: 'POST',
        body: JSON.stringify({
            feedback
        }),
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(res => res.json())
        .then(data => {
            // Extract the prediction property
            const prediction = data.prediction;
            // Update the result element with the prediction
            if (prediction === "anger") {
                fetch('https://api.thecatapi.com/v1/images/search')
                    .then(res => res.json())
                    .then(data => {
                        document.querySelector('#img-section img').src = data[0].url;
                    });
            } else if (prediction === "joy") {
                result.innerHTML = `<p>😊</p>`;
            } else if (prediction === "love") {
                result.innerHTML = `<p>❤️</p>`;
            } else if (prediction === "surprise") {
                result.innerHTML = `<p>😯</p>`;
            } else if (prediction === "fear") {
                result.innerHTML = `<p>😱</p>`;
            }
            else if (prediction === "sadness") {
                result.innerHTML = `<p>😢</p>`;
            }
        });

});

let recognition;
let transcribing = false;

function startRecognition() {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'fr-FR'; // set language to French
    recognition.start();

    recognition.onresult = function (event) {
        for (let i = event.resultIndex; i < event.results.length; i++) {
            let transcript = event.results[i][0].transcript;
            if (event.results[i].isFinal) {
                document.getElementById("transcription").innerHTML = transcript + " ";
            } else {
                document.getElementById("transcription").innerHTML = transcript;
            }
        }
    }
    transcribing = true;
}

function stopRecognition() {
    recognition.stop();
    transcribing = false;
}
