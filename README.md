# SessionLog
パーソナルトレーナー向けに会員のセッション記録を管理するWebアプリ

## 技術スタック 
- Frontend: Nuxt 4 + Vue 3
- Backend: FastAPI (Python)
- DB: DynamoDB
- Infrastructure: AWS Lambda + API Gateway + Amplify

## アーキテクチャ

```
ブラウザ → Amplify (フロントエンド配信)
              ↓
         API Gateway → Lambda → DynamoDB
```

- フロントエンドはAmplifyでホスティング。GitHubのmainブランチへのマージで自動デプロイ
- バックエンドはAPI Gateway + Lambdaのサーバーレス構成。SAMでデプロイ
- DynamoDBはシングルテーブル設計。PK/SKのプレフィックスパターンでエンティティを区別

## 機能一覧

- 会員の登録・一覧表示・詳細表示・編集
- セッション（トレーニング日）の記録・一覧表示
- セッション明細（種目・セット数・レップ数・重量）の記録・一覧表示
- セッション登録時の体重・体脂肪率の記録

## 今後の実装予定

- 認証機能（Cognito。SAMテンプレートに定義済み、フロントエンド未連携）
- テスト
- 種目別の重量推移グラフ表示
- 体重・体脂肪率の推移グラフ表示
- `pages/index.vue` のリダイレクト改善（現在は `navigateTo` で `/members` に直接遷移）