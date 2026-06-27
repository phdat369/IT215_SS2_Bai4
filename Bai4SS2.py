from fastapi import FastAPI
books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20}
]
app = FastAPI()
@app.get("/books/low-stock")
def get_books_low_stock():
    list_book = []
    valid = False
    for book in books:
        if book.get("quantity") < 0:
            continue
        elif book.get("quantity") <= 5:
            list_book.append(book)
            valid = True
    if valid == False:
        return {"message":"Không có sách nào sắp hết hàng",
                "data": []}
    return {"message":"Danh sách các sách gần hết hàng",
            "data":list_book}