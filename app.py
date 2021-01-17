from flask import Flask, jsonify, request, json

app = Flask(__name__)

desenvolvedores = [
    {'id': '0', 'nome': 'Estênio',
     'habilidades': ['PHP', 'Python']
     },
    {'id': '1', 'nome': 'Rafael',
     'habilidades': ['PHP', 'JavaScript']
     },
    {'id': '2', 'nome': 'Lucas',
     'habilidades': ['C', 'C#', 'C++']
     },
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
            desenvolvedor = desenvolvedores[id]
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador.'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso',
                        'mensagem': 'Registro excluído'})


@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)
