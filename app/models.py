from app import db

class QuestionAnswer(db.Model):
    __tablename__ = 'question_answer'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
