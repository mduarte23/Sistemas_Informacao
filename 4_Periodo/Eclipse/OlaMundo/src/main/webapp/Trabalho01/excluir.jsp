<%@page import="org.libertas.ClienteDao"%>
<%@page import="org.libertas.Cliente"%>
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
		//declare um objeto Pessoa
				Cliente p = new Cliente();
				//receba o parametro id e atribua no objeto pessoa o valor do id pessoa
				p.setIdcliente(Integer.parseInt(request.getParameter("id")));
				
				//declare o PessoaDao
				ClienteDao pdao = new ClienteDao();
				//execute o metodo excluir
				pdao.excluir(p);
				
			
			
				//adicione um link pra voltar para pagina lista.jsp
		%>
	<div>Pessoa excluida com sucesso</div>
	<a href="index.jsp">Inicio </a>
	
</body>
</html>