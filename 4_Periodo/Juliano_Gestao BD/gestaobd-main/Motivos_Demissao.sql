
CREATE TABLE IF NOT EXISTS Motivos_Demissao (
	id INT NOT NULL,
	Motivo VARCHAR(70) NULL DEFAULT NULL,
	PRIMARY KEY (id)
);


INSERT INTO Motivos_Demissao (id, Motivo) VALUES
	(1, 'Demitido COM justa causa'),
	(2, 'Demitido SEM justa causa'),
	(4, 'Pedido de demissão SEM justa causa'),
	(5, 'Cessão do empregado'),
	(8, 'Morte'),
	(10, 'Rescisão contrato experiência antecipado pelo empregador'),
	(11, 'Rescisão contrato experiência antecipado pelo empregado'),
	(12, 'Término do contrato de experiência'),
	(22, 'Término do contrato de trabalho por tempo determinado');

