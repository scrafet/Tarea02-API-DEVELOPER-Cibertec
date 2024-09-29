from flask import Blueprint, render_template, url_for, flash, redirect, request
from models import User, Post, Comment
from forms import PostForm, CommentForm
from extensions import db, bcrypt  # Importar bcrypt para verificar contraseñas
from flask_login import login_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Autenticación del usuario
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Has iniciado sesión con éxito', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Inicio de sesión incorrecto, por favor revisa tus credenciales', 'danger')
    return render_template('login.html')

@main.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=1)  # El id de usuario debe ser dinámico
        db.session.add(post)
        db.session.commit()
        flash('Tu publicación ha sido creada con éxito!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Nuevo Post', form=form)

@main.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        flash('Tu comentario ha sido añadido con éxito!', 'success')
        return redirect(request.url)
    return render_template('post.html', title=post.title, post=post, form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión con éxito.', 'info')
    return redirect(url_for('main.home'))
