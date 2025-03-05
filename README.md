🛡️ X API Comment Watch

X API Comment Watch to aplikacja do monitorowania komentarzy na X.com (dawniej Twitter). Pozwala pobierać komentarze do tweetów użytkownika i zarządzać nimi – usuwać lub blokować użytkowników.

📂 Struktura projektu

/x-api-commentwatch
│── /frontend  (→ React/HTML/JS na Netlify)
│   ├─ index.html
│   ├─ style.css
│   └─ app.js
│─ /backend  (→ FastAPI na Railway/Render)
│   ├─ main.py
│   ├─ config.py
│   └─ requirements.txt
│─ .env  (→ Klucze API - tylko backend!)
│─ README.md

🚀 Funkcje

✅ Pobiera komentarze z X.com (Twitter)✅ Wyświetla komentarze na stronie✅ Pozwala zablokować użytkownika✅ API REST do zarządzania komentarzami

⚙️ Instalacja

🔹 1. Klonowanie repozytorium

git clone https://github.com/twoje-repozytorium.git
cd x-api-commentwatch

🔹 2. Backend (FastAPI)

Przejdź do katalogu backend i zainstaluj zależności:

cd backend
pip install -r requirements.txt

🔹 3. Plik .env

Utwórz plik .env w katalogu backend/ i wklej tam swoje klucze API:

API_KEY=your_api_key
API_KEY_SECRET=your_api_key_secret
BEARER_TOKEN=your_bearer_token
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret

🔹 4. Uruchomienie backendu

uvicorn main:app --reload

Teraz API będzie działać na http://127.0.0.1:8000.

🎨 Frontend (Netlify)

🔹 1. Konfiguracja app.js

W pliku frontend/app.js podmień API_URL na adres backendu:

const API_URL = "https://your-backend-url.com";  // Zmień na właściwy adres

🔹 2. Uruchomienie lokalnie

Możesz otworzyć index.html w przeglądarce lub użyć prostego serwera:

cd frontend
python -m http.server 8000

Teraz frontend działa na http://127.0.0.1:8000.

🔹 3. Wdrożenie na Netlify

Zaloguj się na Netlify: https://app.netlify.com/

Dodaj repozytorium frontend/.

Netlify automatycznie wdroży stronę.

🌍 Wdrożenie backendu (Railway/Render)

Zaloguj się na Railway: https://railway.app/

Dodaj nowy projekt i wrzuć kod backendu (backend/).

Dodaj zmienne środowiskowe .env (API Keys) w panelu Railway.

Railway wygeneruje URL backendu, np. https://your-backend-url.com.

Podmień API_URL w app.js na ten adres.

✅ Testowanie API

Możesz przetestować backend w przeglądarce lub Postman/Insomnia:

🔹 Pobranie komentarzy

GET https://your-backend-url.com/comments?username=elonmusk

🔹 Blokowanie użytkownika

POST https://your-backend-url.com/block-user
Content-Type: application/json
{
    "user_id": "123456789"
}

🛠 Technologie

Frontend: HTML, CSS, JavaScript (hostowany na Netlify)

Backend: FastAPI, Tweepy, SQLite (hostowany na Railway/Render)

Baza danych: SQLite (przechowuje blokowanych użytkowników)

