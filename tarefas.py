from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tarefas = [
    {
        'id':0,
        'responsavel':'Rafael',
        'tarefa':'Desenvolver método GET',
        'status': 'concluído'
    },
    {
        'id':1,
        'responsavel':'Gabriel',
        'tarefa':'Desenvolver método POST',
        'status': 'pendente'
    }
]

# para modificar o status de uma lista
# tarefas[1]['status'] = 'concluído'

# listar e incluir novas tarefas
@app.route('/tarefas/', methods=['GET', 'POST'])
def listarIncluir():
    if request.method == 'POST':
        # pegar os dados
        dados = json.loads(request.data)

        # tamanho da fila, vai me dar o valor do próximo id
        posicao = len(tarefas)

        # vai colocar o valor do id na próxima tarefa que for add
        dados['id'] = posicao

        # adicionar nova tarefa a fila
        tarefas.append(dados) 

        return jsonify({'status':'sucesso', 'mensagem':'Tarefa adicionada'})
    elif request.method == 'GET':
        # mostrar a lista completa
        return jsonify(tarefas)

# modificando status, passando ele na URL 
# @app.route('/tarefas/<int:id>/status', methods=['PUT'])
# def tarefa(id, status):
#     if request.method == 'PUT':
#         response = json.loads(response.data)
#         response[id]['status'] = status
#         return jsonify({'status':'sucesso', 'mensagem':'Status alterado'})

# mostrar a tarefa pelo id
# modificando status passando apenas o id
# deletar tarefa pelo id
@app.route('/tarefas/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        response = tarefas[id]

        return jsonify(response)
    
    elif request.method == 'PUT':
        # pegar apenas o status
        # não modificará mais nenhuma valor, apenas o status
        status = request.json.get('status')

        tarefas[id]['status'] = status

        return jsonify({'status':'sucesso', 'mensagem':'Status alterado'})

    
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Tarefa excluida com sucesso'})


if __name__ == '__main__':
    app.run(debug=True)