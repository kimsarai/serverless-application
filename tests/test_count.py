import os
import sys

sys.path.append(os.environ["REPOSITORY_HOME"] + "/app/functions")
import count

def test_ok ():


    event = {
        'queryStringParameters': {
            'name': 'arai'
        }
    }
    context = {}  

    # lambda_handlerを呼び出す
    res = count.lambda_handler(event, context)

    status_code = res['statusCode']
    assert status_code == 200