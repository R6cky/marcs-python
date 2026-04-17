Perfeito — organizei e formatei tudo corretamente em **Markdown profissional para GitHub** 👇

---

```markdown
# 📚 Backend Project - API Escola

Sistema de cadastro e gerenciamento de **alunos, cursos e matrículas**, desenvolvido com **FastAPI + SQLAlchemy**.

---

## 🚀 Funcionalidades

### 👨‍🎓 Alunos
- Criar aluno  
- Listar alunos  
- Buscar aluno por ID  
- Atualizar aluno  
- Deletar aluno  

---

### 📖 Cursos
- Criar curso  
- Listar cursos  
- Buscar curso por ID  
- Atualizar curso  
- Deletar curso  

---

### 📝 Matrículas
- Matricular aluno em curso  
- Listar cursos de um aluno  
- Listar alunos de um curso  
- Cancelar matrícula  
- Concluir curso  

---

## ⚙️ Regras de Negócio

### 📌 Matrículas
- ❌ Um aluno **não pode se matricular duas vezes** no mesmo curso  
- ❌ Não permite matrícula de:
  - aluno inexistente  
  - curso inexistente  
- ⚠️ Um aluno pode ter no máximo **5 matrículas ativas**  

---

### 📌 Validação de Dados
- Email do aluno deve ser **único**  
- Campos obrigatórios:
  - nome (aluno)  
  - email (aluno)  
  - título (curso)  
- ❌ Não permite valores vazios ou inválidos  

---

### 📌 Status da Matrícula

Cada matrícula possui um status:

- `ativa`  
- `cancelada`  
- `concluida`  

---

## 📡 Endpoints Principais

### 🔹 Alunos
```

POST   /alunos
GET    /alunos
GET    /alunos/{id}
PUT    /alunos/{id}
DELETE /alunos/{id}

```

### 🔹 Cursos
```

POST   /cursos
GET    /cursos
GET    /cursos/{id}
PUT    /cursos/{id}
DELETE /cursos/{id}

```

### 🔹 Matrículas
```

POST   /matriculas
GET    /alunos/{id}/cursos
GET    /cursos/{id}/alunos
PUT    /matriculas/{id}/cancelar
PUT    /matriculas/{id}/concluir

```

---

## 📄 Paginação

Alguns endpoints suportam paginação:

```

GET /alunos?page=1&limit=10
GET /cursos?page=1&limit=10

````

---

## ❗ Tratamento de Erros

A API retorna erros padronizados:

```json
{
  "error": "Mensagem descritiva",
  "statusCode": 400
}
````

### Códigos:

* `400` → Requisição inválida
* `404` → Recurso não encontrado
* `500` → Erro interno

---

## 🛠️ Tecnologias Utilizadas

* Python 3.12
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <seu-repositorio>
cd api_escola
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install fastapi uvicorn sqlalchemy pydantic[email]
```

### 3. Rodar o servidor

```bash
python -m uvicorn main:app --reload
```

### 4. Acessar no navegador

* API:

```
http://127.0.0.1:8000
```

* Documentação interativa (Swagger):

```
http://127.0.0.1:8000/docs
```

---

## 📂 Estrutura do Projeto

```
api_escola/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── crud_alunos.py
├── crud_cursos.py
├── crud_matriculas.py
│
└── README.md
```

---

## 💡 Melhorias Futuras

* 🔐 Autenticação com JWT
* 👤 Controle de usuários
* 📊 Dashboard
* 🐳 Dockerização
* ☁️ Deploy em nuvem

---

## 👨‍💻 Autor

**Marcos Vinicius Sousa Ferreira**

Projeto desenvolvido para prática de backend com FastAPI 🚀
