import unittest
from unittest.mock import Mock, patch
import count  # Lambda関数をインポート

class TestCountLambda(unittest.TestCase):
    @patch('count.boto3.client')  # boto3.clientをモック
    def test_lambda_handler(self, mock_boto3_client):
        # モックのDynamoDBクライアントを作成
        dynamodb_mock = Mock()
        mock_boto3_client.return_value = dynamodb_mock

        # DynamoDBのget_itemメソッドのモックを設定
        dynamodb_mock.get_item.return_value = {
            'Item': {
                'name': 'arai',
                'accessNumber': 5
            }
        }

        # Lambdaのイベントとコンテキストを作成
        event = {
            'queryStringParameters': {
                'name': 'arai'
            }
        }
        context = {}

        # Lambda関数を呼び出す
        response = count.lambda_handler(event, context)

        # DynamoDBのget_itemメソッドが呼び出されたことを検証
        dynamodb_mock.get_item.assert_called_once_with(
            Key={'name': 'arai'}
        )

        # Lambda関数の結果を検証
        expected_response = {
            'statusCode': 200,
            'body': 6
        }
        self.assertEqual(response, expected_response)
