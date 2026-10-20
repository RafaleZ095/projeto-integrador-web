from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'unisa_projeto_integrador_2024'

def get_db_connection():
    conn = sqlite3.connect('contas.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/')
def index():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    contas = conn.execute('SELECT * FROM contas ORDER BY data_vencimento ASC').fetchall()
    conn.close()
    
    # Passando a data atual para o HTML verificar se está vencida
    hoje = datetime.now().strftime('%Y-%m-%d')
    return render_template('dashboard.html', contas=contas, hoje=hoje)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['senha'], senha):
            session['usuario_id'] = user['id']
            session['usuario_nome'] = user['nome']
            return redirect(url_for('index'))
        else:
            flash('E-mail ou senha incorretos!', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/nova_conta', methods=['POST'])
def nova_conta():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    descricao = request.form['descricao']
    fornecedor = request.form['fornecedor']
    valor = request.form['valor']
    data_vencimento = request.form['data_vencimento']

    # REGRA DE NEGÓCIO: Validação no Back-end
    if not descricao or float(valor) <= 0:
        flash('Erro: O valor deve ser maior que zero e a descrição é obrigatória.', 'danger')
        return redirect(url_for('index'))

    conn = get_db_connection()
    conn.execute('INSERT INTO contas (descricao, fornecedor, valor, data_vencimento, usuario_id) VALUES (?, ?, ?, ?, ?)',
                 (descricao, fornecedor, valor, data_vencimento, session['usuario_id']))
    conn.commit()
    conn.close()
    
    flash('Conta cadastrada com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/pagar/<int:id>', methods=['POST'])
def pagar_conta(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    conta = conn.execute('SELECT status FROM contas WHERE id = ?', (id,)).fetchone()
    
    # REGRA DE NEGÓCIO: Não permitir pagar conta já paga
    if conta['status'] == 'PAGA':
        flash('Erro: Esta conta já foi paga!', 'danger')
    else:
        data_hoje = datetime.now().strftime('%Y-%m-%d')
        conn.execute('UPDATE contas SET status = "PAGA", data_pagamento = ? WHERE id = ?', (data_hoje, id))
        conn.commit()
        flash('Conta paga com sucesso!', 'success')
        
    conn.close()
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir_conta(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    conn.execute('DELETE FROM contas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Conta excluída com sucesso!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)