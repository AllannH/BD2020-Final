from service.connectDB import getDB
import json


def create_professor(cod, cpf, nome, dpto):
    conn = getDB()
    cur = conn.cursor()

    cur.execute("INSERT INTO professor(cod, cpf, nome, lattes, dpto)"
                f" VALUES ({cod}, {cpf}, '{nome}', "
                f"'http://lattes.cnpq.br/{nome}', {dpto})")
    conn.commit()
    conn.close()
    return get_professor_by_id(cod)


def get_all_professor():
    conn = getDB()
    cur = conn.cursor()

    cur.execute("SELECT * FROM professor")

    obj = []
    for cod, cpf, nome, lattes, dpto in cur:
        obj.append({
            "cod": cod,
            "cpf": cpf,
            "nome": nome,
            "lattes": lattes,
            "dpto": dpto
        })

    conn.close()
    return json.dumps(obj)


def get_professor_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM professor WHERE cod={id}")

    obj = []

    for cod, cpf, nome, lattes, dpto in cur:
        obj.append({
            "cod": cod,
            "cpf": cpf,
            "nome": nome,
            "lattes": lattes,
            "dpto": dpto
        })

    conn.close()
    return json.dumps(obj)


def delete_professor_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM professor WHERE cod = {id}")
        conn.commit()
        conn.close()
        return (f"Professor de ID - {id}, deletado com sucesso!")
    except Exception:
        conn.close()
        return (f"Erro ao deletar a Professor de ID - {id}")


def edit_professor_by_id(id, atr, new):
    conn = getDB()
    cur = conn.cursor()
    cur.execute(f"UPDATE professor SET {atr} = '{new}' WHERE cod = {id}")
    conn.commit()

    conn.close()
    if atr == 'cod':
        return get_professor_by_id(new)
    else:
        return get_professor_by_id(id)
