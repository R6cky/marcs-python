from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud_alunos, crud_cursos, crud_matriculas, schemas, models
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
#CRUD Alunos
@app.post("/alunos")
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    return crud_alunos.criar_aluno(db, aluno)

@app.get("/alunos")
def listar_alunos(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(models.Aluno)
    return query.offset((page - 1) * limit).limit(limit).all()

@app.get("/alunos/{aluno_id}")
def buscar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = crud_alunos.buscar_aluno(db, aluno_id)
    
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return aluno
  
@app.put("/alunos/{aluno_id}")
def atualizar_aluno(aluno_id: int, aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    aluno_atualizado = crud_alunos.atualizar_aluno(db, aluno_id, aluno)


    if not aluno_atualizado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return aluno_atualizado
  
  
  
  
@app.delete("/alunos/{aluno_id}")
def deletar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = crud_alunos.deletar_aluno(db, aluno_id)
    
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado") 
   
    return {"mensagem": "Aluno deletado com sucesso"}




#CRUD Cursos
@app.post("/cursos")
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    return crud_cursos.criar_curso(db, curso)

@app.get("/cursos")
def listar_cursos(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(models.Curso)
    return query.offset((page - 1) * limit).limit(limit).all()

@app.get("/cursos/{curso_id}")
def buscar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = crud_cursos.buscar_curso(db, curso_id)

    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    return curso

@app.put("/cursos/{curso_id}")
def atualizar_curso(curso_id: int, curso: schemas.CursoUpdate, db: Session = Depends(get_db)):
    curso_atualizado = crud_cursos.atualizar_curso(db, curso_id, curso)

    if not curso_atualizado:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    return curso_atualizado
  
@app.delete("/cursos/{curso_id}")
def deletar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()

    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    db.delete(curso)
    db.commit()

    return {"mensagem": "Curso deletado"}



#MATRICULA
@app.post("/matriculas")
def matricular(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    return crud_matriculas.matricular_aluno(db, matricula)


@app.get("/alunos/{aluno_id}/cursos")
def cursos_do_aluno(aluno_id: int, db: Session = Depends(get_db)):
     return crud_matriculas.cursos_do_aluno(db, aluno_id)



@app.get("/cursos/{curso_id}/alunos")
def alunos_do_curso(curso_id: int, db: Session = Depends(get_db)):
     return crud_matriculas.alunos_do_curso(db, curso_id)


# CANCELAR MATRÍCULA
@app.put("/matriculas/{matricula_id}/cancelar")
def cancelar(matricula_id: int, db: Session = Depends(get_db)):
    return crud_matriculas.cancelar_matricula(db, matricula_id)


# CONCLUIR CURSO
@app.put("/matriculas/{matricula_id}/concluir")
def concluir(matricula_id: int, db: Session = Depends(get_db)):
    return crud_matriculas.concluir_curso(db, matricula_id)