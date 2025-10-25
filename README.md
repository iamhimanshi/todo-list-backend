# Todo List Backend API
A simple RESTful API for managing todo items, built with Python Flask.

## Features
- Create, read, update, and delete todo items
- In-memory data storage
- RESTful API design

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todo` | Get all todos |
| POST | `/todo` | Create a new todo |
| GET | `/todo/{id}` | Get a single todo by ID |
| PUT | `/todo/{id}` | Update a todo by ID |
| DELETE | `/todo/{id}` | Delete a todo by ID |

## How to Run

1. Install Flask: `pip install flask`
2. Run: `python app.py`
3. Server starts at: `http://localhost:5000`

##  Project Structure
- `app.py` - Main application with all 5 REST endpoints
- In-memory data storage (no database needed)
  
