from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/detected')
def detected():
    return render_template('detected.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/otp')
def otp():
    return render_template('Otp.html')

if __name__ == '__main__':
    # Use 0.0.0.0 to listen on all public network interfaces (required for access from smartphone)
    # The default port is 5000, but 8080 is also a common alternative.
    # The debug=True parameter has been REMOVED as it is a security risk in production.
    app.run(host='0.0.0.0', port=8080)
