
from flask import Flask, request, render_template
import json, requests, base64, os

app = Flask(__name__)

REPO = "kelissonvidal/painel-empresa"
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_config():
    url = f"https://api.github.com/repos/{REPO}/contents/config.json"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        content = r.json().get("content", "")
        return json.loads(base64.b64decode(content).decode()), r.json().get("sha", "")
    return {}, None

@app.route("/")
@app.route("/login")
def login():
    dados, _ = get_config()
    return render_template("form.html", dados=dados)

@app.route("/salvar", methods=["POST"])
def salvar():
    novo = {
        "saudacao": request.form["saudacao"],
        "coleta_nome": request.form["coleta_nome"],
        "resposta_nome": request.form["resposta_nome"],
        "pergunta_interesse": request.form["pergunta_interesse"],
        "pergunta_pagamento": request.form["pergunta_pagamento"],
        "pergunta_forma": request.form["pergunta_forma"],
        "pergunta_info": request.form["pergunta_info"],
        "encerramento": request.form["encerramento"]
    }
    content = base64.b64encode(json.dumps(novo, ensure_ascii=False, indent=2).encode()).decode()
    _, sha = get_config()
    payload = {
        "message": "update config.json via painel-chatflow",
        "content": content,
        "branch": "main"
    }
    if sha:
        payload["sha"] = sha
    url = f"https://api.github.com/repos/{REPO}/contents/config.json"
    res = requests.put(url, headers=HEADERS, json=payload)
    if res.status_code in [200, 201]:
        return "<h3>✅ Configuração atualizada no GitHub! <a href='/login'>Voltar</a></h3>"
    else:
        return f"<h3>❌ Erro ao salvar: {res.status_code}<br>{res.text}</h3>"
