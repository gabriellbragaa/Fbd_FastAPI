## são os modelos do python
## mapear tal qual o banco de dados


from pydantic import BaseModel
from typing import Optional
from datetime import date


## tem que ser exatamente igual ao banco de dados
## se tiver um campo a mais, não vai funcionar
class Departamento(BaseModel):
    id: int
    name: str
    email: str
    cpf_gerente: Optional[str] = None
    data_inicio_gerente: Optional[date] = None
    created_at: date

## so pra atualizar o departamento
class DepartamentoUpdate(BaseModel):
    name: str
    email: str
    cpf_gerente: Optional[str] = None
    data_inicio_gerente: Optional[date] = None

class Funcionario(BaseModel):
    id: int
    name: str
    email: str
    cpf: str
    data_nascimento: date
    data_admissao: date
    salario: float
    departamento_id: int
    created_at: date

## so pra atualizar o funcionario
## não pode ter o id, porque ele não vai atualizar o id
## não vai ter o cpf pq é chave primária
class FuncionarioUpdate(BaseModel):
    name: str
    email: str
    data_nascimento: date
    data_admissao: date
    salario: float
    departamento_id: int

class localidadeDep(BaseModel):
    dnum: int
    dlocal: str

class projeto(BaseModel):
    projname: str
    projdescricao: str
    data_inicio: date
    data_fim: Optional[date] = None ## opcional de data inicialmente vazio

