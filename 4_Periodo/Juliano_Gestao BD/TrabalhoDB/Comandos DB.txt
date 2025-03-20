CREATE DATABASE salao_beleza

USE salao_beleza


CREATE TABLE cliente(
	id_cliente INT AUTO_INCREMENT PRIMARY KEY ,
	nome_cliente VARCHAR(100),
	endereço VARCHAR (100),
	telefone VARCHAR (20),
	cpf CHAR(11)
);

CREATE TABLE funcionario(
	id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
	nome_funcionario VARCHAR(100),
	endereco VARCHAR(100),
	telefone VARCHAR(100)
);
	
CREATE TABLE servico(
	id_servico INT AUTO_INCREMENT PRIMARY KEY,
	nome_servico VARCHAR(100),
	valor_servico FLOAT(10,2),
	id_produto INT,
	qtd_produto FLOAT 
);

CREATE TABLE agendamento(
	id_agendamento INT AUTO_INCREMENT PRIMARY KEY,
	data_agendamento DATE,
	id_cliente INT,
	id_funcionario INT,
	id_servico INT 
);

CREATE TABLE produto(
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
	nome_produto VARCHAR (100),
	estoque FLOAT,
	valor_compra FLOAT(10,2),
	valor_venda FLOAT(10,2)
);

CREATE TABLE caixa(
	id_caixa INT AUTO_INCREMENT PRIMARY KEY,
	total_caixa FLOAT (10,2),
	total_gasto FLOAT (10,2),
	total_arrecadado FLOAT (10,2)
);

CREATE TABLE pagamento (
	id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
	valor_pago FLOAT(10,2),
	id_agendamento int
);

INSERT INTO  caixa (total_caixa, total_gasto, total_arrecadado)
VALUES (10000, 0 , 0)

SELECT * FROM caixa

SHOW TRIGGERS


-- Populando a tabela cliente
INSERT INTO cliente (nome_cliente, endereço, telefone, cpf)
VALUES
('João Silva', 'Rua A, 123', '11999999999', '12345678901'),
('Maria Oliveira', 'Rua B, 456', '21988888888', '23456789012'),
('Carlos Pereira', 'Rua C, 789', '31977777777', '34567890123'),
('Ana Costa', 'Rua D, 101', '41966666666', '45678901234'),
('Lucas Souza', 'Rua E, 202', '51955555555', '56789012345'),
('Fernanda Lima', 'Rua F, 303', '61944444444', '67890123456'),
('Paulo Almeida', 'Rua G, 404', '71933333333', '78901234567'),
('Camila Santos', 'Rua H, 505', '81922222222', '89012345678'),
('Ricardo Gonçalves', 'Rua I, 606', '91911111111', '90123456789'),
('Juliana Rocha', 'Rua J, 707', '11900000000', '01234567890');

-- Populando a tabela funcionario
INSERT INTO funcionario (nome_funcionario, endereco, telefone)
VALUES
('Pedro Martins', 'Rua Z, 100', '21999999999'),
('Lucas Ribeiro', 'Rua Y, 200', '31988888888'),
('Larissa Andrade', 'Rua X, 300', '41977777777');

-- Populando a tabela produto
INSERT INTO produto (nome_produto, estoque, valor_compra)
VALUES
('Shampoo', 50, 10.00),
('Condicionador', 30, 12.00),
('Creme de Hidratação', 20, 25.00),
('Tintura', 15, 20.00),
('Gel Fixador', 25, 8.00),
('Pente', 100, 3.00),
('Escova', 60, 7.00);

SELECT * FROM produto

-- Populando a tabela servico
INSERT INTO servico (nome_servico, valor_servico, id_produto, qtd_produto)
VALUES
('Corte de Cabelo', 50.00, 13, 1), -- Usa um pente
('Escova Progressiva', 150.00, 17, 1), -- Usa creme de hidratação
('Pintura', 120.00, 18, 1), -- Usa tintura
('Hidratação', 80.00, 17, 1), -- Usa creme de hidratação
('Modelagem', 60.00, 19, 1); -- Usa gel fixador

-- Populando a tabela agendamento
INSERT INTO agendamento (data_agendamento, id_cliente, id_funcionario, id_servico)
VALUES
('2024-11-15', 1, 1, 11),
('2024-11-16', 2, 2, 12),
('2024-11-17', 3, 3, 13),
('2024-11-18', 4, 1, 14),
('2024-11-19', 5, 2, 15),
('2024-11-20', 6, 3, 11),
('2024-11-21', 7, 1, 12),
('2024-11-22', 8, 2, 13),
('2024-11-23', 9, 3, 14),
('2024-11-24', 10, 1, 15);






