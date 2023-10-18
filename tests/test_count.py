import os
import sys

sys.path.append(os.environ["REPOSITORY_HOME"] + "/app/functions")
import Mock

def test_ok ():


    event = {
        'queryStringParameters': {
            'name': 'arai'
        }
    }
    context = {}  

    res = Mock.lambda_handler(event, context)

    status_code = res['statusCode']
    assert status_code == 200