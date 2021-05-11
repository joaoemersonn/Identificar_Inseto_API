from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
@app.route('/')
def hello():
    return 'Hello, World'


@app.route('/identifyinsect', methods=['POST'])
def upload_file():
    f = request.files['the_file']
    f.save('./uploads/%s' % f.filename)

    # codigo aqui!
    # O retorno pode ser um JSON!
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
