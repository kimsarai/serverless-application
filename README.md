# serverless-application
Github ActionsでAWS SAM テンプレートをテストし、デプロイする CI/CDを構築します。

## 概要
GitHubにコードをプッシュすることでGitHub Actionsが起動し、AWS SAMでデプロイされます。AWS SAMテンプレートは下記のようになります。
- AWS DynamoDB
  - 主キーとしてnameを設定しています。
- AWS Lambda
  - エンドポイントのURLにパラメータを指定し、DynamoDBに主キーのvalue値があれば、accessNumberが1ずつ増加します。もし、value値がなければ、そのvalue値が登録されます。
- AWS API GateWay
  - Rest APIを使用しています。

## ファイル構成
```
.
├── README.md
├── .coverage
├── requirements.txt
├── samconfig.toml // SAMのパラメータを定義
├── template.yml // AWS SAMを定義
├── .github
│   └── workflows
│       └── github-actions.yml  // github actionsを定義
├── app
│   └── functions
│      ├── Mock.py // testファイル
│      └── count.py // Lambda関数の定義
└── tests 
    └── test_count.py // Lambdaのテストファイル
```

## 構成図面
<img width="670" alt="image" src="https://github.com/kimsarai/serverless-application/assets/144189297/99f06f53-b803-4e42-b20f-e82d3483367d">


