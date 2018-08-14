from flask import Flask, request
import hashlib
import json
# from receive import parse_xml

app = Flask(__name__)

@app.route("/wx", methods=["GET", "POST"])
def handle():
    try:
        if request.method == 'GET':
            if len(request.args) == 0:
                return 'hello, this is handle view'
            signature = request.args.get('signature')
            timestamp = request.args.get('timestamp')
            nonce = request.args.get('nonce')
            echostr = request.args.get('echostr')
            token = "aptx4869"
            
            args_list = [token, timestamp, nonce]
            args_list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, args_list)
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr
            else:
                return ""
        if request.method == 'POST':
            data = request.form
            if data:
                return json.dumps(data)
            else:
                return 'success'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
