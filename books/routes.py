from flask import Blueprint, render_template, request

BOOKS_BLUEPRINT = Blueprint("book_routes", __name__, template_folder="templates")
BASE_ROUTE_PATH = "/books"

@BOOKS_BLUEPRINT.route(BASE_ROUTE_PATH, methods=['GET']) 
def display_all_books():
    if request.cookies.get("recommendo_user_active"):
        return render_template('Books.html')

@BOOKS_BLUEPRINT.route(BASE_ROUTE_PATH + '/book_id', methods=['GET'])
def display_selected_book():
    if request.cookies.get("recommendo_user_active"):
        return render_template("Book_Solo.html")
