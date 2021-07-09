import pytest

import app as tested_app


@pytest.fixture
def client():
    tested_app.aplication.config['TESTING'] = True
    app = tested_app.aplication.test_client()
    return app


def test_get(client):
    r = client.get('/')
    assert r.data.decode('utf-8') == 'Moe Flask приложение.'
