import openai
from flask_cors import CORS
from flask import Flask, request, jsonify
app = Flask(__name__)
CORS(app)

openai_api = "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"

# this is where u can customize what role u want the ai to play
def askChat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a really cool Spanish friend. You would help the user learn Spanish by teaching spanish and entertaining conversations in spanish"},
                  {"role": "user", "content":prompt}],
                  temperature=0.7
    )
    return response["choices"][0]["message"]["content"]


@app.route('/', methods=['POST'])
def hi():
            # Ensure the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type. Expected JSON."}), 415

    data = request.get_json()  # Parse JSON data from the request
    userInput = data.get("message", "")
    if not userInput:
        return jsonify({"error": "No input provided"}), 400

    response = askChat(userInput)
    return jsonify({"response": response})
        # data = request.json
        # userInput = data.get("message", "")
        # if not userInput:
        #     return jsonify({"error": "no input provided"}), 400
        # response = askChat(userInput)
        # return jsonify({"response": response})
    # return jsonify({"message": "hi"})

@app.route('/ask', methods=['POST']) #this route triggers the ask function
def ask():

    data = request.json
    userInput = data.get("message", "")
    if not userInput:
        return jsonify({"error": "no input provided"}), 400
    
    
    response = askChat(userInput)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)