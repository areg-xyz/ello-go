import sys
import os
import azure.functions as func
from unittest.mock import Mock
import json
import pytest

# Add api directory to path to import the function
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../api')))
import function_app

def test_visitors_get():
    # Construct a mock HTTP request.
    req = func.HttpRequest(
        method='GET',
        body=None,
        url='/api/visitors'
    )

    # Call the function.
    resp = function_app.visitors(req)

    # Check the output.
    assert resp.status_code == 200
    # Initial count should be 0 (or whatever global state is)
    assert resp.get_body() == b"0"

def test_visitors_post_increment():
    # Mock POST to increment
    req = func.HttpRequest(
        method='POST',
        body=json.dumps({'visitor_id': 'test_user_1'}).encode('utf-8'),
        url='/api/visitors'
    )
    
    resp = function_app.visitors(req)
    assert resp.status_code == 200
    
    body = json.loads(resp.get_body())
    assert body['count'] >= 1
    
    # Verify GET returns updated count
    req_get = func.HttpRequest(
        method='GET',
        body=None,
        url='/api/visitors'
    )
    resp_get = function_app.visitors(req_get)
    assert resp_get.get_body() == str(body['count']).encode()
