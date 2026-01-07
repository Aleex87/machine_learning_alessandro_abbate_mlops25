from fastapi import FastAPI
from data_processing import library_data, Book

# list of elements that are pydantic models
books: list[Book] = library_data("library.json").books

app = FastAPI()

#  ----------------- READ --------------------

@app.get("/books")
async def read_books():
    # can return a pydantic model because
    # fastapi serializes it to json under the hood
    return books

# path parameter
@app.get("/book/{id}")
async def read_book_by_id(id: int):
    return [book for book in books if book.id == id]


#  ----------------- CREATE --------------------

@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)

    books.append(new_book)

    # to save / persist data 
    # ex logic foe writing to json (in append mode)
    # ex  open up a database connection and Insert row

 
    return new_book

#  ----------------- UPDATE --------------------

@app.put("/books/update_book")
async def update_book(update_book: Book):
    for i , book in enumerate(books):
        if book.id == update_book.id:
            books[i] = update_book
    return update_book
