
<%@page import="java.text.DecimalFormat" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>Calculo de juros</h1>
	<h3>Valor Depositado = R$1000,00</h3>
	<%
		int meses = 12 * 5;
		double deposito = 1000;
		double juros = 0.7 / 100;
		for (int i = 1; i <= meses; i++){
			double valor_juros = deposito * juros;
			deposito = deposito + valor_juros;
		}
		DecimalFormat df = new DecimalFormat("#.00");
        
        
        out.print("<div>");
		out.print("Valor após 5 anos com juros de 0,7% a.m. R$"+df.format(deposito));
		out.print("</div>");
		
	%>

</body>
</html>