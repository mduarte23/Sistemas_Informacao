drop trigger if EXISTS calcular_preco_venda;

#criando TRIGGER para calcular preco de venda do produto
delimiter $$
CREATE TRIGGER calcular_preco_venda
before INSERT ON produto
FOR EACH ROW
BEGIN
	#calculando preco de venda com 50% de lucro e inserindo no campo valor_venda
	SET NEW.valor_venda = NEW.valor_compra * 1.5;
END $$



DROP TRIGGER if EXISTS recalcular_preco_venda;

#criando uma TRIGGER para ajustar o preco de venda quando altera o preco de custo 
delimiter $$
CREATE TRIGGER recalcular_preco_venda
BEFORE UPDATE ON produto
FOR EACH ROW 
BEGIN
	#calcula o preco de venda se o preço do produto for alterado
	if NEW.valor_compra <> OLD.valor_compra then 
		SET NEW.valor_venda = NEW.valor_compra * 1.5;
	END if;
END $$


 
 
 DROP TRIGGER if EXISTS calcular_valor_gasto;
 
 #trigger para somar o total de valores gastos
 delimiter $$
 CREATE TRIGGER calcular_valor_gasto
 AFTER INSERT ON produto
 FOR EACH ROW 
 BEGIN 
 	#atualizando o valor gasto no caixa
 	UPDATE caixa 
 	SET total_gasto = total_gasto + (NEW.valor_compra * NEW.estoque),
 	total_caixa = total_caixa - (NEW.valor_compra * NEW.estoque)
 	WHERE id_caixa = 2;
END 
$$


DROP TRIGGER if EXISTS reposicao_estoque_ajustar_caixa;
#trigger para ajustar valor de caixa quando compra mais produtos ja cadastrados
delimiter $$
CREATE TRIGGER reposicao_estoque_ajustar_caixa
AFTER UPDATE ON produto
FOR EACH ROW 
BEGIN 
	DECLARE qtd_novos FLOAT DEFAULT 0;
	DECLARE valor FLOAT DEFAULT 0;
	 -- Verifica se houve reposição de estoque
   IF NEW.estoque > OLD.estoque THEN
		#atualizando o valor do caixa e calculando a diferenca de quantidade de produtos	
		SET qtd_novos = NEW.estoque - OLD.estoque;
		SET valor = NEW.valor_compra * qtd_novos;
		UPDATE caixa
		SET total_caixa = total_caixa + valor,
		total_gasto = total_gasto + valor
		WHERE id_caixa = 2;
	END IF;
END
$$

DROP TRIGGER IF EXISTS calcula_pagamento;

DELIMITER $$

CREATE TRIGGER calcula_pagamento
AFTER INSERT ON agendamento
FOR EACH ROW
BEGIN
    -- Declaração de variáveis
    DECLARE valor_pagar FLOAT(10,2) DEFAULT 0;
    DECLARE valor_produto FLOAT(10,2) DEFAULT 0;
    DECLARE quantidade_produto FLOAT(10,2) DEFAULT 0;
    DECLARE valor_servico FLOAT(10,2) DEFAULT 0;

    -- Obtendo o valor do serviço e a quantidade de produtos
    SELECT s.valor_servico, s.qtd_produto
    INTO valor_servico, quantidade_produto
    FROM servico s
    WHERE s.id_servico = NEW.id_servico;

    -- Obtendo o valor do produto relacionado ao serviço
    SELECT p.valor_venda
    INTO valor_produto
    FROM produto p
    INNER JOIN servico s ON p.id_produto = s.id_produto
    WHERE s.id_servico = NEW.id_servico;

    -- Calculando o valor total a ser pago pelo cliente
    SET valor_pagar = (valor_produto * quantidade_produto) + valor_servico;

    -- Inserindo o valor calculado na tabela pagamento
    INSERT INTO pagamento (valor_pago, id_agendamento)
    VALUES (valor_pagar, NEW.id_agendamento);

    -- Atualizando o total arrecadado e o total do caixa
    UPDATE caixa
    SET total_arrecadado = total_arrecadado + valor_pagar,
        total_caixa = total_caixa + valor_pagar
    WHERE id_caixa = 2;

END $$


	
	
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 