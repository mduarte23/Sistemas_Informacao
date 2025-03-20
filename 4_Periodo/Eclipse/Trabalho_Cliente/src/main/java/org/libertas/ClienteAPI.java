package org.libertas;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.stream.Collectors;

import com.google.gson.Gson;

/**
 * Servlet implementation class ClienteAPI
 */
@WebServlet("/ClienteAPI/*")
public class ClienteAPI extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ClienteAPI() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		ClienteDao cdao = new ClienteDao();
		Gson gson = new Gson();
		
		int id = 0;
		try {
			//pega o id passado por parametro 
			id = Integer.parseInt(request.getPathInfo().substring(1));
			
		} catch (Exception e) {
			// TODO: handle exception
		}
				
		String pesquisa = request.getParameter("pesquisa");
		
		String resposta;
		if (id==0) {
			//listar todos
			resposta = gson.toJson(cdao.listar(pesquisa));
		} else {
			//consultar apenas 1
			resposta = gson.toJson(cdao.consultar(id));
		}
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//pega o body da request
		String body = request.getReader().lines().collect(Collectors.joining(System.lineSeparator()));
		
		//converte o body para um objeto Java
		Gson gson = new Gson();
		Cliente c = gson.fromJson(body,  Cliente.class);
		
		//salva o novo cliente
		ClienteDao cdao = new ClienteDao();
//		pdao.inserir(p);
		
		
		
		//envia a resposta
		String resposta = gson.toJson(cdao.inserir(c));
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);
	}
	
	protected void doPut(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//pega o body da request
		String body = request.getReader().lines().collect(Collectors.joining(System.lineSeparator()));
		
		//converte o body para um objeto Java
		Gson gson = new Gson();
		Cliente c = gson.fromJson(body,  Cliente.class);
		
		//pega o id passado por parametro
		int id = 0;
		try {
			id = Integer.parseInt(request.getPathInfo().substring(1));
			
		} catch (Exception e) {
			// TODO: handle exception
		}
		c.setIdcliente(id);
		
		//salva o novo cliente
		ClienteDao cdao = new ClienteDao();
		cdao.alterar(c);
				
		
		//envia a resposta
		String resposta = gson.toJson(cdao.alterar(c));
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);		
		
		
	}
	
	
	protected void doDelete(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//pega o id passado por parametro
		int id = 0;
		try {
			id = Integer.parseInt(request.getPathInfo().substring(1));
					
		} catch (Exception e) {
			// TODO: handle exception
		}
		
		//exclui a nova pessoa
		ClienteDao cdao = new ClienteDao();
		Cliente c = new Cliente();
		Gson gson = new Gson();
		c.setIdcliente(id);
		//cdao.excluir(c);
		
		//evia resposta
		
		String resposta = gson.toJson(cdao.excluir(c));
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);	
	}

}
