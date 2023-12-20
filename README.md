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

エンドポイントは下記の通りになる
```[text]
https://(API GateWayのエンドポイント)/?name=[パラメータを指定]
```


## ファイル構成
```
.
├── README.md
├── .coverage
├── requirements.txt
├── CFn
│   ├── role.yml // oidc用のロール
│   ├── template.yml // AWS SAMを定義
│   ├── samconfig.toml 
│   └── parameters
│       └── role-parameters.json
├── .github
│   └── workflows
│       └── github-actions.yml  // github actionsを定義
├── app
│   └── functions
│       └── count.py // Lambda関数の定義
└── tests 
    └── test_count.py // Lambdaのテストファイル
```

## 構成図面
<img width="670" alt="image" src="https://github.com/kimsarai/serverless-application/assets/144189297/99f06f53-b803-4e42-b20f-e82d3483367d">

## 構築順序
構築順序は下記前提

- CFnディレクトリ内のrole.ymlをデプロイする
```
aws cloudformation create-stack \
--stack-name スタック名 \
--template-body file://./テンプレート名 \
--capabilities CAPABILITY_NAMED_IAM \
--parameters file://./parameters/パラメータ名 \
```
- 指定したブランチにコミットをする

