<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<!-- Faça uma pagina JSP que receba o nome de 2 times de futebol e quantos gols cada um fez. Na página de resposta mostre qual time foi campeao,
	 ou se houve empate -->
	<h1>Times de futebol</h1>
	
	<form action="resposta.jsp" method="post">
		Time 1: 
		<input type= "text" name = "time1"/>
		<br/>
		Quantidade de gols time 1:
		<input type= "text" name = "gol1"/>
		<br/>
		Time 2: 
		<input type= "text" name = "time2"/>
		<br/>
		Quantidade de gols time 2:
		<input type= "text" name = "gol2"/>
		<br/>
		<input type="submit" value= "ok"/>
	</form>
</body>
</html>