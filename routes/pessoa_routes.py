from flask import Blueprint, request, render_template
from services.pessoa_service import cadastra_pessoa, lista_pessoas

pessoa_bp = Blueprint('pessoa', __name__)

@pessoa_bp.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        id = request.form['id']
        nome_pessoa = request.form['nome']
        cadastra_pessoa(id, nome_pessoa)
    
    pessoas = lista_pessoas()
    return render_template('cadastro.html', pessoas=pessoas)
