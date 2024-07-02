package model;

public class Livro {
    private int idLivro;
    private String titulo;
    private String autor;
    private int anoPublicacao;

    //cria o Livro passando titulo como parametro
    public Livro(String titulo){
        this.setTitulo(titulo);   
    }
    //retorna o id do livro
    public int getIdLivro() {
        return idLivro;
    }
    //seta o id do livro
    public void setIdLivro(int id_Livro) {
        this.idLivro = id_Livro;
    }
    //retorna o titulo do livro
    public String getTitulo() {
        return titulo;
    }
    //seta o titulo do livro
    private void setTitulo(String titulo) {
        titulo = titulo.toUpperCase();
        this.titulo = titulo;
    }
    //retorna o nome do autor
    public String getAutor() {
        return autor;
    }
    //seta o nome do autor
    public void setAutor(String autor) {
        this.autor = autor;
    }
    //retorna o ano de publicaçao 
    public int getAnoPublicacao() {
        return anoPublicacao;
    }
    //seta o ano de publicacao
    public void setAnoPublicacao(int anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    //criando toString
    public String toString(){
        return "ID: " + getIdLivro() + " Título: " + getTitulo() + " Autor: " + getAutor() + " Ano de publicação: " + getAnoPublicacao();
    }

    
}
