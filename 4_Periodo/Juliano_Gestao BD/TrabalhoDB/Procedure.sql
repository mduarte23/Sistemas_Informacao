DELIMITER $$
#procedure que calcula quantos agendamentos um cliente realizou
CREATE PROCEDURE calcular_agendamentos_cliente(IN id_cliente_param INT)
BEGIN
    SELECT 
        c.nome_cliente AS Cliente,
        COUNT(a.id_agendamento) AS Total_Agendamentos
    FROM 
        cliente c
    LEFT JOIN 
        agendamento a ON c.id_cliente = a.id_cliente
    WHERE 
        c.id_cliente = id_cliente_param
    GROUP BY 
        c.nome_cliente;
END $$

DELIMITER ;


