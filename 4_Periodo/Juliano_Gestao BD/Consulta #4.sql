#mostra o estado do commit 0-desligado // 1-ligado 
SELECT @@autocommit

#desliga o autocomit
SET @@autocommit = OFF 

DROP TABLE dados_produtos

CREATE TABLE  dados_produtos
SELECT n_numeprodu, c_codiprodu, c_descprodu, n_valoprodu
FROM comprodu

SELECT * FROM dados_produtos

DELETE FROM dados_produtos 
WHERE n_numeprodu = 1

ROLLBACK 


#inicia a transação
START TRANSACTION;
	DELETE FROM dados_produtos;
	INSERT INTO dados_produtos(n_numeprodu, c_codiprodu, c_descprodu, n_valoprodu) VALUES (1, 45678, 'Mouse', 45.00);
	SELECT * FROM dados_produtos;
COMMIT;

SELECT * FROM dados_produtos;



















