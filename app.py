from functools import wraps
from flask_bcrypt import Bcrypt
from flask import Flask, redirect, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap



app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/dbklinik'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)


from model.user import User
from model.dokter import Dokter
from model.obat import Obat
from model.pendaftaran import Pendaftaran
from model.suplier import Suplier
from model.pasien import Pasien



class Login(FlaskForm):
    username = StringField('', validators=[InputRequired()], render_kw={'autofocus': True, 'placeholder': 'Username'})
    password = PasswordField('', validators=[InputRequired()], render_kw={'autofocus':True, 'placeholder': 'Password'})
    level = SelectField('', validators=[InputRequired()], choices=[('Admin','Admin'), ('Dokter','Dokter'), ('Administrasi','Administrasi')])


def login_dulu(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'login' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route('/')
def index():
    if session.get('login') == True:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get('login') == True:
        return redirect(url_for('dashboard'))

    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data) and user.level == form.level.data:
                session['login'] = True
                session['id'] = user.id
                session['level'] = user.level
                return redirect(url_for('dashboard'))
        pesan = "Username atau Password anda salah "
        return render_template("login.html", pesan=pesan, form=form)
            
    return render_template('login.html', form=form)


@app.route('/dashboard')
@login_dulu
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout')
@login_dulu
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)