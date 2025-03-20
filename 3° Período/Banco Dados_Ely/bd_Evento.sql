CREATE DATABASE trabalho

USE trabalho

CREATE TABLE usuario(
	idusuario INT PRIMARY KEY,
	login VARCHAR (50),
	senha VARCHAR (50),
	email VARCHAR (50)
);

CREATE TABLE marca(
	idmarca INT PRIMARY KEY,
	nomemarca VARCHAR (50)
);


CREATE TABLE produto(
	idmarca INT PRIMARY KEY,
	descricao VARCHAR (50),
	precocusto FLOAT,
	precovenda FLOAT,
	saldoestoque INT,
	codbarras INT,
	
	CONSTRAINT fkmarca
	FOREIGN KEY idmarca
	REFERENCES marca(idmarca)	
);

CREATE TABLE cidade(
	idcidade INT PRIMARY KEY,
	nomecidade VARCHAR(50),
	uf CHAR(2)
);

CREATE TABLE cliente(
	idcliente INT PRIMARY KEY,
	nome VARCHAR (70),
	#usar char ou int 
	cpf CHAR(11),
	logradouro VARCHAR (50),
	numero INT,
	bairro VARCHAR (50),
	#usar char ou int#########################################
	cep CHAR (8),
	telefone INT,
	
	CONSTRAINT fkcidade
	FOREIGN KEY idcidade
	REFERENCES cidade(fkcidade)
);

CREATE TABLE fornecedor(
	idfornecedor INT PRIMARY KEY,
	nome VARCHAR (70),
	cnpj CHAR(14),
	logradouro VARCHAR (50),
	numero INT,
	bairro VARCHAR (50),
	#usar char ou int#########################################
	cep CHAR (8),
	telefone INT,
	
	CONSTRAINT fkcidade
	FOREIGN KEY idcidade
	REFERENCES cidade(fkcidade)
);

CREATE TABLE vendedor(
	idvendedor INT PRIMARY KEY,
	nome VARCHAR (70),
	cpf CHAR(11),
	logradouro VARCHAR (50),
	numero INT,
	bairro VARCHAR (50),
	#usar char ou int#########################################
	cep CHAR (8),
	telefone INT,
	percomissao FLOAT,
	
	CONSTRAINT fkcidade
	FOREIGN KEY idcidade
	REFERENCES cidade(fkcidade)
);

CREATE TABLE caixa(
	idcaixa INT PRIMARY KEY,
	dia DATE,
	descricao VARCHAR (50), 
	valor FLOAT,
	##confirmar debito 
	debitocredito CHAR(1),
);

CREATE TABLE compra(
	idcompra INT PRIMARY KEY,
	numeronf INT,
	dia DATE,
	quantidade INT,
	valor FLOAT,
	
	CONSTRAINT fkfornecedor
	FOREIGN KEY idfornecedor
	REFERENCES fornecedor(idfornecedor)
);

CREATE TABLE contasapagar(
	idpagar INT PRIMARY KEY,
	dia DATE,
	valor FLOAT,
	vencimento DATE,
	pagamento DATE,
	valorpago FLOAT,
	
	CONSTRAINT fkfornecedor
	FOREIGN KEY idfornecedor
	REFERENCES fornecedor(idfornecedor),
	
	CONSTRAINT fkcompra
	FOREIGN KEY idcompra
	REFERENCES compra(idcompra),
	
	CONSTRAINT fkcaixa
	FOREIGN KEY idcaixa
	REFERENCES caixa(idcaixa)
);

CREATE TABLE contasareceber(
	idreceber INT PRIMARY KEY,
	dia DATE;
	valor FLOAT,
	vencimento DATE,
	pagamento FLOAT,
	valorpago FLOAT,
	
	CONSTRAINT fkcliente
	FOREIGN KEY idcliente
	REFERENCES cliente(idcliente),
	
	CONSTRAINT fkcaixa
	FOREIGN KEY idcaixa
	REFERENCES caixa(idcaixa)
);

CREATE TABLE venda(
	idvenda INT PRIMARY KEY,
	numeronf INT,
	dia DATE,
	quantidade INT,
	valor FLOAT,
	comissao FLOAT,
	
	CONSTRAINT fkcliente
	FOREIGN KEY idcliente
	REFERENCES cliente(idcliente),
	
	CONSTRAINT fkvendedor
	FOREIGN KEY idvendedor
	REFERENCES vendedor(idvendedor),
	
	CONSTRAINT fkreceber
	FOREIGN KEY idreceber
	REFERENCES contasareceber(idreceber)
);

CREATE TABLE vendaproduto(
	idproduto INT,
	idvenda INT,
	PRIMARY KEY (idproduto, idvenda),
	
	CONSTRAINT fkproduto
	FOREIGN KEY idproduto
	REFERENCES produto(idproduto),
	
	CONSTRAINT fkvenda
	FOREIGN KEY idvenda
	REFERENCES venda(idvenda)
);

CREATE TABLE compraproduto(
	idproduto INT,
	idcompra INT,
	PRIMARY KEY (idproduto, idcompra),
	
	CONSTRAINT fkproduto
	FOREIGN KEY idproduto
	REFERENCES produto(idproduto),
	
	CONSTRAINT fkcompra
	FOREIGN KEY idcompra
	REFERENCES compra(idcompra)
);