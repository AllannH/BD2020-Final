from service.connectDB import getDB
import json


def create_aluno(matricula, nome, cpf, nasc):
    conn = getDB()
    cur = conn.cursor()

    cur.execute("INSERT INTO aluno(matricula, nome, cpf, nasc) "
                f"VALUES ({matricula}, '{nome}', {cpf}, {nasc})")
    conn.commit()
    conn.close()
    return get_aluno_by_id(matricula)


def get_all_aluno():
    conn = getDB()
    cur = conn.cursor()

    cur.execute("SELECT * FROM aluno")

    obj = []
    for matricula, nome, cpf, nasc in cur:
        obj.append({
            "matricula": matricula,
            "nome": nome,
            "cpf": cpf,
            "nasc": str(nasc)
        })

    conn.close()
    return json.dumps(obj)


def get_aluno_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM aluno WHERE matricula={id}")

    obj = []
    for matricula, nome, cpf, nasc in cur:
        obj.append({
            "matricula": matricula,
            "nome": nome,
            "cpf": cpf,
            "nasc": str(nasc)
        })

    conn.close()
    return json.dumps(obj)


def delete_aluno_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM aluno WHERE matricula = {id}")
        conn.commit()
        conn.close()
        return (f"Aluno de ID - {id}, deletado com sucesso!")
    except Exception:
        conn.close()
        return (f"Erro ao deletar o Aluno de ID - {id}")


def edit_aluno_by_id(id, atr, new):
    conn = getDB()
    cur = conn.cursor()
    cur.execute(f"UPDATE aluno SET {atr} = '{new}' WHERE matricula = {id}")
    conn.commit()

    conn.close()
    if atr == 'matricula':
        return get_aluno_by_id(new)
    else:
        return get_aluno_by_id(id)


def get_everything_aluno_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    query = (f"""SELECT DISTINCT aluno.matricula,
				aluno.nome, 
				aluno.cpf, 
				aluno.nasc, 
				palestras.cod,
				palestras.titulo,
				disciplina.nome, 
				disciplina.cod 
                FROM
                    aluno, palestras, inscritos, matriculas, disciplina 
                    WHERE aluno.matricula= {id} 
                    AND matriculas.aluno= {id}  
                    AND palestras.cod = inscritos.palestra 
                    AND disciplina.cod = matriculas.disciplina 
                    AND aluno.matricula = inscritos.aluno;""")

    cur.execute(query)

    obj = {
        "Aluno": [],
        "Palestras": [],
        "Disciplinas": []
    }
    Aluno = []
    palestrasV = []
    disciplinasV = []

    for matricula, nome, cpf, nascimento, codigoP, titulo, nomeD, codigoD in cur:
        if matricula not in Aluno:
            obj["Aluno"].append({
                "matricula": matricula,
                "Nome": nome,
                "cpf": cpf,
                "nascimento": nascimento
            })
            Aluno.append(matricula)
        if codigoP not in palestrasV:
            obj["Palestras"].append({
                "Codigo": codigoP,
                "titulo": titulo
            })
            palestrasV.append(codigoP)

        if codigoD not in disciplinasV:
            obj["Disciplinas"].append({
                "codigo": codigoD,
                "nome": nomeD
            })
            disciplinasV.append(codigoD)
    return obj
