from flask import render_template, request, redirect, url_for, flash, Blueprint
from flaskblog.models import Post
from flaskblog.main.forms import SearchForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect((url_for('main.result', text=form.search.data)))
    return render_template('search.html', form=form)


@main.route('/result/<string:text>')
def result(text):
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.title.contains(text))\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('result.html', text=text, posts=posts)
