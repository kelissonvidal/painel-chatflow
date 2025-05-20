
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("form.html")

@app.route("/audios")
def audios():
    return "<h2>🔊 Gerenciar Áudios - em breve</h2>"

@app.route("/ver_logs")
def logs():
    return "<h2>📝 Logs de interações - em breve</h2>"

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
