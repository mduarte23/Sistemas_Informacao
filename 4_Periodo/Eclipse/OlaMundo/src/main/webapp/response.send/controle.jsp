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
		String usuario= request.getParameter("usuario");
		String senha = request.getParameter("senha");
		
		if ((usuario.equals("marcelo")) && (senha.equals("123"))){
			response.sendRedirect("usuarioMarcelo.jsp");
		}else if ((usuario.equals("roberval")) && (senha.equals("123"))){
			response.sendRedirect("usuarioRoberval.jsp");
		}else{
			response.sendRedirect("invalido.jsp");
		}
	%>

</body>
</html>