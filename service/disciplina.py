from service.connectDB import getDB
import json


def create_disciplina(cod, nome, dpto, prof):
    conn = getDB()
    cur = conn.cursor()

    cur.execute("INSERT INTO disciplina(cod, nome, dpto, prof)"
                f" VALUES ({cod}, '{nome}', {dpto}, {prof})")
    conn.commit()
    conn.close()
    return get_disciplina_by_id(cod)


def get_all_disciplina():
    conn = getDB()
    cur = conn.cursor()

    cur.execute("SELECT * FROM disciplina")

    obj = []
    for cod, nome, dpto, prof in cur:
        obj.append({
            "cod": cod,
            "nome": nome,
            "dpto": dpto,
            "prof": prof
        })

    conn.close()
    return json.dumps(obj)


def get_disciplina_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM disciplina WHERE cod={id}")

    obj = []

    for cod, nome, dpto, prof in cur:
        obj.append({
            "cod": cod,
            "nome": nome,
            "dpto": dpto,
            "prof": prof
        })

    conn.close()
    return json.dumps(obj)


def delete_disciplina_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM disciplina WHERE cod = {id}")
        conn.commit()
        conn.close()
        return (f"Disciplina de ID - {id}, deletado com sucesso!")
    except Exception:
        conn.close()
        return (f"Erro ao deletar a Disciplina de ID - {id}")


def edit_disciplina_by_id(id, atr, new):
    conn = getDB()
    cur = conn.cursor()
    cur.execute(f"UPDATE disciplina SET {atr} = '{new}' WHERE cod = {id}")
    conn.commit()

    conn.close()
    if atr == 'cod':
        return get_disciplina_by_id(new)
    else:
        return get_disciplina_by_id(id)


def get_material_disciplina_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(f"""SELECT nome, material_biblio.titulo, material_video.titulo from disciplina, material_biblio, material_video, encontros
                WHERE material_biblio.disciplina = {id} AND disciplina.cod = {id} AND encontros.disciplina = {id} AND material_video.cod = encontros.video;""")



    materia = []
    Texto = []
    Video = []

    obj = {
        "Disciplina": [],
        "Livro texto": [],
        "Videos": []
    }

    for disciplina, texto, video in cur:
        if disciplina not in materia:
            obj["Disciplina"].append({
                "Disciplina": disciplina
            })
            materia.append(disciplina)

        if texto not in Texto:
            obj["Livro texto"].append({
                "Livro texto": texto
            })
            Texto.append(texto)

        if video not in Video:
            obj["Videos"].append({
                "Videos": video
            })
            Video.append(video)

    conn.close()
    return obj
