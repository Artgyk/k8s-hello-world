import os

import requests

def test_health():
    res = requests.get("http://localhost/hello-world/health")
    assert 200 == res.status_code