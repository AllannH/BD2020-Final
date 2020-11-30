from flask import Flask

from service.instituicao import (create_instituicao,
                                 get_all_instituicao,
                                 get_instituicao_by_id,
                                 delete_instituicao_by_id,
                                 edit_instituicao_by_id,
                                 get_everything_instituicao_by_id)
from service.departamento import (create_departamento,
                                  get_all_departamento,
                                  get_departamento_by_id,
                                  delete_departamento_by_id,
                                  edit_departamento_by_id,
                                  get_every_from_departamento)
from service.palestra import (create_palestra,
                              get_all_palestra,
                              get_palestra_by_id,
                              delete_palestra_by_id,
                              edit_palestra_by_id,
                              get_next_palestra,
                              insert_into_palestra)
from service.professor import (create_professor,
                               get_all_professor,
                               get_professor_by_id,
                               delete_professor_by_id,
                               edit_professor_by_id)
from service.disciplina import (create_disciplina,
                                get_all_disciplina,
                                get_disciplina_by_id,
                                delete_disciplina_by_id,
                                edit_disciplina_by_id,
                                get_material_disciplina_by_id)
from service.aluno import (create_aluno,
                           get_all_aluno,
                           get_aluno_by_id,
                           delete_aluno_by_id,
                           edit_aluno_by_id,
                           get_everything_aluno_by_id)

app = Flask(__name__)

@app.route("/")
def index():
    return "HOME"

# region OBJ instituicao


@app.route("/instituicao/create/<int:cnpj>&"
           "<string:nome>", methods=["GET"])
def create_inst(cnpj, nome):
    return create_instituicao(cnpj, nome)


@app.route("/instituicao", methods=["GET"])
def get_all_inst():
    return get_all_instituicao()


@app.route("/instituicao/<int:id>", methods=["GET"])
def get_inst_by_id(id):
    return get_instituicao_by_id(id)


@app.route("/instituicao/delete/<int:id>", methods=["GET"])
def delete_inst_by_id(id):
    return delete_instituicao_by_id(id)


@app.route("/instituicao/edit/<int:id>&<string:atr>"
           "&<string:new>", methods=["GET"])
def edit_inst_by_id(id, atr, new):
    return edit_instituicao_by_id(id, atr, new)

@app.route("/instituicao/all/<int:id>", methods=["GET"])
def get_everything_inst_by_id(id):
    return get_everything_instituicao_by_id(id)

# endregion

# region OBJ departamento


@app.route("/departamento/create/<int:cod>&<string:nome>&<string:instituicao>", methods=["GET"])
def create_dept(cod, nome, instituicao):
    return create_departamento(cod, nome, instituicao)


@app.route("/departamento", methods=["GET"])
def get_all_dept():
    return get_all_departamento()


@app.route("/departamento/<int:id>", methods=["GET"])
def get_dept_by_id(id):
    return get_departamento_by_id(id)


@app.route("/departamento/delete/<int:id>", methods=["GET"])
def delete_dept_by_id(id):
    return delete_departamento_by_id(id)


@app.route("/departamento/edit/<int:id>&<string:atr>"
           "&<string:new>", methods=["GET"])
def edit_dept_by_id(id, atr, new):
    return edit_departamento_by_id(id, atr, new)

@app.route("/departamento/todos", methods=["GET"])
def get_every_from_dpto():
    return get_every_from_departamento()

# endregion

# region OBJ palestra


@app.route("/palestra/create/<int:cod>&<string:titulo>&<string:datahora>"
           "&<string:prof>&<string:video>", methods=["GET"])
def create_palest(cod, titulo, datahora, prof, video):
    return create_palestra(cod, titulo, datahora, prof, video)


@app.route("/palestra", methods=["GET"])
def get_all_palest():
    return get_all_palestra()


@app.route("/palestra/<int:id>", methods=["GET"])
def get_palest_by_id(id):
    return get_palestra_by_id(id)


@app.route("/palestra/delete/<int:id>", methods=["GET"])
def delete_palest_by_id(id):
    return delete_palestra_by_id(id)


@app.route("/palestra/edit/<int:id>&<string:atr>"
           "&<string:new>", methods=["GET"])
def edit_palest_by_id(id, atr, new):
    return edit_palestra_by_id(id, atr, new)

@app.route("/palestra/mes", methods=["GET"])
def get_next_palest():
    return get_next_palestra()

@app.route("/palestra/insert/<string:palestra>&<string:aluno>", methods=["GET"])
def insert_into_palest(palestra, aluno):
    return insert_into_palestra(palestra, aluno)

# endregion

# region OBJ professor


@app.route("/professor/create/<int:cod>&<string:cpf>&"
           "<string:nome>&<string:dpto>", methods=["GET"])
def create_prof(cod, cpf, nome, dpto):
    return create_professor(cod, cpf, nome, dpto)


@app.route("/professor", methods=["GET"])
def get_all_prof():
    return get_all_professor()


@app.route("/professor/<int:id>", methods=["GET"])
def get_prof_by_id(id):
    return get_professor_by_id(id)


@app.route("/professor/delete/<int:id>", methods=["GET"])
def delete_prof_by_id(id):
    return delete_professor_by_id(id)


@app.route("/professor/edit/<int:id>&<string:atr>"
           "&<string:new>", methods=["GET"])
def edit_prof_by_id(id, atr, new):
    return edit_professor_by_id(id, atr, new)

# endregion

# region OBJ disciplina


@app.route("/disciplina/create/<int:cod>&<string:nome>&<string:dpto>"
           "&<string:prof>", methods=["GET"])
def create_disc(cod, nome, dpto, prof):
    return create_disciplina(cod, nome, dpto, prof)


@app.route("/disciplina", methods=["GET"])
def get_all_disc():
    return get_all_disciplina()


@app.route("/disciplina/<int:id>", methods=["GET"])
def get_disc_by_id(id):
    return get_disciplina_by_id(id)


@app.route("/disciplina/delete/<int:id>", methods=["GET"])
def delete_disc_by_id(id):
    return delete_disciplina_by_id(id)


@app.route("/disciplina/edit/<int:id>"
           "&<string:atr>&<string:new>", methods=["GET"])
def edit_disc_by_id(id, atr, new):
    return edit_disciplina_by_id(id, atr, new)

@app.route("/disciplina/material/<int:id>", methods=["GET"])
def get_material_disc_by_id(id):
    return get_material_disciplina_by_id(id)

# endregion

# region OBJ aluno


@app.route("/aluno/create/<int:matricula>&<string:nome>"
           "&<string:cpf>&<string:date>", methods=["GET"])
def create_aln(matricula, nome, cpf, date):
    return create_aluno(matricula, nome, cpf, date)


@app.route("/aluno", methods=["GET"])
def get_all_aln():
    return get_all_aluno()


@app.route("/aluno/<int:id>", methods=["GET"])
def get_aln_by_id(id):
    return get_aluno_by_id(id)


@app.route("/aluno/delete/<int:id>", methods=["GET"])
def delete_aln_by_id(id):
    return delete_aluno_by_id(id)


@app.route("/aluno/edit/<int:id>&<string:atr>&<string:new>", methods=["GET"])
def edit_aln_by_id(id, atr, new):
    return edit_aluno_by_id(id, atr, new)


@app.route("/aluno/all/<int:id>", methods=["GET"])
def get_everything_aln_by_id(id):
    return get_everything_aluno_by_id(id)

# endregion


if __name__ == "__main__":
    app.run(debug=True)
