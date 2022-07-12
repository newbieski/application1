import mysql.connector
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response


from urllib.request import urlopen
from bs4 import BeautifulSoup



def mycurl(url) :
    html = urlopen("https://"+url)
    bsObject = BeautifulSoup(html, "html.parser")
    res = []

    for link in bsObject.find_all('a'):
        res.append(link.text.strip() + link.get('href'))
    return "\n".join(res)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world2(username=None) :
    return 'hello world! {}'.format(username)

@app.route('/curl/<url>')
def curl_url(url=None) :
    return mycurl(url)


def main():
    app.debug = False
    app.run(host='127.0.0.1', port='5001')

if __name__ == '__main__' :
    main()