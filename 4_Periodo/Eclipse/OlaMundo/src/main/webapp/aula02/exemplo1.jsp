<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%@include file="menu.jsp" %>
	<%!
		//declaracao tem !
		public double media(double a, double b){
			return (a+b)/2;
	}
	%>


	<%
		int a = 1;
		int b = 2;
		int c = a + b;
	%>
	<div style= "font-size: 100px">
		
		<%= c 
		// precisa do = para chamar funcao
		%>
		<br/>
		<%= media(a,b) %>
	</div>

</body>
</html>