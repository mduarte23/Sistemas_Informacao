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
					<a class="nav-link text-white active" href="index.jsp">Home</a>
				</li>
				<li  class="nav-item">
					<a class="nav-link text-white" href="formulario.jsp?id=0">Cadastrar Novo Filme</a>
				</li>
				<li class="nav-item"><a class="nav-link text-white" href="listar.jsp">Listar Filmes</a>
				</li>

			</ul>
		</div>
	</nav>

	
	
	<h1 class="text-center mt-5">Cadastro de Filmes</h1>
	
	<div class="text-center mt-5">
	<button type="button" class="btn btn-dark mr-5">
		<a class="btn btn-dark" href="formulario.jsp?id=0">Cadastro de Filme</a>
	</button>
	<button type="button" class="btn btn-dark ml-7">
	<a class="btn btn-dark" href="listar.jsp?id=0">Listar Filmes</a>
	</button>
	
	</div>
	
	


	
	
	
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