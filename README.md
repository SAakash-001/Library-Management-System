# Library Management System - Flask API

## Overview
This is a Flask-based RESTful API for managing a library system. The API supports CRUD operations for books and members and includes search functionality, pagination, and token-based authentication.

---

## How to Run the Project

### Prerequisites
1. Install Python 3.7 or higher.
2. Install Flask:
   ```bash
   pip install flask
   ```

### Steps to Run
1. Clone the repository:
   ```bash
   git clone (https://github.com/SAakash-001/Library-Management-System)
   cd https://github.com/SAakash-001/Library-Management-System/run
   ```

2. Run the Flask server:
   ```bash
   python run.py
   ```

3. Access the API endpoints using tools like Postman, cURL, or directly via a browser (for GET requests).

### Example Commands
#### Add a Book:
```bash
curl -X POST http://127.0.0.1:5000/books \
-H "Content-Type: application/json" \
-H "Authorization: Bearer secure_token" \
-d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}'
```
#### Search Books:
```bash
curl -X GET http://127.0.0.1:5000/books?query=gatsby&page=1
```
---

## Design Choices

### 1. **In-Memory Storage**
   - Used Python dictionaries to store `books` and `members`. This avoids external database dependencies and simplifies setup.
   - Counters (`book_id_counter` and `member_id_counter`) ensure unique IDs for books and members.

### 2. **Authentication**
   - Implemented token-based authentication with a hardcoded token (`secure_token`).
   - Authentication is enforced for sensitive operations (e.g., POST, PUT, DELETE).

### 3. **RESTful Structure**
   - Endpoints follow REST principles for clarity and scalability.
   - Separate routes for CRUD operations and search.

### 4. **Pagination**
   - Added pagination for search results to enhance usability when dealing with large datasets.
   - Default `per_page` value is set to 5.

### 5. **Extensibility**
   - The design allows for future integration with a database or more advanced features like user roles or borrowing history.

---

## Assumptions and Limitations

### Assumptions
1. All users share a single token (`secure_token`).
2. Books and members are stored in-memory, meaning data will be reset if the server restarts.
3. Book titles and author names are case-insensitive during search.

### Limitations
1. **No Persistent Storage**: The system uses in-memory dictionaries, which are not suitable for production use.
2. **Hardcoded Token**: The token is hardcoded and not dynamically managed.
3. **Limited Validation**: Input validation is minimal (e.g., no checks for duplicate titles or email formats).
4. **Scalability**: In-memory storage limits scalability and performance for large datasets.

---

## API Endpoints

### **Books**
- **POST** `/books` (Add a book) *(Requires Token)*
- **GET** `/books/<book_id>` (Retrieve a book by ID)
- **PUT** `/books/<book_id>` (Update a book by ID) *(Requires Token)*
- **DELETE** `/books/<book_id>` (Delete a book by ID) *(Requires Token)*
- **GET** `/books?query=<query>&page=<page>` (Search books with pagination)

### **Members**
- **POST** `/members` (Add a member) *(Requires Token)*
- **GET** `/members/<member_id>` (Retrieve a member by ID)
- **PUT** `/members/<member_id>` (Update a member by ID) *(Requires Token)*
- **DELETE** `/members/<member_id>` (Delete a member by ID) *(Requires Token)*

---

## Future Enhancements
1. Integrate with a relational database (e.g., SQLite, PostgreSQL) for persistent storage.
2. Implement role-based access control for better security.
3. Add more comprehensive validation and error handling.
4. Create a frontend to interact with the API.

