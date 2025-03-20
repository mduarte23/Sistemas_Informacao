CREATE USER libertas@'%' IDENTIFIED BY 'alunos4p'

GRANT ALL PRIVILEGES ON biblioteca.* TO libertas@'%'

CREATE DATABASE livros

USE livros

CREATE TABLE autor(
	id_autor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nome VARCHAR (100)
)

CREATE TABLE livro(
	id_livro INT PRIMARY KEY  NOT NULL  AUTO_INCREMENT,
	titulo VARCHAR (100) not null,
	id_autor INT NOT NULL ,
	ano_publicacao YEAR NOT NULL,
	
	CONSTRAINT fk_autor
	FOREIGN KEY (id_autor)
	REFERENCES autor(id_autor)
);

CREATE TABLE emprestimo (
	id_emprestimo INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
	id_livro INT,
	data_emprestimo DATE,
	data_devolucao DATE,
	
	CONSTRAINT fk_livro
	FOREIGN KEY (id_livro)
	REFERENCES livro(id_livro)
)

INSERT INTO autor(nome)
VALUES ('Machado de Assis'),
('Mauricio de Sousa'), 
('Paulo Coelho')

INSERT INTO livro(titulo, id_autor, ano_publicacao)
VALUES ('Dom Casmurro', 1, '1999'),
('Turma da Monica', 2, '1959'), 
('O Alquimista', 3, '1988')

INSERT INTO emprestimo(id_livro, data_emprestimo, data_devolucao)
VALUES (1, '2024-05-21', '2024-05-28'),
(2, '2024-01-02', '2024-02-10'), 
(3, '2023-05-12', '2023-05-18')


SELECT * FROM autor

SELECT * from livro

SELECT l.id_livro, l.titulo, a.nome FROM livro l
INNER JOIN autor a
WHERE l.id_autor = a.id_autor

SELECT l.titulo, COUNT(*) AS Qtd_Emprestimo FROM emprestimo e
INNER JOIN livro l
WHERE e.id_livro = l.id_livro
GROUP BY l.titulo
