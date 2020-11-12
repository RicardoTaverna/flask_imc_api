from flask import Flask, request, make_response, jsonify, render_template

app = Flask('__name__')

@app.route('/healthcheck', methods=['GET'])
def health_check():
    return 'ok', 200

@app.route('/imc', methods=['POST'])
def calcula_imc():
    body = request.get_json()
    peso = float(body['peso'])
    altura = float(body['altura'])
    if altura > 0 and peso > 0:
        resultado = round(peso / altura ** 2, 2)
        res = make_response(jsonify({"resultado": resultado}), 200)
        return res
    else:
        res = make_response(jsonify({"resultado": "valores incorretos"}), 400)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)