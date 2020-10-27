import json
import pytest
from app import db, JobsModel


def test_jobs(app):
    client = app.test_client()
    response = client.get('/api/v1/jobs')
    print(response)
    # data = json.loads(response.data.decode())
    assert response.status_code == 200

# def func(x):
#     return x + 1
#
#
# def test_answer():
    # assert func(4) == 5
