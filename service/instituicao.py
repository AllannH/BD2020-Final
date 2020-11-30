from service.connectDB import getDB
import json


def create_instituicao(cnpj, nome):
    conn = getDB()
    cur = conn.cursor()

    cur.execute("INSERT INTO instituicao(cnpj, nome)"
                f" VALUES ({cnpj}, '{nome}')")
    conn.commit()
    conn.close()
    return get_instituicao_by_id(cnpj)


def get_all_instituicao():
    conn = getDB()
    cur = conn.cursor()

    cur.execute("SELECT * FROM instituicao")

    obj = []

    for cnpj, nome in cur:
        obj.append({
            "cnpj": cnpj,
            "nome": nome
        })

    conn.close()
    return json.dumps(obj)


def get_instituicao_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM instituicao WHERE cnpj={id}")

    obj = []

    for cnpj, nome in cur:
        obj.append({
            "cnpj": cnpj,
            "nome": nome
        })

    conn.close()
    return json.dumps(obj)


def delete_instituicao_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM instituicao WHERE cnpj = {id}")
        conn.commit()
        conn.close()
        return (f"Instituição de ID - {id}, deletado com sucesso!")
    except Exception:
        conn.close()
        return (f"Erro ao deletar a Instituição de ID - {id}")


def edit_instituicao_by_id(id, atr, new):
    conn = getDB()
    cur = conn.cursor()
    cur.execute(f"UPDATE instituicao SET {atr} = '{new}' WHERE cnpj = {id}")
    conn.commit()

    conn.close()
    if atr == 'cnpj':
        return get_instituicao_by_id(new)
    else:
        return get_instituicao_by_id(id)


def get_everything_instituicao_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(
        f"SELECT instituicao.nome, departamento.nome, disciplina.nome FROM instituicao, departamento, disciplina WHERE cnpj={id} AND disciplina.dpto = departamento.cod")

    obj = []

    for inst, dpto, disc in cur:
        obj.append(
            {
                "Instituicao": inst,
                "Departamento": dpto,
                "Disciplina": disc
            }
        )

    conn.close()

    return json.dumps(obj)
