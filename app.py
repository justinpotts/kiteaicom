from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message
from flask_sslify import SSLify

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'hello@kiteai.com'
app.config['MAIL_PASSWORD'] = 'KiteAI2017'
app.config['TESTING'] = False
app.config['DEBUG'] = True
#sslify = SSLify(app)
mail = Mail(app)


def email(request):
    return_url = request.form['return']
    print return_url
    contact = request.form['email']

    msg = Message('SALES', sender='hello@kiteai.com', recipients=['hello@kiteai.com'])
    msg.body = contact
    mail.send(msg)

    return redirect(url_for(return_url, success=[True]))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email(request)
    return render_template('index.html')


@app.route('/why')
def why():
    if request.method == 'POST':
        email(request)
    return render_template('why.html')


@app.route('/features')
def features():
    if request.method == 'POST':
        email(request)
    return render_template('features.html')


@app.route('/demo')
def demo():
    if request.method == 'POST':
        email(request)
    return render_template('demo.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
