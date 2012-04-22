import os
from app.models import UserProfile
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', userprofiles=UserProfile.objects.all())

@app.route('/hawka')
def hawka():
    return render_template('hawka.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
