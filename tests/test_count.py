import os
import sys

sys.path.append(os.environ["REPOSITORY_HOME"] + "/app/functions")
from unittest.mock import patch
import count

def test_ok ():


    event = {
        'queryStringParameters': {
            'name': 'arai'
        }
    }
    context = {}  

    res = count.lambda_handler(event, context)

    status_code = res['statusCode']
    assert status_code == 200