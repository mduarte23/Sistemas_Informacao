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
	<h1>Cadastro de Pessoas</h1>
	<a href="formulario.jsp?id=0">Novo</a>

	<table border="1">
		<th>id</th>
		<th>Nome</th>
		<th>Telefone</th>
		<th>Email</th>
		<th>Cidade</th>
		<th>Endereço</th>
		<th>CEP</th>
		
		<%
				ClienteDao dao = new ClienteDao();
											for (Cliente p : dao.listar()){
												out.print("<tr>");
												out.print("<td>" + p.getIdclientea() + "</td>");
												out.print("<td>" + p.getNome() + "</td>");
												out.print("<td>" + p.getTelefone() + "</td>");
												out.print("<td>" + p.getCPF() + "</td>");
												out.print("<td>" + p.getCidade() + "</td>");
												out.print("<td>" + p.getEndereco() + "</td>");
												out.print("<td>" + p.getCep() + "</td>");
												out.print("<td>");
												out.print("<a href='formulario.jsp?id=" + p.getIdclientea() + "'>Alterar</a>");
												out.print("<a href='excluir.jsp?id=" + p.getIdclientea() + "'>Excluir</a>");
												out.print("</tr>");
											}
				%>
	</table>
	<a href="index.jsp">Inicio</a>
</body>
</html>