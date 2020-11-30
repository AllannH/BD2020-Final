from service.connectDB import getDB
import json


def create_palestra(cod, titulo, datahora, prof, video):
    conn = getDB()
    cur = conn.cursor()

    cur.execute("INSERT INTO palestras"
                "(cod, titulo, datahora, prof, video) VALUES "
                f"({cod}, '{titulo}', '{datahora}', {prof}, {video})")
    conn.commit()
    conn.close()
    return get_palestra_by_id(cod)


def get_all_palestra():
    conn = getDB()
    cur = conn.cursor()

    cur.execute("SELECT * FROM palestras")

    obj = []
    for cod, titulo, datahora, prof, video in cur:
        obj.append({
            "cod": cod,
            "titulo": titulo,
            "datahora": str(datahora),
            "prof": prof,
            "video": video
        })

    conn.close()
    return json.dumps(obj)


def get_palestra_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM palestras WHERE cod={id}")

    obj = []

    for cod, titulo, datahora, prof, video in cur:
        obj.append({
            "cod": cod,
            "titulo": titulo,
            "datahora": str(datahora),
            "prof": prof,
            "video": video
        })

    conn.close()
    return json.dumps(obj)


def delete_palestra_by_id(id):
    conn = getDB()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM palestras WHERE cod = {id}")
        conn.commit()
        conn.close()
        return (f"Palestras de ID - {id}, deletado com sucesso!")
    except Exception:
        conn.close()
        return (f"Erro ao deletar a Palestras de ID - {id}")


def edit_palestra_by_id(id, atr, new):
    conn = getDB()
    cur = conn.cursor()
    cur.execute(f"UPDATE palestras SET {atr} = '{new}' WHERE cod = {id}")
    conn.commit()

    conn.close()
    if atr == 'cod':
        return get_palestra_by_id(new)
    else:
        return get_palestra_by_id(id)

def get_next_palestra():
    conn = getDB()
    cur = conn.cursor()
    cur.execute("SELECT * FROM GetPalestras;")
    obj = []

    for titulo, datahora, nome, palestra, descricao, link in cur:
        obj.append({
            "titulo": titulo,
            "datahora": str(datahora),
            "nome": nome,
            "palestra": palestra,
            "descricao": descricao,
            "link": link
        })

    conn.close()

    return json.dumps(obj)


# SELECT PALESTRAS.titulo, PALESTRAS.datahora, PROFESSOR.nome, VID.titulo AS palestra, VID.descricao, VID.link FROM PALESTRAS
# JOIN PROFESSOR ON PROFESSOR.cod = PALESTRAS.prof
# JOIN MATERIAL_VIDEO AS VID ON VID.cod = PALESTRAS.video
# WHERE PALESTRAS.datahora > CURDATE() AND PALESTRAS.datahora < CURDATE() + INTERVAL 30 DAY;

def insert_into_palestra(palestra,aluno):
    conn = getDB()
    cur = conn.cursor()
    try:
        cur.execute(f"CALL INSCRICAO ({palestra},{aluno})")
        conn.commit()
        conn.close()
        return f"Aluno: {aluno}, adicionado na palestra"
    except:
        return "Ocorreu um erro"

# DELIMITER $$
# CREATE PROCEDURE INSCRICAO (IN cod VARCHAR(25), IN matricula VARCHAR(25))
# BEGIN
# 	IF (SELECT COUNT(ALUNO) from INSCRITOS WHERE PALESTRA = cod) < 50 THEN
# 		INSERT INTO INSCRITOS (palestra, aluno) VALUES (cod, matricula);
# 	END IF;
# END $$
# DELIMITER ;