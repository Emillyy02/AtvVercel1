from flask import Flask,render_template,request,redirect

class cadsapatos:
    def __init__(self,idsapatos,modelo,marca,categoria,tamanho,cor):
        self.idsapatos = idsapatos
        self.modelo = modelo
        self.marca = marca
        self.categoria = categoria
        self.tamanho = tamanho
        self.cor = cor

lista = []

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Cadastro de Sapatos'

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro de Sapatos')

@app.route('/criar', methods=['POST'])
def criar():
    idsapatos = request.form['ID-Sapatos']
    modelo = request.form['Modelo']
    marca = request.form['Marca']
    categoria = request.form['Categoria']
    tamanho = request.form['Tamanho']
    cor = request.form['Cor']
    obj = cadsapatos(idsapatos,modelo,marca,categoria,tamanho,cor)
    lista.append(obj)
    return redirect('/sapatos')

@app.route('/sapatos')
def sapatos():
    return render_template('Sapatos.html', Titulo='Sapatos',ListaSapatos=lista)

@app.route('/excluir/<IDsap>', methods=['GET', 'DELETE'])
def excluir(IDsap):
    for i, sap in enumerate(lista):
        if sap.idsapatos == IDsap:
            lista.pop(i)
            break
    return redirect('/sapatos')

@app.route('/editar/<IDsap>', methods=['GET'])
def editar(IDsap):
    for i, sap in enumerate(lista):
        if sap.idsapatos == IDsap:
            return render_template('Editar.html', Titulo='Editar Sapatos', Sapatos= sap)

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    id = request.form['ID-Sapatos']
    for i, sap in enumerate(lista):
        if sap.idsapatos == id:
            sap.modelo = request.form['Modelo']
            sap.marca = request.form['Marca']
            sap.categoria = request.form['Categoria']
            sap.tamanho = request.form['Tamanho']
            sap.cor = request.form['Cor']
        return redirect('/sapatos')

if __name__ == '__main__':
    app.run()
