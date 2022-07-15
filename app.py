from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

from urllib.request import urlopen
from bs4 import BeautifulSoup

from collections import defaultdict

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def mycurl(url) :
    html = urlopen("https://"+url)
    bsObject = BeautifulSoup(html, "html.parser")
    dict = defaultdict(int)
    
    for link in bsObject.find_all('a'):
        key = link.text.strip()
        key = key.replace(" ", "")
        dict[key] += 1    
    
    wordcloud = WordCloud(
        font_path = 'NanumBarunGothic.ttf',
        width = 800,
        height = 800,
        background_color="white",
        )

    wordcloud = wordcloud.generate_from_frequencies(dict)

    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    

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