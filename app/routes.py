from flask import Blueprint, json, render_template, request, jsonify
from app.models import db, QuestionAnswer
import http.client
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/chat', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')

    # Send question to ChatGPT (via RapidAPI)
    conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")
    payload = f'{{"messages":[{{"role":"user","content":"{question}"}}],"web_access":false}}'
    headers = {
        'x-rapidapi-key': os.getenv("RAPIDAPI_KEY"),
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    conn.request("POST", "/gpt4", payload, headers)
    res = conn.getresponse()
    data = res.read()

    response_data = data.decode("utf-8")
    response_json = json.loads(response_data)
    answer = response_json.get("result", "No response")

    # Save question and answer to the database
    question_answer = QuestionAnswer(question=question, answer=answer)
    db.session.add(question_answer)
    db.session.commit()

    return jsonify({"question": question, "answer": answer})
