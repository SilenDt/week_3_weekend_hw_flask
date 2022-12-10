from flask import render_template, request, redirect
from app import app
from models.books import *
from models.book import *


@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def add_new_book():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  description = request.form['description']
  new_book = Book(title, author, genre, description)
  books.append(new_book)
  return redirect('/books')


@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
  delete_book_at_index(int(index))
  return redirect('/books')

@app.route('/books/<index>')
def book(index):
    return render_template('book.html', title="Book Details", book = books[int(index)])