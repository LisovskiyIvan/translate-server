from flask import Flask, request
from flask_cors import cross_origin
from googletrans import Translator

app = Flask(__name__)

def trans(text, src, dest):
    translator = Translator()
    translation = translator.translate(text=text, src=src, dest=dest)
    resp = translation.text
    return resp


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def hello_world():
    value = request.get_json()
    text = value['text']
    src = value['src']
    dest = value['dest']
    res = trans(text, src, dest)
    return (res)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
