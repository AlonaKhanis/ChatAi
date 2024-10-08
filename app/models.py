from app import db
from datetime import datetime

class QuestionAnswer(db.Model):
    __tablename__ = 'question_answer'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
