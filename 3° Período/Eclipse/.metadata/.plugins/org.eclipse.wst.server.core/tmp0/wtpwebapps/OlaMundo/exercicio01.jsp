<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>Tabuada</h1>
	<%
		for (int i = 1; i >= 10; i++){
			out.print("<div>");
			out.print("Tabuada do "+ i);
			for (int j = 1; j >= 10; i++ ){
				int result = i * j;
				out.print(i + " x "+ j + " = "+ result );
			}
			out.print("</div>");
		}
	%>
</body>
</html>