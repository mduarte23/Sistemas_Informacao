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

	<!--  scope é onde a aplicacao vai funcionar -->
	<jsp:useBean id="p" scope="page" class="org.libertas.Cliente"/>
	<jsp:useBean id="pdao" scope="page" class="org.libertas.ClienteDao"/>
	<!-- 	Tudo isso pode ser substituido quando property e param sao iguais
	<jsp:setProperty property="nome" name="p" param="nome"/>
	<jsp:setProperty property="telefone" name="p" param="telefone"/>
	<jsp:setProperty property="email" name="p" param="email"/>
	<jsp:setProperty property="cidade" name="p" param="cidade"/>
	 -->
	
	<jsp:setProperty property="*" name="p"/>
	<% pdao.salvar(p); %>
	
	Registro salvo com sucesso!
	<br/>
	<a href="index.jsp">OK</a>
	
</body>
</html>