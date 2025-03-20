<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>Tela de login</h1>
	<form action = "controle.jsp" method= "post">
		Usuario:
		<input type = "text" name="usuario"/>
		<br/>
		Senha:
		<input type = "password" name="senha"/>
		<br/>
		<input type="submit" value = "ok"/>
	</form>

</body>
</html>