import pytest
from unittest.mock import patch
from flask import json
from app import create_app, db
from app.models import QuestionAnswer

@pytest.fixture
def app():
    app = create_app('testing')  
    with app.app_context():
        db.create_all() 
        yield app 
        db.session.remove()  
        db.drop_all() 

@pytest.fixture
def client(app):
    return app.test_client()


@patch('openai.ChatCompletion.create')
def test_question_answer(mock_openai, client):
    # Ensure the table is empty before the test runs
    with client.application.app_context():
        assert QuestionAnswer.query.count() == 0

    mock_openai.return_value = type('obj', (object,), {
        'choices': [
            type('obj', (object,), {
                'message': {
                    'content': 'Mocked response'
                }
            })()
        ]
    })

    question = {'question': 'Sample question?'}

    response = client.post('/ask', data=json.dumps(question), content_type='application/json')

    assert response.status_code == 200
    assert response.json['answer'] == 'Mocked response'

    with client.application.app_context():
        count = QuestionAnswer.query.count()
        assert count == 1  # Check if one record was created
        question_answer = QuestionAnswer.query.first()
        assert question_answer is not None
        assert question_answer.question == 'Sample question?'
        assert question_answer.answer == 'Mocked response'

@patch('openai.ChatCompletion.create')
def test_database_error(mock_openai, client):

    mock_openai.return_value = type('obj', (object,), {
        'choices': [
            type('obj', (object,), {
                'message': {
                    'content': 'Mocked response'
                }
            })()
        ]
    })

    
    with patch('app.db.session.commit', side_effect=Exception("Database error")):
        question = {'question': 'Sample question?'}

        response = client.post('/ask', data=json.dumps(question), content_type='application/json')

        assert response.status_code == 500
        assert response.json['error'] == 'Failed to save the answer to the database'