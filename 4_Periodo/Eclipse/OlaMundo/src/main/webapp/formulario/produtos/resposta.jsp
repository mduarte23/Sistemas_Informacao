<%@page import="java.text.DecimalFormat"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	
	<%
		double preco = Double.parseDouble(request.getParameter("valor_dolar"));
		String descricao = request.getParameter("descricao");
		double quantidade = Double.parseDouble(request.getParameter("quantidade"));
		double dolar = 5;
		
		double preco_reais = preco * dolar;
		double total_reais = preco_reais * quantidade;
		
		DecimalFormat df = new DecimalFormat("###,##0.00");
		
		
	%>
	
	<div>
		Você comprou uma <%= descricao %> no valor unitário de R$<%=df.format(preco_reais)%>.
		<br/>
		A quantidade total comprada foi <%=quantidade %>, e ficou o valor total de R$<%=df.format(total_reais) %>
	</div>
	
	
</body>
</html>