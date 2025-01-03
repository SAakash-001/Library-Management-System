from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# In-memory storage
books = {
    1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    3: {"title": "1984", "author": "George Orwell", "year": 1949}
}
members = {}
book_id_counter = 4
member_id_counter = 1

# Authentication token
TOKEN = "secure_token"

# Helper: Authentication Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != f"Bearer {TOKEN}":
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

# Books CRUD
@app.route("/books", methods=["POST"])
@token_required
def add_book():
    global book_id_counter
    data = request.json
    books[book_id_counter] = {
        "title": data["title"],
        "author": data["author"],
        "year": data.get("year")
    }
    book_id_counter += 1
    return jsonify({"message": "Book added", "book_id": book_id_counter - 1}), 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    return jsonify(book)

@app.route("/books/<int:book_id>", methods=["PUT"])
@token_required
def update_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    data = request.json
    book.update({"title": data["title"], "author": data["author"], "year": data.get("year")})
    return jsonify({"message": "Book updated"})

@app.route("/books/<int:book_id>", methods=["DELETE"])
@token_required
def delete_book(book_id):
    if book_id not in books:
        return jsonify({"message": "Book not found"}), 404
    del books[book_id]
    return jsonify({"message": "Book deleted"})

# Members CRUD
@app.route("/members", methods=["POST"])
@token_required
def add_member():
    global member_id_counter
    data = request.json
    members[member_id_counter] = {
        "name": data["name"],
        "email": data["email"]
    }
    member_id_counter += 1
    return jsonify({"message": "Member added", "member_id": member_id_counter - 1}), 201

@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = members.get(member_id)
    if not member:
        return jsonify({"message": "Member not found"}), 404
    return jsonify(member)

@app.route("/members/<int:member_id>", methods=["PUT"])
@token_required
def update_member(member_id):
    member = members.get(member_id)
    if not member:
        return jsonify({"message": "Member not found"}), 404
    data = request.json
    member.update({"name": data["name"], "email": data["email"]})
    return jsonify({"message": "Member updated"})

@app.route("/members/<int:member_id>", methods=["DELETE"])
@token_required
def delete_member(member_id):
    if member_id not in members:
        return jsonify({"message": "Member not found"}), 404
    del members[member_id]
    return jsonify({"message": "Member deleted"})

# Search and Pagination
@app.route("/books", methods=["GET"])
def search_books():
    query = request.args.get("query", "").lower()
    page = int(request.args.get("page", 1))
    per_page = 5

    filtered_books = [
        {"id": book_id, **details}
        for book_id, details in books.items()
        if query in details["title"].lower() or query in details["author"].lower()
    ]

    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = filtered_books[start:end]

    return jsonify({"books": paginated_books, "total": len(filtered_books), "page": page})

if __name__ == "__main__":
    app.run(debug=True)
