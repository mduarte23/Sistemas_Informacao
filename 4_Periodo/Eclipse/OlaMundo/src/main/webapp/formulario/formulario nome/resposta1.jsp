<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Exemplo JSP</title>
</head>
<body>
<%
    String anoString = request.getParameter("ano");
    Integer anoNascimento = Integer.parseInt(anoString);
    int idade = 2024 - anoNascimento;
%>
<div>
    Você nasceu no ano de <%= anoNascimento %> e tem <%= idade %> anos de idade.
</div>
</body>
</html>