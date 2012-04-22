import os
from app.models import UserProfile
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def basic_redirect():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    up = UserProfile.objects.all()
    return render_template('index.html', userprofiles=up)

@app.route('/hawka')
def hawka():
    return render_template('hawka.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
