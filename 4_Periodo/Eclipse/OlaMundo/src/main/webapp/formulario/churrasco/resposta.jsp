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
		int homem = Integer.parseInt(request.getParameter("homem"));
		int mulher = Integer.parseInt(request.getParameter("mulher"));
		int crianca = Integer.parseInt(request.getParameter("crianca"));
		
		double carne = (homem * 0.300) + (mulher * 0.270) + (crianca * 0.250);
		double cerveja = (homem * 2) + (mulher * 1.5);
		double refrigerante = (homem * 0.3) + (mulher * 0.6) + (crianca * 1);
		
		if (homem > mulher){
			response.sendRedirect("erro.jsp");
		}
	%>
	
	<div>
		Quantidade que deverá ser comprado:
		<br/>
		Carne: <%=carne %>Kg;
		<br/>
		Cerveja: <%=cerveja %> litros;
		<br/>
		Refrigerante: <%=refrigerante %> litros;
	</div>
</body>
</html>