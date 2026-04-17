from sqlalchemy.orm import Session
from sqlalchemy import desc
import models, schemas

def criar_curso(db: Session, curso: schemas.CursoCreate):
    db_curso = models.Curso(**curso.model_dump())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso


def listar_cursos(db: Session, page: int = 1, limit: int = 10):
    query = db.query(models.Curso)
    query = query.order_by(desc(models.Curso.id))
    return query.offset((page - 1) * limit).limit(limit).all()

#buscar curso por ID
def buscar_curso(db: Session, curso_id: int):
    return db.query(models.Curso).filter(models.Curso.id == curso_id).first()

#Atualizar curso
def atualizar_curso(db: Session, curso_id: int, curso: schemas.CursoUpdate):
    db_curso = buscar_curso(db, curso_id)

    if db_curso:
        db_curso.nome = curso.nome
        db_curso.descricao = curso.descricao
        db.commit()
        db.refresh(db_curso)

    return db_curso

#Deletar curso
def deletar_curso(db: Session, curso_id: int):
    db_curso = buscar_curso(db, curso_id)

    if db_curso:
        db.delete(db_curso)
        db.commit()
    
    return db_curso



#Listar cursos de aluno
def cursos_do_aluno(db: Session, aluno_id: int):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    return aluno.cursos if aluno else []    

 #Listar alunos de um curso   
def alunos_do_curso(db: Session, curso_id: int):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    return curso.alunos if curso else []

#Operação 	Função
#Create =	criar_curso
#Read =	  listar_cursos
#Create =	criar_aluno
#Read =	  listar_alunos