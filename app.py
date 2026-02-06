from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens=[
        {'id':1, 'nome':'Celular','cod_barra':'2311516','preco':1200},
        {'id':1, 'nome':'Celular','cod_barra':'2311516','preco':1200},
        {'id':1, 'nome':'Celular','cod_barra':'2311516','preco':1200}
    ]

    return render_template("produtos.html",itens=itens)