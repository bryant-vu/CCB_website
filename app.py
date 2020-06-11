from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/about/')
def about():
    return render_template('about.html')

@app.route('/api/v1/appointments/')
def appointments():
    return render_template('appointments.html')

@app.route('/api/v1/barbers/')
def barbers():
    return render_template('barbers.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='192.168.1.10', port=port)
