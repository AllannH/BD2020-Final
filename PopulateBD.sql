INSERT INTO INSTITUICAO (cnpj, nome) VALUES ('3994021', 'UnB');
INSERT INTO INSTITUICAO (cnpj, nome) VALUES ('4242424', 'USP');
INSERT INTO INSTITUICAO (cnpj, nome) VALUES ('0900043', 'UFPE');
INSERT INTO INSTITUICAO (cnpj, nome) VALUES ('7783000', 'UFRJ');
INSERT INTO INSTITUICAO (cnpj, nome) VALUES ('8899331', 'UFPA');


INSERT INTO DEPARTAMENTO (cod, nome, instituicao) VALUES ('2200', 'Matemática', '3994021');
INSERT INTO DEPARTAMENTO (cod, nome, instituicao) VALUES ('1100', 'Ciência da Computação', '3994021');
INSERT INTO DEPARTAMENTO (cod, nome, instituicao) VALUES ('0010', 'Medicina', '3994021');
INSERT INTO DEPARTAMENTO (cod, nome, instituicao) VALUES ('3310', 'Artes', '3994021');
INSERT INTO DEPARTAMENTO (cod, nome, instituicao) VALUES ('4055', 'Direito', '3994021');


INSERT INTO PROFESSOR (cod, cpf, nome, lattes, dpto) VALUES ('211', '343134234', 'Carlos Fonsceca', 'https://lattes.com/3HFUF43', '2200');
INSERT INTO PROFESSOR (cod, cpf, nome, lattes, dpto) VALUES ('342', '173470894', 'Joao Pedro', 'https://lattes.com/7JAFS98', '0010');
INSERT INTO PROFESSOR (cod, cpf, nome, lattes, dpto) VALUES ('612', '147895624', 'Julio Gomes', 'https://lattes.com/9BYSF12', '1100');
INSERT INTO PROFESSOR (cod, cpf, nome, lattes, dpto) VALUES ('510', '953456835', 'Matheus da Silva', 'https://lattes.com/3GKAS09', '3310');
INSERT INTO PROFESSOR (cod, cpf, nome, lattes, dpto) VALUES ('168', '678349672', 'Arthur Filho', 'https://lattes.com/8IVDA41', '2200');
INSERT INTO PROFESSOR (cod, cpf, nome, lattes, dpto) VALUES ('397', '946723504', 'Roberto Farias', 'https://lattes.com/1GDAA52', '1100');


INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('1', 'Cálculo Vetorial', 'Palestra sobre vetores e tensores', 'Youtube', 'https://youtube.com/YUHDs0'); 
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('2', 'IA na Educação', 'Palestra sobre Inteligencia Artificial', 'ZOOM', 'https://zoom.com/IAS-QPE-TLK');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('3', 'Computação Hoje', 'Palestra sobre computação na atualidade', 'Skype', 'https://Skype.com/GasQR32');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('4', 'Importancia da Matematica', 'Palestra sobre a matematica', 'Teams', 'https://Teams.com/ASC13A2&2');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('5', 'Atividade fisica na pandemia', 'Palestra sobre atividade fisica', 'Youtube', 'https://youtube.com/YTDLs0');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('6', 'Politica moderna', 'Palestra sobre politica moderna', 'Meet', 'https://Meet.com/OPQF1v2');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('7', 'Calculo 1 PT.1', 'Aula 1 de Calculo 1', 'Meet', 'https://Meet.com/AFDBYHI');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('8', 'Calculo 1 PT.2', 'Aula 2 de Calculo 1', 'Meet', 'https://Meet.com/AFDBYHI');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('9', 'Calculo 1 PT.3', 'Aula 3 de Calculo 1', 'Meet', 'https://Meet.com/AFDBYHI'); 
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('10', 'Banco de Dados Aula 1', 'Aula 1 de Banco de Dados', 'Teams', 'https://Teams.com/OFASI12&9');  
INSERT INTO MATERIAL_VIDEO (cod, titulo, descricao, plataforma, link) VALUES ('11', 'Banco de Dados Aula 2', 'Aula 2 de Banco de Dados', 'Teams', 'https://Meet.com/OFASI12&9');  


INSERT INTO PALESTRAS (cod, titulo, datahora, prof, video) VALUES ('1', 'Cálculo Vetorial', '2020-12-12', '211', '1');
INSERT INTO PALESTRAS (cod, titulo, datahora, prof, video) VALUES ('2', 'IA na Educação', '2020-02-19', '397', '2');
INSERT INTO PALESTRAS (cod, titulo, datahora, prof, video) VALUES ('3', 'Computação Hoje', '2020-10-05', '612', '3');
INSERT INTO PALESTRAS (cod, titulo, datahora, prof, video) VALUES ('4', 'Importancia da Matematica', '2019-03-26', '168', '4');
INSERT INTO PALESTRAS (cod, titulo, datahora, prof, video) VALUES ('5', 'Atividade fisica na pandemia', '2021-08-08', '342', '5');
INSERT INTO PALESTRAS (cod, titulo, datahora, prof, video) VALUES ('6', 'Politica moderna', '2020-10-02', '397', '6');


INSERT INTO ALUNO (matricula, nome, cpf, nasc) VALUES ('1332321', 'Ana Lucena', '339232332', '2000-01-01');
INSERT INTO ALUNO (matricula, nome, cpf, nasc) VALUES ('3457125', 'Ana Julia', '792227257', '1999-07-15');
INSERT INTO ALUNO (matricula, nome, cpf, nasc) VALUES ('6167235', 'James Rodrigues', '954271783', '2000-01-23');
INSERT INTO ALUNO (matricula, nome, cpf, nasc) VALUES ('7235156', 'Ronaldo Pessoa', '123316267', '1998-09-17');
INSERT INTO ALUNO (matricula, nome, cpf, nasc) VALUES ('8281290', 'Felipe Passos', '891472825', '2001-11-08');


INSERT INTO INSCRITOS (palestra, aluno) VALUES ('1', '1332321');
INSERT INTO INSCRITOS (palestra, aluno) VALUES ('4', '1332321');
INSERT INTO INSCRITOS (palestra, aluno) VALUES ('6', '1332321');
INSERT INTO INSCRITOS (palestra, aluno) VALUES ('6', '3457125');
INSERT INTO INSCRITOS (palestra, aluno) VALUES ('5', '7235156');
INSERT INTO INSCRITOS (palestra, aluno) VALUES ('2', '8281290');
INSERT INTO INSCRITOS (palestra, aluno) VALUES ('3', '8281290');
INSERT INTO INSCRITOS (palestra, aluno) VALUES ('1', '7235156');


INSERT INTO DISCIPLINA (cod, nome, dpto, prof) VALUES ('1', 'Banco de Dados', '1100', '612');
INSERT INTO DISCIPLINA (cod, nome, dpto, prof) VALUES ('2', 'Calculo 1', '2200', '168');
INSERT INTO DISCIPLINA (cod, nome, dpto, prof) VALUES ('3', 'Calculo 2', '2200', '211');
INSERT INTO DISCIPLINA (cod, nome, dpto, prof) VALUES ('4', 'Arte Moderna', '3310', '510');
INSERT INTO DISCIPLINA (cod, nome, dpto, prof) VALUES ('5', 'Anatomia', '0010', '342');
INSERT INTO DISCIPLINA (cod, nome, dpto, prof) VALUES ('6', 'Teoria da Computacao', '1100', '397');


INSERT INTO ENCONTROS (disciplina, datahora, video) VALUES ('1','2020-11-30 12:00:00','10');
INSERT INTO ENCONTROS (disciplina, datahora, video) VALUES ('1','2020-11-30 13:00:00','11');
INSERT INTO ENCONTROS (disciplina, datahora, video) VALUES ('2','2020-12-11 13:00:00','7');
INSERT INTO ENCONTROS (disciplina, datahora, video) VALUES ('2','2020-12-13 14:30:00','8');
INSERT INTO ENCONTROS (disciplina, datahora, video) VALUES ('2','2020-12-15 16:00:00','9');


INSERT INTO MATERIAL_BIBLIO (cod, titulo, autor, link, disciplina) VALUES ('1','Limite para C1','James Rodrigues','localhost:8803/Livros/AFGYUIH','2');
INSERT INTO MATERIAL_BIBLIO (cod, titulo, autor, link, disciplina) VALUES ('2','Derivada para C1','Gareth Junior','localhost:8803/Livros/BBPAUSD','2');
INSERT INTO MATERIAL_BIBLIO (cod, titulo, autor, link, disciplina) VALUES ('3','Integral para C1','Rodolph Beat','localhost:8803/Livros/NMIGRAA','2');
INSERT INTO MATERIAL_BIBLIO (cod, titulo, autor, link, disciplina) VALUES ('4','Introducao ao banco de dados','Felipe Moraes','localhost:8803/Livros/ONYGAFA','1');
INSERT INTO MATERIAL_BIBLIO (cod, titulo, autor, link, disciplina) VALUES ('5','Algebra Relacional','Bianca Teixeira','localhost:8803/Livros/PIUHNFA','1');


INSERT INTO TAGS_VIDEO (video_id, tag) VALUES ('7','Limite, funcoes');
INSERT INTO TAGS_VIDEO (video_id, tag) VALUES ('8','Derivada, Definicao');
INSERT INTO TAGS_VIDEO (video_id, tag) VALUES ('9','Integral, Definida');
INSERT INTO TAGS_VIDEO (video_id, tag) VALUES ('10','Introducao');
INSERT INTO TAGS_VIDEO (video_id, tag) VALUES ('11','CRUD');


INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('1', '1332321');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('1', '7235156');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('1', '6167235');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('2', '8281290');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('2', '7235156');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('3', '8281290');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('3', '6167235');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('3', '7235156');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('4', '7235156');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('4', '1332321');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('5', '7235156');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('5', '8281290');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('5', '3457125');
INSERT INTO MATRICULAS (disciplina, aluno) VALUES ('6', '3457125');



INSERT INTO NOTAS (disciplina, aluno, notas) VALUES ('2', '1332321', 80);
INSERT INTO NOTAS (disciplina, aluno, notas) VALUES ('1', '1332321', 80);
INSERT INTO NOTAS (disciplina, aluno, notas) VALUES ('5', '8281290', 80);
INSERT INTO NOTAS (disciplina, aluno, notas) VALUES ('3', '3457125', 80);
INSERT INTO NOTAS (disciplina, aluno, notas) VALUES ('3', '6167235', 80);


CREATE VIEW GetPalestras AS
SELECT PALESTRAS.titulo, PALESTRAS.datahora, PROFESSOR.nome, VID.titulo AS palestra, VID.descricao, VID.link FROM PALESTRAS
JOIN PROFESSOR ON PROFESSOR.cod = PALESTRAS.prof
JOIN MATERIAL_VIDEO AS VID ON VID.cod = PALESTRAS.video
WHERE PALESTRAS.datahora > CURDATE() AND PALESTRAS.datahora < CURDATE() + INTERVAL 30 DAY;

SELECT * FROM GetPalestras;

DELIMITER $$
CREATE PROCEDURE INSCRICAO (IN cod VARCHAR(25), IN matricula VARCHAR(25))
BEGIN
	IF (SELECT COUNT(ALUNO) from INSCRITOS WHERE PALESTRA = cod) < 50 THEN
		INSERT INTO INSCRITOS (palestra, aluno) VALUES (cod, matricula);
	END IF;
END $$
DELIMITER ;

DROP PROCEDURE INSCRICAO;

CALL INSCRICAO(2,3457125)


