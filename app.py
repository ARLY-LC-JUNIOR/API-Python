#Api - é um lugar de disponibilizar recursos e/ou funcionalidades. 
#Objetivo de criar uma Api que disponibiloza consulta, criação, edição e exclusão de livros. 
#URL - Localhost
#Recorsos - Livro
from flask import Flask, jsonify, request

app = Flask(__name__)

livros =[
    {   'id': 1,
        'titulo': 'Simplesmente Mujica Um Livro Onde o Mito e o Homem São Revelados sem Censuras',
        'autor':  'Alfredo garcia'
    },
    {  'id': 2,
        'titulo': 'Bob Dylan a voz de uma geração História Discografia Fotos e Documentos',
        'autor':  'Brian Southal'
    },
    {   'id': 3,
        'titulo': 'ACDC rock and roll ao máximo A história definitiva da maior banda de rock do mundo',
        'autor':  'Murray Engleheart e Arnaud Durieux'
    },
]
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
#Consultar por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
        for livro in livros:
            if livro.get('id') == id:   
                return jsonify(livro)    
#Editar id livro
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Criar novo livro
app.route('/livros',methods=['POST'])
def incluir_novo__livro():
    novo_livro = request.get_json()  
    livros.append(novo_livro)
    
    return jsonify(livros)

app.run(port=5000, host='localhost',debug=True)





