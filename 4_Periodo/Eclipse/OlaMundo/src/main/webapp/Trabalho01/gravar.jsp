<%@page import="org.libertas.Cliente"%>
<%@page import="org.libertas.ClienteDao"%>
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
		ClienteDao dao = new ClienteDao();
				Cliente p = new Cliente();
				p.setIdcliente(Integer.parseInt(request.getParameter("idpessoa")));
				p.setNome(request.getParameter("nome"));
				p.setTelefone(request.getParameter("telefone"));
				p.setEmail(request.getParameter("email"));
				p.setCidade(request.getParameter("cidade"));
				p.setEndereco(request.getParameter("endereco"));
				p.setCep(request.getParameter("cep"));
				
				//salva a pessoa
				if (p.getIdclientea()>0){
			dao.alterar(p);
				}else{
			dao.inserir(p);
				}
		%>
	<h1>Pessoa salva com sucesso</h1>
	<a href="index.jsp">Inicio</a>
	
</body>
</html>