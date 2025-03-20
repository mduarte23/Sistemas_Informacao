<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<jsp:useBean id="pdao" scope="page" class="org.libertas.ClienteDao" />
	
	<a href="formulario.jsp?idpessoa=0">Novo</a>
	<table border="1" width="100%">
		<th>Nome</th>
		<th>Telefone</th>
		<th>E-mail</th>
		<th>Cidade</th>
		<th>Endereço</th>
		<th>CEP</th>
		
		<c:forEach var="p" items="${pdao.listar()}">
			<tr>
				<td>${p.nome}</td>
				<td>${p.telefone}</td>
				<td>${p.email}</td>
				<td>${p.cidade}</td>
				<td>${p.endereco}</td>
				<td>${p.cep}</td>
				<td>
					<a href="formulario.jsp?idpessoa=${p.idpessoa}">alterar</a>
					<a href="excluir.jsp?idpessoa=${p.idpessoa}">excluir</a>
				
				</td>
			</tr>
		</c:forEach>
		
	</table>

</body>
</html>