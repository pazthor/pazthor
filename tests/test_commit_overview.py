import sys, types
req = types.ModuleType("requests")
req.get = lambda *a, **k: None
req.post = lambda *a, **k: None
sys.modules.setdefault("requests", req)
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# These tests show how to mock external HTTP requests using unittest.mock.
# They serve as a brief tutorial and follow common best practices.
import io
from contextlib import redirect_stdout
from unittest.mock import patch

import commit_overview as co

# These tests follow best practices demonstrated in the tutorial, using
# patches for external API calls and verifying output without network access.

class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception("HTTP error")


def test_get_github_commits():
    data = [
        {
            "sha": "abc",
            "commit": {
                "author": {"date": "2025-06-01T12:00:00Z"},
                "message": "Initial commit",
            },
        }
    ]
    with patch("commit_overview.requests.get", return_value=FakeResponse(data)) as m:
        commits = co.get_github_commits("t", "owner", "repo")
        assert commits == [
            {
                "sha": "abc",
                "date": "2025-06-01T12:00:00Z",
                "message": "Initial commit",
            }
        ]
        m.assert_called_once()


def test_get_gitlab_commits():
    data = [
        {"id": "1", "committed_date": "2025-06-02T12:00:00Z", "title": "Fix"}
    ]
    with patch("commit_overview.requests.get", return_value=FakeResponse(data)) as m:
        commits = co.get_gitlab_commits("t", "proj")
        assert commits == [
            {
                "id": "1",
                "date": "2025-06-02T12:00:00Z",
                "message": "Fix",
            }
        ]
        m.assert_called_once()


def test_print_overview(capsys):
    commits = [
        {"date": "2025-06-01T12:00:00Z", "message": "Initial"}
    ]
    co.print_overview("GitHub", commits)
    out = capsys.readouterr().out
    assert "GitHub: 1 commits." in out


def test_generate_ai_summary():
    commits = [{"message": "Add feature"}]
    response = {"choices": [{"message": {"content": "Summary"}}]}
    with patch(
        "commit_overview.requests.post", return_value=FakeResponse(response)
    ) as m:
        summary = co.generate_ai_summary(commits, "key")
        assert summary == "Summary"
        m.assert_called_once()


def test_generate_ai_summary_no_key():
    commits = [{"message": "Add"}]
    summary = co.generate_ai_summary(commits, api_key=None)
    assert summary is None

