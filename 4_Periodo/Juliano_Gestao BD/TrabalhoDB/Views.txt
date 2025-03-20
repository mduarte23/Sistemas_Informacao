CREATE VIEW pagamento_cliente AS 
SELECT c.nome_cliente AS cliente, a.data_agendamento AS data, p.valor_pago AS valor_pagar FROM pagamento p 
INNER JOIN agendamento a ON p.id_agendamento = a.id_agendamento
INNER JOIN cliente c ON c.id_cliente = a.id_cliente



CREATE VIEW funcionario_servico AS 
SELECT f.nome_funcionario AS funcionario, a.data_agendamento AS DATA, s.nome_servico AS servico_realizado FROM funcionario f
INNER JOIN agendamento a ON a.id_funcionario = f.id_funcionario
INNER JOIN servico s ON s.id_servico = a.id_servico


SELECT * FROM pagamento_cliente

SELECT * FROM funcionario_servico