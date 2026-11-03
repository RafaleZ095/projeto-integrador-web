Quase perfeito! A estrutura do seu README está ótima, mas ele veio com dois problemas por causa da conversão:
1. **O link do GitHub foi bloqueado** (apareceu `[suspicious link removed]`).
2. **O texto cortou no final** (parou no comando `cd projeto-integrador-we`).
3. **A formatação das listas ficou toda na mesma linha** (o que deixa o visual feio no GitHub).

Não se preocupe, eu corrigi tudo para você. **Copie o texto abaixo, apague o conteúdo atual do seu `README.md` no VS Code e cole isso:**

***

```markdown
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
```

### 2. Criar e Ativar o Ambiente Virtual (venv)
No Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```
No Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale o Flask:
```bash
pip install Flask
```

### 4. Inicializar o Banco de Dados
Execute o script para criar as tabelas e popular o banco com dados iniciais:
```bash
python Database.py
```

### 5. Executar a Aplicação
Inicie o servidor Flask:
```bash
python app.py
```

O sistema estará rodando no endereço: **http://localhost:8080** (ou http://127.0.0.1:8080).

---

## 🔑 Credenciais de Teste

Para acessar o painel e testar as regras de negócio, utilize:
* **E-mail:** admin@unisa.com
* **Senha:** 123456

---

## 🧪 Testes e Regras de Negócio
O sistema possui proteções validadas por testes de caixa-preta:
* Bloqueio de login com credenciais inválidas.
* Proteção de rotas (redireciona para o login se não estiver autenticado).
* Bloqueio de cadastro de contas com valor zerado ou negativo.
* **Prevenção de baixa duplicada:** Impede que uma conta já "PAGA" receba baixa novamente.
```

***

### 🚀 O que fazer agora:
1. Salve esse arquivo no VS Code (`Ctrl + S`).
2. Suba ele para o seu repositório no GitHub (pode ser pelo site, clicando em "Add file" > "Upload files").
3. Confira no site do GitHub se as listas e os blocos de código ficaram bonitos e formatados.

Agora seu repositório está **perfeito** para o professor avaliar e rodar o projeto sem erros! Você está liberado para entregar o PDF e o vídeo.
