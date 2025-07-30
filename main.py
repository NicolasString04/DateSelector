from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Inicializa o Firebase
cred = credentials.Certificate('credenciais.json')  # ajuste o caminho se necessário
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/')
def index():
    return render_template('date.html')

@app.route('/salvar_encontro', methods=['POST'])
def salvar_encontro():
    local = request.form.get('local')
    data = request.form.get('data')
    hora = request.form.get('hora')

    doc_ref = db.collection('encontros').document()
    doc_ref.set({
        'local': local,
        'data': data,
        'hora': hora
    })

    return redirect(url_for('flor'))

@app.route('/flor')
def flor():
    return render_template('flor.html')

if __name__ == '__main__':
    app.run(debug=True)
