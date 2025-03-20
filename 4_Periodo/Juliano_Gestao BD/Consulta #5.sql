delimiter //
CREATE PROCEDURE insere_dados()
BEGIN 
	#declara variavel erro_sql como falso 
	DECLARE erro_sql TINYINT DEFAULT FALSE;
	#se ocorrer algum erro na execução muda a variavel erro_sql pra TRUE
	DECLARE CONTINUE handler FOR SQLEXCEPTION SET erro_sql = TRUE;
	START TRANSACTION;
		INSERT INTO dados_produtos(n_numeprodu, c_codiprodu, c_descprodu, n_valoprodu) 
		VALUES (2, 45680, 'TECLADO', 50.00); 
		INSERT INTO dados_produtos(n_numeprodu, c_codiprodu, c_descprodu, n_valoprodu) 
		VALUES (3, 45682, 'GABINETE', 250.00); 
		INSERT INTO dados_produtos(n_numeprodu, c_codiprodu, c_descprodu, n_valoprodu) 
		VALUES (4, 45684, 'PROCESSADOR', 1050.00); 
		INSERT INTO dados_produtos(n_numeprodu, c_codiprodu, c_descprodu, n_valoprodu) 
		VALUES (5, 45686, 'MEMORIA 16GB', 300,00); 
		if erro_sql = FALSE then
			COMMIT;
			SELECT 'Transação efetivada com sucesso!' AS Resultado;
		else
			ROLLBACK;
			SELECT 'Erro na transação' AS Resultado;
		END if;
	END //
		

