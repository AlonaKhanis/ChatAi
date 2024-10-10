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

        # Attempt to save the question and answer to the database
        question_answer = QuestionAnswer(question=question, answer=answer)
        db.session.add(question_answer)
        
        try:
            db.session.commit()
        except Exception as db_error:
            db.session.rollback() 
            logging.error(f"Database error occurred: {str(db_error)}")
            return jsonify({"error": "Failed to save the answer to the database"}), 500

        return jsonify({"answer": answer})

    except openai.error.OpenAIError as api_error:
        logging.error(f"OpenAI API error occurred: {str(api_error)}")
        return jsonify({"error": "Failed to get a response from the AI model"}), 500
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": "An internal error occurred"}), 500
