from flask import Flask, json, jsonify
from douyu import DouYu
from huya import get_real_url as get_huya_real_url
from bilibili import get_real_url as get_bilibili_real_url
app = Flask(__name__)


@app.route('/')
def index():
    return "This is the main page"


@app.route('/douyv/<rid>')
@app.route('/douyu/<rid>')
def douyv(rid):
    d = DouYu(rid)
    res = {
        "url": d.get_real_url()
    }
    return jsonify(res)


@app.route('/huya/<rid>')
def huya(rid):
    res = {
        "url": get_huya_real_url(rid)
    }
    return jsonify(res)


@app.route('/bilibili/<rid>')
def bilibili(rid):
    res = {
        "url": get_bilibili_real_url(rid)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
