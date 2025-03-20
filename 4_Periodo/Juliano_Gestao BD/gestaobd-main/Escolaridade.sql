
CREATE TABLE IF NOT EXISTS Escolaridade (
	id INT NOT NULL,
	Escolaridade VARCHAR(50) NULL DEFAULT NULL,
	PRIMARY KEY (id)
);


INSERT INTO Escolaridade (id, Escolaridade) VALUES
	(1, 'Analfabeto'),
	(2, 'Até 5º Ano Incompleto'),
	(3, 'Até 5º Ano Completo'),
	(4, 'Do 6º ao 9º Incompleto'),
	(5, 'Fundamental Completo'),
	(6, 'Médio Incompleto'),
	(7, 'Médio Completo'),
	(8, 'Superior Incompleto'),
	(9, 'Superior Completo'),
	(10, 'Pós Graduação Compl.'),
	(11, 'Mestrado Completo'),
	(12, 'Doutorado Completo'),
	(13, 'Ph.D.');

