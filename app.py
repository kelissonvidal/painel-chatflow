
from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/login", methods=["GET"])
def login():
    return render_template("form.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    dados = {
        "saudacao": request.form["saudacao"],
        "coleta_nome": request.form["coleta_nome"],
        "resposta_nome": request.form["resposta_nome"],
        "pergunta_interesse": request.form["pergunta_interesse"],
        "pergunta_pagamento": request.form["pergunta_pagamento"],
        "pergunta_forma": request.form["pergunta_forma"],
        "pergunta_info": request.form["pergunta_info"],
        "encerramento": request.form["encerramento"]
    }
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    return "✅ Configuração salva com sucesso!"
