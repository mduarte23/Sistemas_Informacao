package model;

public class Emprestimo {
    private int idEmprestimo;
    private int idLivro;
    private int idUsuario;
    private String dataEmprestimo;
    private boolean emprestimo;
    private String dataDevolucao;
    //cria o Obj Emprestimo passando o id do livro
    public Emprestimo(int id_livro){
        this.setIdLivro(id_livro);
    }
    //seta a data de devolucao
    public void setDevolucao(String devolucao) {
        this.dataDevolucao = devolucao;
    }
    //retorna a data de devolucao
    public String getDevolucao(){
        return dataDevolucao;
    }
    //retorna se o emprestimo é verdadeirro ou falso
    public boolean isEmprestimo() {
        return emprestimo;
    }
    //seta o emprestimo
    public void setEmprestimo(boolean emprestimo) {
        this.emprestimo = emprestimo;
    }
    //retorna o id do emprestimo
    public int getIdEmprestimo() {
        return idEmprestimo;
    }
    //seta o id do emprestimo
    public void setIdEmprestimo(int idEmprestimo) {
        this.idEmprestimo = idEmprestimo;
    }
    //retorna o id do livro
    public int getIdLivro() {
        return idLivro;
    }
    //seta o id do livro
    private void setIdLivro(int idLivro) {
        this.idLivro = idLivro;    
    }
    //retorna o id do usuario
    public int getIdUsuario() {
        return idUsuario;
    }
    //seta o id do usuario
    public void setIdUsuario(int idUsuario) {
        this.idUsuario = idUsuario;
    }
    //retorna a data de emprestimo
    public String getDataEmprestimo() {
        return dataEmprestimo;
    }
    //seta a data de emprestimo
    public void setDataEmprestimo(String dataEmprestimo) {
        this.dataEmprestimo = dataEmprestimo;
    }

    
}

