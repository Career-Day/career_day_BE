
import json
import pytest
import os
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from app import db, JobsModel

def test_hello(app):
  client = app.test_client()
  resp = client.get('/')
  import pdb; pdb.set_trace()
  data = json.loads(resp.data.decode())
  assert resp.status_code == 200

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
