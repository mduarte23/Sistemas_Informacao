CREATE DATABASE carros

USE carros

CREATE TABLE tipo(
	idtipo INT PRIMARY KEY AUTO_INCREMENT,
	nometipo VARCHAR (50)
);

INSERT INTO tipo (nometipo)
VALUES ('Carro');

INSERT INTO tipo (idtipo, nometipo)
VALUES (2, 'Moto');

INSERT INTO tipo (nometipo)
VALUES ('Avião');

INSERT INTO tipo (nometipo)
VALUES ('Barco');


SELECT * FROM tipo;

CREATE TABLE marca(
	idmarca INT PRIMARY KEY AUTO_INCREMENT,
	nomemarca VARCHAR (50)
);

INSERT INTO marca (nomemarca)
VALUES ('VW');

INSERT INTO marca (nomemarca)
VALUES ('Fiat');

INSERT INTO marca (nomemarca)
VALUES ('Honda');

SELECT * FROM marca;

CREATE TABLE veiculo(
	idveiculo INT PRIMARY KEY AUTO_INCREMENT,
	placa VARCHAR (10),
	modelo VARCHAR (50),
	idmarca INT,
	idtipo INT,
	
	CONSTRAINT fkmarcaveiculo
	FOREIGN KEY (idmarca)
	REFERENCES marca(idmarca),
	
	CONSTRAINT fktipoveiculo
	FOREIGN KEY (idtipo)
	REFERENCES tipo(idtipo)
);

INSERT INTO veiculo(idveiculo, placa, modelo, idmarca, idtipo)
VALUES (1, 'XXX-1234', 'Fusca', 1, 1)

INSERT INTO veiculo(placa, modelo, idmarca, idtipo)
VALUES ('WWW-321', 'Uno', 2, 1)

INSERT INTO veiculo(placa, modelo ,idmarca, idtipo)
VALUES ('YYY-1233', 'Gol', 1, 1)

INSERT INTO veiculo (placa, modelo, idmarca, idtipo)
VALUES ('JJJ-1234', 'CG 150', 3, 2)

SELECT * FROM veiculo

CREATE DATABASE exercicio01

USE exercicio01

CREATE TABLE filme(
	idfilme INT PRIMARY KEY AUTO_INCREMENT ,
	titulo VARCHAR(50),
	data_lancamento DATE 
);
CREATE TABLE ator(
	idator INT PRIMARY KEY AUTO_INCREMENT ,
	nome VARCHAR (50),
	genero CHAR(1)
);
CREATE TABLE filmeator(
	idfilme INT,
	idator INT,
	PRIMARY KEY (idfilme, idator),
	
	CONSTRAINT fkfilmeator
	FOREIGN KEY (idfilme)
	REFERENCES filme(idfilme),
	
	CONSTRAINT fkatorfilme
	FOREIGN KEY (idator)
	REFERENCES ator(idator)
);


SELECT * FROM filme;

ALTER TABLE ator
add email VARCHAR(50);

ALTER TABLE filme

INSERT INTO filmeator (idfilme, idator)
VALUES (2,4);

INSERT INTO filme (titulo)
VALUES ('O Auto da Compadecida');

#INSERE
INSERT INTO ator (nome, genero)
VALUES ('Matheus Nachtergale', 'M');

#MUDAR VALOR
UPDATE ator
SET genero  = 'F'
WHERE idator  = 2;

#APAGAR
DELETE FROM filmeator
WHERE idfilme = 2;

DELETE FROM filme
WHERE idfilme = 2;




USE trabalho

#inserindo valores

SELECT * FROM cidade

INSERT INTO cidade (idcidade, nomecidade, uf)
VALUES(1, 'Pratapolis', 'MG');

SELECT * FROM cliente

INSERT INTO cliente(idcliente, nome, cpf, logradouro, numero, bairro, cep, telefone, idcidade)
VALUES (1, 'Teosvaldo' , '14873948299', 'rua da saudade', '999', 'jequitiba', '86900753', 98771152, 1);

SELECT * FROM fornecedor

INSERT INTO fornecedor(idfornecedor, nome, cnpj, logradouro, numero, cep, telefone, idcidade)
VALUES (1, 'Ironaldo', '14725836998745', 'Rua Teodorico Fontoura', '723', '37804923', 82453755, 1);

SELECT * FROM cidade

INSERT INTO cidade (idcidade, nomecidade, uf)
VALUES(2, 'São Joao DelRei', 'MG');

SELECT * FROM marca

INSERT INTO marca(idmarca, nomemarca)
VALUES (1, 'Phillips');

SELECT * FROM produto

INSERT INTO produto(idproduto, descricao, precocusto, precovenda, saldoestoque, codbarras, idmarca)
VALUES (1, 'Barbeador', 4.78, 7.50, 77, 741852, 1)

SELECT * FROM usuario

INSERT INTO usuario(idusuario, login, senha, email)
VALUES (1, '825', '987412', 'teosvaldo@gmail.com')

SELECT * FROM compra

INSERT INTO compra(idcompra, numeronf, dia, quantidade, valor, idfornecedor)
VALUES (1, 78945236, '2024-02-03', 2, 15.00, 1)

SELECT * FROM cliente

INSERT INTO cliente(idcliente, nome, cpf, logradouro, numero, bairro, cep, telefone, idcidade)
VALUES (2, 'Garideia', '14283948255', 'Rua das Queresmeiras', 142, 'Piedade', '71425999', 82536954, 2)

SELECT * FROM vendedor

INSERT INTO vendedor (idvendedor, nome, cpf, logradouro, numero, bairro, cep, telefone, percomissao, idcidade)
VALUES (1, 'Ely', '14258673958', 'Rua Maria Antonia', 741, 'Souza', '72351058', 123456789, 12.40, 2)

#alterando valores

SELECT * FROM cliente

UPDATE cliente
SET cpf  = '12345678900'
WHERE idcliente  = 2;

SELECT * FROM vendedor

UPDATE vendedor
SET logradouro = 'Rua B'
WHERE idvendedor = 1

SELECT * FROM marca

UPDATE marca
SET nomemarca = 'Philco'
WHERE idmarca = 1

SELECT * FROM usuario

UPDATE usuario 
SET login = 'ab1425'
WHERE idusuario = 1

SELECT * FROM produto 

UPDATE produto
SET precovenda = 8
WHERE idproduto = 1

#excluindo registros
SELECT * FROM usuario

DELETE FROM usuario
WHERE idusuario = 1 ;

SELECT * FROM cliente

DELETE FROM cliente
WHERE idcidade = 1;

USE carros

SELECT * FROM veiculo

CREATE DATABASE carro_consulta

USE carro_consulta

CREATE TABLE veiculo(
	idveiculo INT PRIMARY KEY AUTO_INCREMENT ,
	modelo VARCHAR(50),
	marca  VARCHAR (50),
	ano INT,
	placa CHAR (7),
	cor VARCHAR(50),
	preco float 
);


SELECT * FROM veiculo

INSERT INTO veiculo (modelo, marca, ano, placa, cor, preco)
VALUES ('Uno Mille', 'Fiat', 2003, 'UNO9898', 'branco', 20000.00)

SELECT DISTINCT marca FROM veiculo
ORDER BY marca;

SELECT modelo,marca, preco FROM veiculo
ORDER BY preco DESC ;

SELECT modelo,marca, preco FROM veiculo
ORDER BY preco 

SELECT modelo, cor, preco FROM veiculo
WHERE marca = 'Fiat'

SELECT * FROM veiculo
WHERE modelo LIKE '%Turbo%'

SELECT modelo, marca, preco FROM veiculo
WHERE cor = 'preto'

SELECT modelo, marca, preco FROM veiculo
WHERE (marca = 'Fiat' AND preco > 10000) OR (marca <> 'Fiat' AND preco >= 15000)

SELECT modelo, marca, cor FROM veiculo
WHERE (cor = 'azul' OR cor = 'amarela' OR cor = 'verde')
ORDER BY marca

SELECT modelo, ano, preco FROM veiculo
WHERE (preco >= 10000 AND preco <= 20000)
ORDER BY preco DESC 

SELECT modelo, marca, ano, placa FROM veiculo
WHERE placa LIKE '%8'