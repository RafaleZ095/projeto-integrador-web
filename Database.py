import sqlite3
from werkzeug.security import generate_password_hash

def init_db():
    conn = sqlite3.connect('contas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            fornecedor TEXT NOT NULL,
            valor REAL NOT NULL,
            data_vencimento DATE NOT NULL,
            status TEXT DEFAULT 'PENDENTE',
            data_pagamento DATE,
            usuario_id INTEGER,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )
    ''')

    senha_hash = generate_password_hash('123456')
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", 
                       ('Admin UNISA', 'admin@unisa.com', senha_hash))
        
        # Populando com contas de exemplo (Uma vencida, uma a vencer)
        cursor.execute("INSERT INTO contas (descricao, fornecedor, valor, data_vencimento, usuario_id) VALUES (?, ?, ?, ?, ?)",
                       ('Servidor AWS', 'Amazon', 450.00, '2023-10-01', 1))
        cursor.execute("INSERT INTO contas (descricao, fornecedor, valor, data_vencimento, usuario_id) VALUES (?, ?, ?, ?, ?)",
                       ('Licença Office', 'Microsoft', 120.50, '2026-12-15', 1))
    except sqlite3.IntegrityError:
        pass

    conn.commit()
    conn.close()
    print("Banco de dados criado e populado com sucesso!")

if __name__ == '__main__':
    init_db()