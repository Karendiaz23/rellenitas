import sys
import os
import pytest

# Agrega la carpeta backend al path para que Python pueda encontrar app.py

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
