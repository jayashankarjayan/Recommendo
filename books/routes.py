from flask import Blueprint, render_template

BOOKS_BLUEPRINT = Blueprint("book_routes", __name__, template_folder="templates")
BASE_ROUTE_PATH = "/books"

@BOOKS_BLUEPRINT.route(BASE_ROUTE_PATH, methods=['GET']) 
def display_all_books():
    return render_template('Books.html')

@BOOKS_BLUEPRINT.route(BASE_ROUTE_PATH + '/book_id', methods=['GET'])
def display_selected_book():
    return render_template("Book_Solo.html")
