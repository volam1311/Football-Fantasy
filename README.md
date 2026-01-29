# Football Fantasy:

Football Fantasy is an AI-powered chatbot designed to answer all your questions about football (soccer). Whether you want to learn about legendary players, famous matches, tactical strategies, or keep up with the latest news and stats, this assistant is here to help. Just type your question about teams, players, tournaments, or anything football-related, and get instant, insightful responses to fuel your passion for the beautiful game.

## Key technology:

Front end:
- React 
- CSS

Back end:
- FastAPI
- OpenAI API

## How to run the app:

### 1. Clone the repository:

```
git clone https://github.com/volam1311/Football-Fantasy
```

### 2. Install dependencies for backend:

```
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the backend:
```
uvicorn main:app --reload
```

### 4. Install dependencies for frontend:

```
# Open the another tab for the terminal
cd client
npm install
npm run dev
```

The app will be running on the link: http://localhost:3000

