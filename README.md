# Deeper Systems test: MongoDB User CRUD Application

This project includes:

- **Backend:** A Python script (`parser.py`) to import JSON data into MongoDB and a Flask API (`app.py`) providing CRUD operations.
- **Frontend:** A Vue 3 application using Vuetify for UI and Axios for HTTP requests.

## Prerequisites

- MongoDB (running on `localhost:27017`)
- Python 3.13.2
- Node.js and npm

## Setup Instructions

### Backend
1. Navigate to the backend folder:
   ```
   cd backend
   ```

2. Create a virtual environment and install dependencies (LINUX):
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Import data into MongoDB collection named myDatabase:
   ```
   python parser.py
   ```

4. Start the Flask server:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the frontend folder:
   ```
   cd frontend
   ```

2. install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run serve
   ```

# Project Structure

```
DEEPERSYSTEMSTEST/
├── backend/
│   ├── app.py
│   ├── parser.py
│   ├── requirements.txt
|   |── udata.json
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── main.js
│   │   ├── App.vue
│   │   ├── router.js
│   │   ├── components/
│   │   │   └── UserModal.vue
│   │   └── views/
│   │       ├── UserList.vue
│   │       └── UserDetail.vue
|
└── README.md
```
