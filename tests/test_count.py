import os
import sys

sys.path.append(os.environ["REPOSITORY_HOME"] + "/app/functions")
import count

def test_ok ():


    res = count.lambda_handler(1,2)

    status_code = res['statusCode']
    assert status_code == 200