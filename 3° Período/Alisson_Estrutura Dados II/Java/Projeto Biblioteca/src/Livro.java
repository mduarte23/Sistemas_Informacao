public class Livro {
    //static String getContador;
    private int id;
    private String titulo;
    private String autor;
    private int anoPublicacao;
    //private static int contador = 0;
    
    public Livro(String titulo){
        this.setTitulo(titulo);
        //contador ++;
        this.setId(id);
    }
    public void setId(int id){
        this.id = id;
    }

    private void setTitulo(String titulo){
        titulo = titulo.toUpperCase();
        this.titulo = titulo;
    }

    public int getContador(){
        return  this.id;
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

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setAnoPublicacao(int anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    //criar toString 
    public String toString(){
        return "ID: " + getId() + " Titulo: " + getTitulo() + " Autor: " + getAutor() + " Ano de publicação: " + getAnoPublicacao();
    }
    
}
