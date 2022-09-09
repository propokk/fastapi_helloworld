import pytest
import json

from backend.models.admin_models_dals import AnswersDAL, CategoriesDAL, QuestionCategoriesDAL, QuestionsDAL, QuizzesDAL
from backend.models.conf_test_db import *


#####################################TEST POST REQUESTS################################

def test_create_quizz(client, monkeypatch):
    # await database_test.connect()

    # new_quizz = sa.insert(Quizzes).values(title="Python", description="for pythonista", is_active=True)
    # await database_test.fetch_one(query=new_quizz)
    test_request_payload = {"title":"Python", "description":"for pythonista", "is_active": True}
    test_response_payload = {"id":1, "title":"Python", "description":"for pythonista", "is_active": True}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(QuizzesDAL, "create_quizz", mock_post)

    response = client.post("/quizz", data = json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload

def test_create_quizz_invalid_json(client):
    response = client.post("/quizz", data = json.dumps({"title": "Python"}))
    assert response.status_code == 422
    
def test_create_question(client, monkeypatch):
    test_request_payload = {"question_text": "Is your job important?", "quizz_id": 1}
    test_response_payload = {"id":1, "question_text": "Is your job important?", "quizz_id": 1}
    
    async def mock_post(payload):
        return 1

    monkeypatch.setattr(QuestionsDAL, "create_question", mock_post)

    response = client.post("/question", data = json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload

def test_create_question_invalid_json(client):
    response = client.post("/question", data = json.dumps({"question_text": "Is your job important?"}))
    assert response.status_code == 422


def test_create_answer(client, monkeypatch):
    test_request_payload = {"answer_text": "LOL. No.", "question_id": 1, "is_correct": True}
    test_response_payload = {"id":1, "answer_text": "LOL. No.", "question_id": 1, "is_correct": True}
    
    async def mock_post(payload):
        return 1

    monkeypatch.setattr(AnswersDAL, "create_answer", mock_post)

    response = client.post("/answer", data = json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload

def test_create_answer_invalid_json(client):
    response = client.post("/answer", data = json.dumps({"answer_text": "LOL. No."}))
    assert response.status_code == 422



def test_create_category(client, monkeypatch):
    test_request_payload = {"name": "API devs", "description": "for API developers"}
    test_response_payload = {"id":1, "name": "API devs", "description": "for API developers"}
    
    async def mock_post(payload):
        return 1

    monkeypatch.setattr(CategoriesDAL, "create_category", mock_post)

    response = client.post("/category", data = json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload

def test_create_category_invalid_json(client):
    response = client.post("/category", data = json.dumps({"name": "API devs"}))
    assert response.status_code == 422


def test_create_question_category(client, monkeypatch):
    test_request_payload = {"question_id": 1, "category_id": 1}
    test_response_payload = {"id":1, "question_id": 1, "category_id": 1}
    
    async def mock_post(payload):
        return 1

    monkeypatch.setattr(QuestionCategoriesDAL, "create_question_category", mock_post)

    response = client.post("/question_category", data = json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload

def test_create_question_category_invalid_json(client):
    response = client.post("/question_category", data = json.dumps({"question_id": 1}))
    assert response.status_code == 422



#####################################TEST GET REQUESTS#################################

def test_get_quizz(client, monkeypatch):
    test_data = {"title":"Python", "description":"for pythonista", "is_active": True, "id": 1}

    async def mock_get():
        return test_data

    monkeypatch.setattr(QuizzesDAL, "get_all_quizzes", mock_get)

    response = client.get("/quizz")
    assert response.status_code == 200
    assert response.json() == test_data

def test_get_questions(client, monkeypatch):
    test_data = {"id":1, "question_text": "Is your job important?", "quizz_id": 1}

    async def mock_get():
        return test_data

    monkeypatch.setattr(QuestionsDAL, "get_all_questions", mock_get)

    response = client.get("/question")
    assert response.status_code == 200
    assert response.json() == test_data

def test_get_answer(client, monkeypatch):
    test_data = {"id":1, "answer_text": "LOL. No.", "question_id": 1, "is_correct": True}

    async def mock_get():
        return test_data

    monkeypatch.setattr(AnswersDAL, "get_all_answers", mock_get)
    
    response = client.get("/answer")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_category(client, monkeypatch):
    test_data = {"id":1, "name": "API devs", "description": "for API developers"}

    async def mock_get():
        return test_data

    monkeypatch.setattr(CategoriesDAL, "get_all_categories", mock_get)

    response = client.get("/category")
    assert response.status_code == 200
    assert response.json() == test_data

def test_get_question_category(client, monkeypatch):
    test_data = {"id":1, "question_id": 1, "category_id": 1}

    async def mock_get():
        return test_data

    monkeypatch.setattr(QuestionCategoriesDAL, "get_all_question_categories", mock_get)

    response = client.get("/question_category")
    assert response.status_code == 200
    assert response.json() == test_data



#####################################TEST PUT REQUESTS#################################


def test_update_quizz(client, monkeypatch):
    test_update_data = {"title":"PYTHON", "description":"for pythonista", "is_active": True, "id": 1}

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(QuizzesDAL, "update_quizz", mock_put)

    response = client.put("/quizz/1", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
    ],
)
def test_update_quizz_invalid(client, id, payload, status_code):

    response = client.put(f"/quizz/{id}", data=json.dumps(payload),)
    assert response.status_code == status_code



def test_update_questions(client, monkeypatch):
    test_update_data = {"id":1, "question_text": "Is your JOB important?", "quizz_id": 1}

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(QuestionsDAL, "update_question", mock_put)

    response = client.put("/question/1", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"question_text": "bar"}, 422],
    ],
)
def test_update_questions_invalid(client, id, payload, status_code):

    response = client.put(f"/question/{id}", data=json.dumps(payload),)
    assert response.status_code == status_code



def test_update_answers(client, monkeypatch):
    test_update_data = {"id":1, "answer_text": "LOL. YES.", "question_id": 1, "is_correct": True}

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(AnswersDAL, "update_answer", mock_put)

    response = client.put("/answer/1", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"answer_text": "bar"}, 422],
    ],
)
def test_update_questions_invalid(client, id, payload, status_code):

    response = client.put(f"/answer/{id}", data=json.dumps(payload),)
    assert response.status_code == status_code



def test_update_category(client, monkeypatch):
    test_update_data = {"id":1, "name": "API DEVS", "description": "for API developers"}

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(CategoriesDAL, "update_category", mock_put)

    response = client.put("/category/1", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"name": "bar"}, 422],
    ],
)
def test_update_questions_invalid(client, id, payload, status_code):

    response = client.put(f"/category/{id}", data=json.dumps(payload),)
    assert response.status_code == status_code



def test_update_question_category(client, monkeypatch):
    test_update_data = {"id":1, "question_id": 1, "category_id": 1}

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(QuestionCategoriesDAL, "update_question_category", mock_put)

    response = client.put("/question_category/1", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"question_id": 1}, 422],
    ],
)
def test_update_questions_invalid(client, id, payload, status_code):

    response = client.put(f"/question_category/{id}", data=json.dumps(payload),)
    assert response.status_code == status_code



#####################################TEST DELETE REQUESTS################################



def test_delete_quizz(client, monkeypatch):
    async def mock_delete(id):
        return id

    monkeypatch.setattr(QuizzesDAL, "delete_quizz", mock_delete)

    response = client.delete("/quizz/1")
    assert response.status_code == 200


def test_delete_question(client, monkeypatch):
    async def mock_delete(id):
        return id

    monkeypatch.setattr(QuestionsDAL, "delete_question", mock_delete)

    response = client.delete("/question/1")
    assert response.status_code == 200

def test_delete_answer(client, monkeypatch):
    async def mock_delete(id):
        return id

    monkeypatch.setattr(AnswersDAL, "delete_answer", mock_delete)

    response = client.delete("/answer/1")
    assert response.status_code == 200

def test_delete_category(client, monkeypatch):
    async def mock_delete(id):
        return id

    monkeypatch.setattr(CategoriesDAL, "delete_category", mock_delete)

    response = client.delete("/category/1")
    assert response.status_code == 200   

def test_delete_question_category(client, monkeypatch):
    async def mock_delete(id):
        return id

    monkeypatch.setattr(QuestionCategoriesDAL, "delete_question_category", mock_delete)

    response = client.delete("/question_category/1")
    assert response.status_code == 200   

