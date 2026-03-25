# SessionLog
パーソナルトレーナー向けに会員のセッション記録・成長グラフを管理するWebアプリ

## 技術スタック 
- Frontend: Nuxt 4 + Vue 3
- Backend: FastAPI (Python)
- DB: DynamoDB
- Infrastructure: AWS Lambda + API Gateway + Amplify

## ローカル起動方法

### フロントエンド
cd frontend
npm install
npm run dev

### バックエンド
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload