package org.filmes;

import java.sql.Statement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.LinkedList;

import org.filmes.Conexao;
import org.filmes.Filme;


public class FilmeDao {
	
	public void salvar(Filme f) {
		if (f.getId_filme()>0) {
			alterar(f);
		}else {
			inserir(f);
		}
	}

	public void inserir(Filme f) {
		Conexao con = new Conexao();
		
		try {
			String sql= "INSERT INTO filme (nome, diretor, genero, ano, streaming)"
					+ " VALUES (?,?,?,?,?)";
			PreparedStatement prep =con.getConnection().prepareStatement(sql);	
			prep.setString(1, f.getNome());
			prep.setString(2, f.getDiretor());
			prep.setString(3, f.getGenero());
			prep.setString(4, f.getAno());
			prep.setString(5, f.getStreaming());
			prep.execute();
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		con.desconecta();
	}
	
	public LinkedList<Filme> listar() {
		LinkedList<Filme> lista = new LinkedList<Filme>();
		Conexao con = new Conexao();
		try {
			String sql = "SELECT * FROM filme ORDER BY nome";
			Statement sta = con.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			while (res.next()) {
				Filme f = new Filme();
				f.setId_filme(res.getInt("id_filme"));
				f.setNome(res.getString("nome"));
				f.setDiretor(res.getString("diretor"));
				f.setGenero(res.getString("genero"));
				f.setAno(res.getString("ano"));
				f.setStreaming(res.getString("streaming"));
				lista.add(f);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		con.desconecta();
		return lista;
		
	}
	
	public void alterar(Filme f) {
		Conexao con = new Conexao();
		try {
			String sql = "UPDATE filme SET nome = ?, diretor = ?, genero = ?,"
					+ " ano = ?, streaming = ? "
					+ "WHERE id_filme = ?";
			PreparedStatement prep = con.getConnection().prepareStatement(sql);
			prep.setString(1, f.getNome());
			prep.setString(2, f.getDiretor());
			prep.setString(3, f.getGenero());
			prep.setString(4, f.getAno());
			prep.setString(5, f.getStreaming());
			prep.setInt(6, f.getId_filme());
			prep.execute();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		con.desconecta();
	}
	
	public void excluir(Filme f) {
		Conexao con = new Conexao();
		try {
			String sql = "DELETE FROM filme"
					+ " WHERE id_filme = ?";
			PreparedStatement prep = con.getConnection().prepareStatement(sql);
			prep.setInt(1, f.getId_filme());
			prep.execute();
		} catch (Exception e) {
			e.printStackTrace();
		}
		con.desconecta();
	}
	
	public Filme consultar(int id) {
		Filme p = new Filme();
		Conexao con = new Conexao();
		try {
			String sql = "SELECT * FROM filme WHERE id_filme = "+ id;
			Statement sta = con.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			if (res.next()) {
				p.setId_filme(res.getInt("id_filme"));
				p.setNome(res.getString("nome"));
				p.setDiretor(res.getString("diretor"));
				p.setGenero(res.getString("diretor"));
				p.setAno(res.getString("ano"));
				p.setStreaming(res.getString("streaming")
						);
				
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		con.desconecta();
		return p;
	}
}
	
