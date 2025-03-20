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
	int idpessoa = Integer.parseInt(request.getParameter("id"));
		Cliente p = new Cliente();
		ClienteDao pdao = new ClienteDao();
		if (idpessoa > 0){
			p = pdao.consultar(idpessoa);
		} else {
			//limpa os dados para novo
			p.setNome("");
			p.setTelefone("");
			p.setEmail("");
			p.setCidade("");
			p.setEndereco("");
			p.setCep("");
		}
	%>

	<form action="gravar.jsp" method="post">
		<input type="hidden" name="idpessoa" value="<%=p.getIdclientea()%>" />
	
		Nome:
		<input type="text" name="nome" value="<%= p.getNome() %>"/>
		<br/>
		Telefone:
		<input type="text" name="telefone" value="<%= p.getTelefone() %>"/>
		<br/>
		Email:
		<input type="text" name= "email" value="<%= p.getTelefone() %>"/>
		<br/>
		Cidade:
		<input type="text" name="cidade" value="<%=p.getCPF()%>"/>
		<br/>
		Endereco:
		<input type="text" name="endereco" value="<%= p.getEndereco() %>"/>
		<br/>
		CEP:
		<input type="text" name="cep" value="<%= p.getCep() %>"/>
		<br/>
		<input type="submit" value="salvar"/>
	</form>

</body>
</html>