public class Livro {
    private int id;
    private String titulo;
    private String autor;
    private String anoPublicacao;
    private static int contador = 0;
    
    public Livro(String titulo){
        this.setTitulo(titulo);
        contador ++;
        this.setId(contador);
    }
    public void setId(int contador){
        this.id = contador;
    }

    private void setTitulo(String titulo){
        titulo = titulo.toUpperCase();
        this.titulo = titulo;
    }

    

    public String getTitulo(){
        return this.titulo;
    }

    public int getId(){
        return this.id;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public String getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setAnoPublicacao(String anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    //criar toString 
    public String toString(){
        return "ID: " + getId() + " Titulo: " + getTitulo() + " Autor: " + getAutor() + " Ano de publicação: " + getAnoPublicacao();
    }
    
}
