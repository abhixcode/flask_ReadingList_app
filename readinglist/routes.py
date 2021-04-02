from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_ReadingList_app.readinglist.forms import ListForm
from flask_ReadingList_app.models import User, Readinglist, Booklist
from flask_ReadingList_app import create_app,db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

readinglist = Blueprint('readinglist', __name__)

@readinglist.route('/list')
@login_required
def home():
    #user = User.query.filter_by(username=username).first_or_404()
    readinglist = ["abc","1234"]
    #readinglist = Readinglist.query.filter_by(author=user)
    return render_template("books.html", readinglist=readinglist, title = "Bookhead")

@readinglist.route("/list/new", methods=['GET', 'POST'])
@login_required
def new_list():
    form = ListForm()
    if form.validate_on_submit():
        #alist = Readinglist(title=form.title.data, author=current_user)
        #abook = Booklist(bookname=form.bookname.data, book=form.title.data)
        
        #db.session.add(alist)
        #db.session.add(abook)
        #db.session.commit()
        flash('Your list has been created!', 'success')
        return redirect(url_for('readinglist.home'))
    return render_template('create_list.html', title='New List',
                           form=form, legend='New List')

@readinglist.route("/list/<int:list_id>")
def alist(list_id):
    #alist = Readinglist.query.get_or_404(list_id)
    booklist = ["abcbook","1234book"]
    return render_template('alist.html', title='abc', booklist=booklist)


@readinglist.route("/list/<int:list_id>/update", methods=['GET', 'POST'])
@login_required
def update_list(list_id):
    readinglist = Readinglist.query.get_or_404(list_id)
    booklist = Booklist.query.get_or_404(list_id)
    if readinglist.author != current_user:
        abort(403)
    form = ListForm()
    if form.validate_on_submit():
        readinglist.title = form.title.data
        booklist.bookname = form.bookname.data
        db.session.commit()
        flash('Your list has been updated!', 'success')
        return redirect(url_for('readinglist.alist', list_id=post.id))
    elif request.method == 'GET':
        form.title.data = readinglist.title
        form.bookname.data = booklist.bookname
    return render_template('create_list.html', title='Update List',
                           form=form, legend='Update List')


@readinglist.route("/list/<int:list_id>/delete", methods=['POST'])
@login_required
def delete_list(list_id):
    readinglist = Readinglist.query.get_or_404(list_id)
    booklist = booklist.query.get_or_404(list_id)
    if readinglist.author != current_user:
        abort(403)
    db.session.delete(booklist)
    db.session.delete(readinglist)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('readinglist.home'))

@readinglist.route("/list/<int:list_id>/add")
def addbook(list_id):
    #alist = Readinglist.query.get_or_404(list_id)
    booklist = ["abcbook","1234book"]
    return render_template('addbook.html', title='abc', booklist=booklist)
