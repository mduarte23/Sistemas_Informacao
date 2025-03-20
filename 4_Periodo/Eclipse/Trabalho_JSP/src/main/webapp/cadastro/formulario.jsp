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
<title>Formulario</title>
</head>
<body>

	<%
		int id_filme = Integer.parseInt(request.getParameter("id"));
		Filme f = new Filme();
		FilmeDao fdao = new FilmeDao();
		if (id_filme > 0){
			f = fdao.consultar(id_filme);
		}else{
			f.setNome("");
			f.setDiretor("");
			f.setGenero("");
			f.setAno("");
			f.setStreaming("");
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
					<a class="nav-link text-white active" href="formulario.jsp?id=0">Cadastrar Novo Filme</a>
				</li>
				<li class="nav-item"><a class="nav-link text-white" href="listar.jsp">Listar Filmes</a>
				</li>

			</ul>
		</div>
	</nav>
	
	<h1 class="text-center mt-5">Realizar Cadastro de Filmes</h1>
	
	<div class="container d-flex justify-content-center ">

		<form class="col-7" action="gravar.jsp" method="post">
			Nome: 
			<input type="hidden" name="id_filme" value="<%=f.getId_filme() %>" />
			
			<input class="form-control" type="text" name="nome" value="<%=f.getNome() %>"
				placeholder="Nome do filme" required> 
				<br /> 
				Diretor: 
				<input
				class="form-control" type="text" name="diretor" value="<%=f.getDiretor() %>"
				placeholder="Nome do diretor" required> 
				<br /> 
				Gênero: 
				<input
				class="form-control" type="text" name="genero" placeholder="Gênero" value="<%=f.getGenero() %>" required>

			<br /> Ano: <input class="form-control" type="number" value="${f.ano}" name="ano"
				placeholder="Ano de lançamento" required> <br /> Streaming <select
				class="form-control" name="streaming" required>
				<option>Netflix</option>
				<option>Amazon Prime</option>
				<option>Disney+</option>
				<option>Apple Tv+</option>
				<option>Paramount+</option>
				<option>Star+</option>
				<option>Outros</option>
			</select> <br />
			
			<div class="text-center">
    <button type="submit" class="btn btn-dark">Enviar</button>
</div>
		</form>
	</div>
</body>
</html>