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
		String time1 = request.getParameter("time1");
		int gol1 = Integer.parseInt(request.getParameter("gol1"));
		
		String time2 = request.getParameter("time2");
		int gol2 = Integer.parseInt(request.getParameter("gol2"));
		
		String campeao;
			
		if (gol1 > gol2){
			campeao = time1;
			out.print("O campeao foi " + campeao);
		}else if (gol1 < gol2){
			campeao = time2;
			out.print("O campeao foi " + campeao);
		}else{
			campeao = "empate";
			out.print("O resultado foi "+ campeao);
		}
	%>
	
	
</body>
</html>