
CREATE TABLE IF NOT EXISTS Estado_Civil (
	id CHAR(1) NOT NULL,
	EstadoCivil VARCHAR(30) NULL DEFAULT NULL,
	PRIMARY KEY (id)
);


INSERT INTO Estado_Civil (id, EstadoCivil) VALUES
	('C', 'Casado(a)'),
	('D', 'Divorciado(a)'),
	('J', 'Separado(a)'),
	('O', 'Outros'),
	('S', 'Solteiro(a)'),
	('U', 'União Estável'),
	('V', 'Viúvo(a)');

