import os
import sys

sys.path.append(os.environ["REPOSITORY_HOME"] + "/app/functions")

import unittest.mock
import count  # count モジュールをインポート

def test_ok():
    event = {
        'queryStringParameters': {
            'name': 'arai'
        }
    }
    context = {}
    
    # Boto3リソースの get_item メソッドをモック
    with unittest.mock.patch('boto3.resource') as mock_resource:
        mock_table = unittest.mock.MagicMock()
        mock_resource.return_value.Table.return_value = mock_table

        mock_get_item = unittest.mock.MagicMock()
        mock_get_item.return_value = {'Item': {'name': 'arai', 'accessNumber': 42}}
        mock_table.get_item = mock_get_item

        # テスト対象のコードを実行
        res = count.lambda_handler(event, context)

    # 期待されるメソッド呼び出しが行われたことをアサート
    mock_get_item.assert_called_with(Key={'name': 'arai'})
    mock_table.update_item.assert_called_with(
        Key={'name': 'arai'},
        UpdateExpression='set accessNumber = :s',
        ExpressionAttributeValues={':s': 43}
    )

    # 他のアサーションを追加
    assert res == {"statusCode": 200, "body": 43}
