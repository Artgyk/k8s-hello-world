import pytest
from flask.testing import FlaskClient

from hello_world import api


@pytest.fixture()
def client() -> FlaskClient:
    return api.app.test_client()


def test_get_hello_world(client: FlaskClient):
    res = client.get("/hello")

    assert 200 == res.status_code
    assert b'hello world' == res.data


def test_get_health(client: FlaskClient):
    res = client.get("/health")

    assert 200 == res.status_code
