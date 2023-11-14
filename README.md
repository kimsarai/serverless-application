# serverless-application

Github ActionsでAWS SAM テンプレートをテストし、デプロイする CI/CD パイプラインを構築します。

AWS SAMテンプレートは以下の構成となっています。
・AWS DynamoDB
・AWS Lambda
・AWS API GateWay

DynamoDB：主キーとしてnameを設定
Lambda関数：エンドポイントのURLにパラメータを指定し、DynamoDBに主キーの値があれば、accessNumberが増加。なければ、登録。
API GateWay：Rest APIを使用

