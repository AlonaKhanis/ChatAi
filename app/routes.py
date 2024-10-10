from flask import Blueprint, request, jsonify
from app import db 
from app.models import QuestionAnswer
import openai
import os
import logging

main = Blueprint('main', __name__)

@main.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.json
        question = data.get('question')

        if not question:
            return jsonify({"error": "No question provided"}), 400

        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": question}],
            max_tokens=100
        )

        answer = response.choices[0].message['content'].strip() if response.choices else "No response"

       
        question_answer = QuestionAnswer(question=question, answer=answer)
        db.session.add(question_answer)
        db.session.commit()

        return jsonify({"answer": answer})

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}") 
        return jsonify({"error": "An internal error occurred"}), 500
