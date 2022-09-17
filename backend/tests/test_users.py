import pytest
import json

from backend.models.user_models_dal import UserQuizzDAL


def test_get_quizzes_for_user(client, monkeypatch, token):
    test_data = {"id":1,"title":"Python", "description":"for pythonista", "is_active": True}

    async def mock_get():
        return test_data

    monkeypatch.setattr(UserQuizzDAL, "get_all_quizzes_for_user", mock_get)

    response = client.get("/quizzes", headers=token)
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_categories_for_user(client, monkeypatch, token):
    test_data = {"id":1, "name": "API devs", "description": "for API developers"}

    async def mock_get():
        return test_data

    monkeypatch.setattr(UserQuizzDAL, "get_all_categories_for_user", mock_get)

    response = client.get("/quizzes/categories", headers = token)
    assert response.status_code == 200
    assert response.json() == test_data

def test_get_questions_for_user(client, monkeypatch, token):
    test_request_payload = {"quizz_id":1, "category_id": 1}
    test_response_payload = {"id": 1, "question_text": "Is your job important?"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(UserQuizzDAL, "get_questions_for_user", mock_post)

    response = client.post("/quizzes/categories/questions", data = json.dumps(test_request_payload), headers=token)

    assert response.status_code == 200
    assert response.json() == test_response_payload
    

def test_send_answer(client, monkeypatch, token):
    test_request_payload = {"question_id":1, "answer_text": "LOL. No."}
    test_response_payload = {"user_score": 0, "max_score": 1}


    response = client.post("/quizzes/categories/questions/answer", data = json.dumps(test_request_payload), headers=token)

    assert response.status_code == 200
    assert response.json() == test_response_payload
