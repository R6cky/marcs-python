from pydantic import BaseModel, EmailStr

# -------- ALUNO --------

class AlunoBase(BaseModel):
    nome: str
    email: EmailStr


class AlunoCreate(AlunoBase):
    pass


class AlunoOut(AlunoBase):
    id: int

    class Config:
        from_attributes = True
    
# -------- CURSO --------
    
        
class CursoBase(BaseModel):
    nome: str
    descricao: str


class CursoCreate(CursoBase):
    pass


class CursoUpdate(CursoBase):
    pass


class Curso(CursoBase):
    id: int

    class Config:
        from_attributes = True        
        
 
 # -------- MATRÍCULA --------
       
class MatriculaBase(BaseModel):
    aluno_id: int
    curso_id: int


class MatriculaCreate(BaseModel):
    aluno_id: int
    curso_id: int


class MatriculaOut(BaseModel):
    id: int
    status: str

    class Config:
        from_attributes = True
#Isso define como os dados chegam na API