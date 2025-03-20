<%@page import="org.filmes.Filme"%>
<%@page import="org.filmes.FilmeDao"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet"
	href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
	integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
	crossorigin="anonymous">
<title>Filmes</title>
</head>
<body>

	<%
		Filme f = new Filme();
		FilmeDao fdao = new FilmeDao();
		String idFilmeStr = request.getParameter("id_filme");

	    // Verifica se o id_filme é válido
	    if (idFilmeStr != null && !idFilmeStr.isEmpty()) {
	        f.setId_filme(Integer.parseInt(idFilmeStr));
	    }
		
		
		f.setNome(request.getParameter("nome"));
		f.setDiretor(request.getParameter("diretor"));
		f.setGenero(request.getParameter("genero"));
		f.setAno(request.getParameter("ano"));
		f.setStreaming(request.getParameter("streaming"));
		
		if (f.getId_filme()>0){
			fdao.alterar(f);
		}else{
			fdao.inserir(f);
		}
	%>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
		<a class="navbar-brand" href="index.jsp"> <img class="logo"
			src="img/logo.webp" alt="Logo" style="width: 70px; heigth: auto;">
		</a>
		<button class="navbar-toggler" type="button" data-toggle="collapse"
			data-target="#navbarNav" aria-controls="navbarNav"
			aria-expanded="false" aria-label="Alterna navegação">
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse" id="navbarNav">
			<ul class="nav nav-pills nav-fill">
				<li class="nav-item">
					<a class="nav-link text-white " href="index.jsp">Home</a>
				</li>
				<li  class="nav-item">
					<a class="nav-link text-white " href="formulario.jsp?id=0">Cadastrar Novo Filme</a>
				</li>
				<li class="nav-item"><a class="nav-link text-white" href="listar.jsp">Listar Filmes</a>
				</li>

			</ul>
		</div>
	</nav>
	
	<h1 class="text-center mt-5">Filme salvo com sucesso</h1>
	<br/>
	
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
		integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
		crossorigin="anonymous"></script>
	<script
		src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
		integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
		crossorigin="anonymous"></script>
	<script
		src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
		integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
		crossorigin="anonymous"></script>

</body>
</html>