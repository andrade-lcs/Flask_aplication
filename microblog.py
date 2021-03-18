from flask import Flask

app = Flask ("microblog")

@app.route("/")
def index():
    return "Olá, Mundo"

app.run()

#código para rodar o app
#python microblog.py
#ctrl+c para a aplicação