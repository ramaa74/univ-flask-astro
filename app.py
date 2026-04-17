import os
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sample_data import cameras_data, telescopes_data, photos_data, vlogs_data

app = Flask(__name__)

# CONFIG
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "development-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "mysql+pymysql://root:root@localhost/astro_db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# MODELS
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(255))

class Camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))  # Amateur, Amateur sérieux, Professionnel
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    release_date = db.Column(db.Date)
    score = db.Column(db.Integer)  # 1-5

class Telescope(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))  # Pour enfants, Automatisés, Complets
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    release_date = db.Column(db.Date)
    score = db.Column(db.Integer)  # 1-5

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    image_path = db.Column(db.String(500))

class VlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vlog_title = db.Column(db.String(200))
    username = db.Column(db.String(80))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# UTILITAIRES
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user" not in session:
            flash("Connectez-vous pour accéder à cette page.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped_view

@app.context_processor
def inject_user():
    return dict(logged_in="user" in session, current_user=session.get("user"))

@app.template_filter('static_image')
def static_image(path):
    if not path:
        return ''
    if path.startswith('http://') or path.startswith('https://'):
        return path
    if path.startswith('/'):
        path = path.lstrip('/')
    if path.startswith('static/'):
        path = path[len('static/'):]
    return url_for('static', filename=path)

# ROUTES
@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("cameras"))
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if User.query.filter_by(username=username).first():
            flash("Ce nom d’utilisateur existe déjà.", "danger")
            return render_template("register.html")

        user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        flash("Votre compte a bien été créé. Connectez-vous.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session["user"] = username
            flash(f"Bienvenue, {username}!", "success")
            return redirect(url_for("cameras"))

        flash("Nom d’utilisateur ou mot de passe incorrect.", "danger")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for("login"))

@app.route("/cameras")
@login_required
def cameras():
    cameras = Camera.query.order_by(Camera.category, Camera.brand).all()
    return render_template("cameras.html", cameras=cameras)

@app.route("/telescopes")
@login_required
def telescopes():
    telescopes = Telescope.query.order_by(Telescope.category, Telescope.brand).all()
    return render_template("telescopes.html", telescopes=telescopes)

@app.route("/photos")
@login_required
def photos():
    photos = Photo.query.all()
    return render_template("photos.html", photos=photos)

@app.route("/vlog", methods=["GET", "POST"])
@login_required
def vlog():
    if request.method == "POST":
        vlog_title = request.form.get("vlog_title")
        comment_text = request.form.get("comment", "").strip()
        if not comment_text:
            flash("Le commentaire ne peut pas être vide.", "warning")
        else:
            comment = VlogComment(vlog_title=vlog_title, username=session.get("user"), content=comment_text)
            db.session.add(comment)
            db.session.commit()
            flash("Votre commentaire a bien été ajouté.", "success")
        return redirect(url_for("vlog"))

    comments = VlogComment.query.order_by(VlogComment.created_at.desc()).all()
    comments_by_title = {}
    for comment in comments:
        comments_by_title.setdefault(comment.vlog_title, []).append(comment)

    return render_template("vlog.html", vlogs=vlogs_data, comments_by_title=comments_by_title)


def ensure_sample_data():
    if not Camera.query.first() and not Telescope.query.first() and not Photo.query.first():
        for cam in cameras_data:
            db.session.add(Camera(**cam))
        for tel in telescopes_data:
            db.session.add(Telescope(**tel))
        for ph in photos_data:
            db.session.add(Photo(**ph))
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        ensure_sample_data()
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
