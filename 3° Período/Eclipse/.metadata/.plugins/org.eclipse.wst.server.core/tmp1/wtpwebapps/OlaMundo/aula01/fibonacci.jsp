<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>Sequencia de Fibonacci</h1>
	<%
		int numero1 = 1;
		int numero2 = 1;
		int soma;
		for (int i = 1; i <= 20; i++){
			soma = numero1 + numero2;
			out.print(numero1 + " ");
			
			
			numero1 = numero2;
			numero2 = soma;
			
			
		}
	%>

</body>
</html>