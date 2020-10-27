import pytest
import os
from dotenv import load_dotenv, find_dotenv
from app import create_app, db

load_dotenv(find_dotenv())

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('config.TestingConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.session.close()
        db.drop_all()
