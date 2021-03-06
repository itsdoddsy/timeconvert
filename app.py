from flask import Flask, jsonify, request
import dateparser
from dateutil import parser
from datetime import datetime

app = Flask(__name__)

# def ensure_future_tense(text):
#     if text.endswith("ago"):
#         return
#     return "in {}".format(text)

def getabsolute(time):
    gettime = str(dateparser.parse(time, settings={'PREFER_DATES_FROM': 'future'}))
    absolutetime = str(parser.parse(gettime).timestamp()).split('.')[0]
    return absolutetime

def getrelative(time, now):
    getnow = str(now.timestamp()).split('.')[0]
    getrelative = int(getabsolute(time)) - int(getnow)
    return getrelative
@app.route('/', methods=['GET', 'POST'])
def main():
    if 'input' in request.args:
        input = request.args.get('input')
        if input != '':
            return '{}, {}'.format(getabsolute(input), getrelative(input, datetime.now()))
        else:
            return 'Input required'
    else:
        return 'Input required'

if __name__ == '__main__':
    app.run()
