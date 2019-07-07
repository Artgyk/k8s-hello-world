import requests
import pytest

import subprocess


@pytest.fixture()
def host():
    try:
        out = subprocess.check_output(["minikube", 'ip'])
        return out.decode('utf-8').strip()
    except Exception:
        return 'localhost'


def test_health(host):
    res = requests.get(f"http://{host}/hello-world/health")
    assert 200 == res.status_code
