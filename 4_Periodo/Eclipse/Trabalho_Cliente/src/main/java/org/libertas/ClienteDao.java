package org.libertas;

import java.sql.Statement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.LinkedList;

public class ClienteDao {
	//private static LinkedList<Pessoa> lista = new LinkedList<Pessoa>();
	
	public void salvar(Cliente c) {
		if (c.getIdcliente()>0) {
			alterar(c);
		}else {
			inserir(c);
		}
	}
	
	public Retorno inserir(Cliente c) {
		//lista.add(p);
		//abre a conexao com o bd
		Conexao con = new Conexao();
		
		RetornoDao retornoDao = new RetornoDao();
		try {
			String sql = "INSERT INTO cliente (nome, telefone, cpf, cidade, endereco, cep)"
					+ " VALUES (?,?,?,?,?,?)";
			PreparedStatement prep = con.getConnection().prepareStatement(sql);
			prep.setString(1,  c.getNome());
			prep.setString(2,  c.getTelefone());
			prep.setString(3,  c.getCPF());
			prep.setString(4,  c.getCidade());
			prep.setString(5,  c.getEndereco());
			prep.setString(6,  c.getCep());
			prep.execute();
			
			String mensagem = "Inserido com sucesso!";
			Boolean resposta = true;
			
			Retorno retorno = retornoDao.RetornoJson(resposta, mensagem);
			
			//fecha a conexao com o banco de dados 
			con.desconecta();
			return retorno;
			
			
		} catch (Exception e) {
			e.printStackTrace();
			//fecha a conexao com o banco de dados 
			con.desconecta();
			String mensagem = "Falha ao inserir!";
			Boolean resposta = false;
			
			Retorno retorno = retornoDao.RetornoJson(resposta, mensagem);
			
			return retorno;
		}
	}
	public LinkedList<Cliente> listar(String pesquisa) {
		//return lista;
		LinkedList<Cliente> lista = new LinkedList<Cliente>();
		Conexao con = new Conexao();
		try {
			String sql = "SELECT * FROM cliente "
					+ "WHERE nome like ? "
					+ "ORDER BY nome";
			PreparedStatement sta = con.getConnection().prepareStatement(sql);
			sta.setString(1,  "%" + pesquisa + "%");
			
			ResultSet res = sta.executeQuery();
			while (res.next()) {
				Cliente p = new Cliente();
				p.setIdcliente(res.getInt("id_cliente"));
				p.setNome(res.getString("nome"));
				p.setTelefone(res.getString("telefone"));
				p.setCPF(res.getString("cpf"));
				p.setCidade(res.getString("cidade"));
				p.setEndereco(res.getString("endereco"));
				p.setCep(res.getString("cep"));
				lista.add(p);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		con.desconecta();
		return lista;
	}
	
	public Retorno alterar(Cliente c) {
		Conexao con = new Conexao();
		
		RetornoDao retornoDao = new RetornoDao();
		
		try {
			String sql = "UPDATE cliente SET "
					+"nome = ?, telefone = ?, " 
					+ "cpf = ? , cidade = ?, "
					+ "endereco = ? , cep = ? "
					+ "WHERE id_cliente = ?";
			PreparedStatement prep = con.getConnection().prepareStatement(sql);
			prep.setString(1, c.getNome());
			prep.setString(2, c.getTelefone());
			prep.setString(3, c.getCPF());
			prep.setString(4, c.getCidade());
			prep.setString(5, c.getEndereco());
			prep.setString(6, c.getCep());
			prep.setInt(7, c.getIdcliente());
			prep.execute();
			
			String mensagem = "Alterado com sucesso!";
			Boolean resposta = true;
			
			Retorno retorno = retornoDao.RetornoJson(resposta, mensagem);
			
			//fecha a conexao com o banco de dados 
			con.desconecta();
			return retorno;
			
		} catch (Exception e) {
			e.printStackTrace();
			String mensagem = "Falha ao alterar!";
			Boolean resposta = false;
			
			Retorno retorno = retornoDao.RetornoJson(resposta, mensagem);
			
			//fecha a conexao com o banco de dados 
			con.desconecta();
			
			return retorno;
		}
		
	}
	public Retorno excluir(Cliente c) {
		Conexao con = new Conexao();
		
		RetornoDao retornoDao = new RetornoDao();
		
		try {
			String sql = "DELETE FROM cliente"
					+ " WHERE id_cliente = ?";
			PreparedStatement prep = con.getConnection().prepareStatement(sql);
			prep.setInt(1, c.getIdcliente());
			prep.execute();
			
			String mensagem = "Excluido com sucesso!";
			Boolean resposta = true;
			
			Retorno retorno = retornoDao.RetornoJson(resposta, mensagem);
			
			//fecha a conexao com o banco de dados 
			con.desconecta();
			return retorno;
		} catch (Exception e) {
			e.printStackTrace();
			
			String mensagem = "Falha ao excluir!";
			Boolean resposta = false;
			
			Retorno retorno = retornoDao.RetornoJson(resposta, mensagem);
			
			//fecha a conexao com o banco de dados 
			con.desconecta();
			
			return retorno;
		}
		
	}
	
	public Cliente consultar(int id) {
		Cliente p = new Cliente();
		Conexao con = new Conexao();
		try {
			String sql = "SELECT * FROM cliente WHERE id_cliente = "+ id;
			Statement sta = con.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			if (res.next()) {
				p.setIdcliente(res.getInt("id_cliente"));
				p.setNome(res.getString("nome"));
				p.setTelefone(res.getString("telefone"));
				p.setCPF(res.getString("cpf"));
				p.setCidade(res.getString("cidade"));
				p.setEndereco(res.getString("endereco"));
				p.setCep(res.getString("cep"));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		con.desconecta();
		return p;
	}
}
