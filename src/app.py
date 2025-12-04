from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

FAQ = [
    {"q":"what do you do","a":"I build automation tools and AI agents."},
    {"q":"how to contact","a":"Connect on LinkedIn: https://www.linkedin.com/in/vishalshelar-ai/"}
]

def simple_answer(msg):
    m=msg.lower()
    for f in FAQ:
        if f['q'] in m:
            return f['a']
    return "Sorry, I don't have an answer for that yet. I'm a demo chatbot."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    msg = data.get('msg','')
    reply = simple_answer(msg)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
