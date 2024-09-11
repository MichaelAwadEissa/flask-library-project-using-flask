# from app.models import Blogs, db
# from flask import render_template, request, redirect, url_for, Blueprint
# from app.blogs import blogs_blueprint


# @blogs_blueprint.route("/", endpoint="list")
# def blogs_list():
#     blogs = Blogs.query.all()
#     return render_template("blogs/list.html", blogs=blogs)


# @blogs_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
# def blogs_create():
#     # print(request.method, request.form)
#     if request.method == "POST":
#         blog = Blogs(
#             name=request.form["name"],
#             description=request.form["description"],
#             image=request.form["image"],
#         )
#         db.session.add(blog)
#         db.session.commit()
#         return redirect(blog.show_url)

#     return render_template("blogs/create.html")


# @blogs_blueprint.route("<int:id>/update", endpoint="update", methods=["GET", "POST"])
# def blogs_update(id):
#     blog = db.get_or_404(Blogs, id)
#     if request.method == "POST":
#         # print("requested blog----------->\n", request.form)
#         # print("-==->", request.POST["name"])
#         # print("-==->", request.form["name"])
#         blogobj = blog
#         blogobj.name = request.form["name"]
#         blogobj.description = request.form["description"]
#         blogobj.image = request.form["image"]
#         db.session.add(blogobj)
#         db.session.commit()
#         return redirect(url_for("blogs.list"))

#     return render_template("blogs/update.html", blog=blog)


# @blogs_blueprint.route("<int:id>", endpoint="show")
# def blog_show(id):
#     blog = db.get_or_404(Blogs, id)
#     return render_template("blogs/show.html", blog=blog)


# @blogs_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
# def blogs_delete(id):
#     blog = db.get_or_404(Blogs, id)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect(url_for("blogs.list"))


# # use -> url_for
# # @blogs_blueprint.route("<int:id>/delete", endpoint="delete")
# # def blogs_delete(id):
# #     blog = db.get_or_404(Blogs, id)
# #     db.session.delete(blog)
# #     db.session.commit()
# #     return redirect(url_for("blogs.list"))
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/library'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/books')
def list_books():
    books = Book.query.all()
    return render_template('list.html', books=books)

@app.route('/books/<int:id>')
def show_book(id):
    book = Book.query.get_or_404(id)
    return render_template('show.html', book=book)

@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        cover_photo = request.form['cover_photo']
        num_pages = request.form['num_pages']
        description = request.form['description']
        new_book = Book(title=title, cover_photo=cover_photo, num_pages=num_pages, description=description)
        db.session.add(new_book)
        db.session.commit()
        flash('Book created successfully!')
        return redirect(url_for('list_books'))
    return render_template('create.html')

@app.route('/books/<int:id>/update', methods=['GET', 'POST'])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.cover_photo = request.form['cover_photo']
        book.num_pages = request.form['num_pages']
        book.description = request.form['description']
        db.session.commit()
        flash('Book updated successfully!')
        return redirect(url_for('list_books'))
    return render_template('update.html', book=book)

@app.route('/books/<int:id>/delete', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!')
    return redirect(url_for('list_books'))

if __name__ == '__main__':
    app.run(debug=True)
