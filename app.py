from flask import Flask, request, render_template
import os
import base64

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    cmd = request.args.get('cmd')
    ret = None
    if cmd is not None:
       ret = "powershell.exe -exec bypass -enc " + base64.b64encode(cmd.encode('utf-16-le')).decode()
    return render_template("magie.html", ret=ret)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,host='0.0.0.0',port=port)
