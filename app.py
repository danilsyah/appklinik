from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)