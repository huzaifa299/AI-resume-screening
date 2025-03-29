from flask import Flask, render_template

#app = Flask(__name__)
import os
app = Flask(__name__, template_folder=os.path.join('..', 'templates'))

@app.route('/')
def home():
    return render_template('Login.html')  # Ensure you have an 'index.html' file in a 'templates' folder

if __name__ == '__main__':
    app.run(debug=True)