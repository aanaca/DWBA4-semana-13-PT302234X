import logging
import traceback

import flask
from replit import db

app = flask.Flask(__name__)

@app.errorhandler(500)
def internal_server_error(e: str):
    return flask.jsonify(error=str(e)), 500


@app.route('/', methods=['GET', 'POST'])
def cadastroContatos():
  try:
    contatos = db.get('contatos', {}); 
    print(contatos);
    if flask.request.method == "POST":
      nome = flask.request.form['nome']
      email = flask.request.form['email']
      telefone = flask.request.form['telefone']
      contatos[nome] = {'email': email, 'telefone': telefone, 'mensagem': mensagem,'opçoes de resposta': opçoes}
      db['contatos'] = contatos
      return flask.redirect('/')
    return flask.render_template('contatos.html', contatos=contatos)
  except Exception as e:
    logging.exception('failed to database')
    flask.abort(500, description=str(e) + ': ' + traceback.format_exc())

@app.route('/limparBanco', methods=['POST'])
def limparBanco():
  try:
    del db["contatos"];
    return flask.render_template('contatos.html')
  except Exception as e:
    logging.exception(e)
    return flask.render_template('contatos.html')

app.run('0.0.0.0')