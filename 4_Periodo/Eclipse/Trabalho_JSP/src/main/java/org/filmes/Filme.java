package org.filmes;

public class Filme {
	private int id_filme;
	private String nome;
	private String diretor;
	private String genero;
	private String ano;
	private String streaming;
	
	public int getId_filme() {
		return id_filme;
	}
	public void setId_filme(int id_filme) {
		this.id_filme = id_filme;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getDiretor() {
		return diretor;
	}
	public void setDiretor(String diretor) {
		this.diretor = diretor;
	}
	public String getGenero() {
		return genero;
	}
	public void setGenero(String genero) {
		this.genero = genero;
	}
	public String getAno() {
		return ano;
	}
	public void setAno(String ano) {
		this.ano = ano;
	}
	public String getStreaming() {
		return streaming;
	}
	public void setStreaming(String streaming) {
		this.streaming = streaming;
	}
	@Override
	public String toString() {
		return "";
	}
	
	
	
}
