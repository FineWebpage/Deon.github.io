from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return '<pre>{}</pre>'.format(soup.prettify())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
