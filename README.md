README.md

# 💰 Módulo Web de Contas a Pagar (Projeto Integrador - UNISA)

> **Projeto Integrador: Programação WEB**  
> **Curso:** CST em Análise e Desenvolvimento de Sistemas — Universidade Santo Amaro (UNISA)  
> **Autor:** Rafael Mendes dos Santos (RA: 5681570)  
> **Orientador:** Prof. Luis Fernando dos Santos Pires  

---

## 📌 Sobre o Projeto

O **Módulo Web de Contas a Pagar** é uma solução voltada para micro e pequenas empresas, desenvolvida com o objetivo de automatizar a gestão de compromissos financeiros e substituir o uso de planilhas manuais suscetíveis a erros. 

A aplicação adota o padrão arquitetural **MVC (Model-View-Controller)** e oferece controle restrito de acesso por autenticação via sessão HTTP, cadastro e listagem de débitos, registro de baixas com verificação de integridade (prevenção de pagamentos duplicados) e alertas visuais de status.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Microframework Web:** Flask
* **Banco de Dados:** SQLite3 (Relacional)
* **Segurança:** Criptografia de senhas com *hash* (`Werkzeug`) e autenticação baseada em sessão (`Flask Session`)
* **Frontend:** HTML5, CSS3, Jinja2 Templates

---

## ⚙️ Passo a Passo para Execução Local

Siga as instruções abaixo no terminal ou prompt de comando para rodar a aplicação:

### 1. Clonar o Repositório
```bash
git clone https://github.com/RafaleZ095/projeto-integrador-web.git
cd projeto-integrador-web
