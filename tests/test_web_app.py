import os
import tempfile

import pytest

from app import app
from app.models import Url
from app.tasks import count_words_at_url
app.testing = True

@pytest.fixture
def new_url_deets():
    url = url = Url(url="https://www.google.com/", count=313)
    return url

def test_count_words_at_url(new_url_deets):
    task_url_deets = count_words_at_url(new_url_deets.url, to_store_in_db=0)
    assert new_url_deets.url == task_url_deets.url
    assert new_url_deets.count == task_url_deets.count