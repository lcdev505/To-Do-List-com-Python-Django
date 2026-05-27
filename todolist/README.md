# 📝 To-Do List com Django

Aplicação web completa de gerenciamento de tarefas desenvolvida com Python e Django, com autenticação de usuários, containerização com Docker e deploy em produção no Railway.

🔗 **[Demo ao vivo](https://to-do-list-com-python-django-production.up.railway.app/core/home/)**

---

## ✨ Funcionalidades

- **CRUD completo** — criar, listar, editar e excluir tarefas
- **Toggle de status** — marcar tarefas como concluídas ou pendentes
- **Autenticação de usuários** — cadastro, login e logout
- **Isolamento de dados** — cada usuário visualiza apenas suas próprias tarefas
- **Testes de integração** — cobertura completa do CRUD com Django TestCase

---

## 🛠️ Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.13 |
| Framework | Django 6 |
| Banco de Dados | PostgreSQL 15 |
| Containerização | Docker + Docker Compose |
| Servidor de Produção | Gunicorn |
| Arquivos Estáticos | WhiteNoise |
| Deploy | Railway |

---

## 🏗️ Arquitetura

O projeto segue o padrão **MTV** (Model-Template-View) do Django:

```
core/
├── models.py        # TaskModel com ForeignKey para User
├── views.py         # CRUD + autenticação (login, register, logout)
├── forms.py         # TaskForm (ModelForm)
├── urls.py          # Rotas do app
├── tests.py         # Testes de integração
└── static/css/      # Estilos separados por página
templates/
├── home.html        # Listagem de tarefas
├── form.html        # Formulário de criação/edição
├── login.html       # Página de login
└── register.html    # Página de cadastro
```

---

## 🚀 Como rodar localmente

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/lcdev505/To-Do-List-com-Python-Django.git
cd To-Do-List-com-Python-Django
```

2. Crie o arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=sua_secret_key_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://root:senha@postgres:5432/postgres_db
DB_NAME=postgres_db
DB_USER=root
DB_PASSWORD=sua_senha
DB_HOST=postgres
DB_PORT=5432
```

3. Suba os containers:
```bash
docker compose up --build
```

4. Acesse em: [http://localhost:8000/core/home/](http://localhost:8000/core/home/)

---

## 🧪 Testes

Para rodar os testes de integração:

```bash
docker compose exec web python manage.py test
```

Os testes cobrem todas as operações do CRUD:

- `criarTarefaTest` — verifica criação e persistência no banco
- `ListarTarefaTest` — verifica listagem no contexto do template
- `EditarTarefaTest` — verifica atualização de dados
- `DeletarTarefaTest` — verifica remoção do registro

---

## 📁 Variáveis de Ambiente

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | Modo debug (`True` local, `False` produção) |
| `ALLOWED_HOSTS` | Hosts permitidos separados por vírgula |
| `DATABASE_URL` | URL de conexão com o PostgreSQL |

---

## 📄 Licença

Este projeto está sob a licença MIT.