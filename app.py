from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/why')
def why():
    return render_template('why.html')


@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/demo')
def demo():
    return render_template('demo.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
