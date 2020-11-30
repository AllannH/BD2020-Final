from service.connectDB import getDB
import json


def create_departamento(cod, nome, instituicao):
    conn = getDB()
    cur = conn.cursor()

    cur.execute("INSERT INTO departamento(cod, nome, instituicao)"
                f" VALUES ({cod}, '{nome}', instituicao)")
    conn.commit()
    conn.close()
    return get_departamento_by_id(cod)


def get_all_departamento():
    conn = getDB()
    cur = conn.cursor()

    cur.execute("SELECT * FROM departamento")

    obj = []

    for cnpj, nome, instituicao in cur:
        obj.append({
            "cnpj": cnpj,
            "nome": nome,
            "instituicao": instituicao
        })

    conn.close()
    return json.dumps(obj)


def get_departamento_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM departamento WHERE cod={id}")

    obj = []

    for cnpj, nome, instituicao in cur:
        obj.append({
            "cnpj": cnpj,
            "nome": nome,
            "instituicao": instituicao
        })

    conn.close()
    return json.dumps(obj)


def delete_departamento_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    try:
        
        cur.execute(f"DELETE FROM departamento WHERE cod = {id}")
        conn.commit()
        conn.close()
        return (f"Departamento de ID - {id}, deletado com sucesso!")
    except Exception:
        conn.close()
        return (f"Erro ao deletar a Departamento de ID - {id}")


def edit_departamento_by_id(id, atr, new):
    conn = getDB()
    cur = conn.cursor()
    cur.execute(f"UPDATE departamento SET {atr} = '{new}' WHERE cod = {id}")
    conn.commit()

    conn.close()
    if atr == 'cod':
        return get_departamento_by_id(new)
    else:
        return get_departamento_by_id(id)


def get_every_from_departamento():
    conn = getDB()
    cur = conn.cursor()
    cur.execute("""SELECT departamento.nome, disciplina.nome, professor.nome from departamento, disciplina, professor
                    WHERE professor.dpto = departamento.cod AND disciplina.prof = professor.cod AND departamento.cod = disciplina.dpto""")

    obj = []

    for dpto, disc, prof in cur:
        obj.append({
            "Departamento": dpto,
            "Disciplina": disc,
            "Professor": prof
        })

    conn.close()

    return json.dumps(obj)