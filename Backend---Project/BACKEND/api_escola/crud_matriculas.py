from sqlalchemy.orm import Session
import models

def matricular_aluno(db: Session, dados):
    # Verificar aluno
    aluno = db.query(models.Aluno).filter(models.Aluno.id == dados.aluno_id).first()
    if not aluno:
        return {"error": "Aluno não encontrado", "statusCode": 404}

    # Verificar curso
    curso = db.query(models.Curso).filter(models.Curso.id == dados.curso_id).first()
    if not curso:
        return {"error": "Curso não encontrado", "statusCode": 404}

    # Verificar duplicidade
    existente = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == dados.aluno_id,
        models.Matricula.curso_id == dados.curso_id
    ).first()

    if existente:
        return {"error": "Aluno já matriculado neste curso", "statusCode": 400}

    # Limite de 5 matrículas
    total = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == dados.aluno_id,
        models.Matricula.status == "ativa"
    ).count()

    if total > 5:
        return {"error": "Limite de 5 matrículas atingido", "statusCode": 400}

    nova = models.Matricula(
        aluno_id=dados.aluno_id,
        curso_id=dados.curso_id
    )

    db.add(nova)
    db.commit()
    db.refresh(nova)

    return nova


def cursos_do_aluno(db: Session, aluno_id: int):
    return db.query(models.Matricula).filter(models.Matricula.aluno_id == aluno_id).all()


def alunos_do_curso(db: Session, curso_id: int):
    return db.query(models.Matricula).filter(models.Matricula.curso_id == curso_id).all()


def cancelar_matricula(db: Session, matricula_id: int):
    matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()

    if not matricula:
        return {"error": "Matrícula não encontrada", "statusCode": 404}

    matricula.status = "cancelada"
    db.commit()
    return matricula


def concluir_curso(db: Session, matricula_id: int):
    matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()

    if not matricula:
        return {"error": "Matrícula não encontrada", "statusCode": 404}

    matricula.status = "concluida"
    db.commit()
    return matricula