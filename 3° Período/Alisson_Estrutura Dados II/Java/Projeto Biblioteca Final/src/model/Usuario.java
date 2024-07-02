package model;

public class Usuario {
    private int idUsuario;
    private String nome;
    private String endereco;
    private String telefone;
    //cria o obj Usuario setando o nome
    public Usuario(String nome){
        this.setNome(nome);
    }
    //retorna o id do usuario
    public int getIdUsuario() {
        return idUsuario;
    }
    //seta o id do usuario
    public void setIdUsuario(int idUsuario) {
        this.idUsuario = idUsuario;
    }
    //retorna o nome
    public String getNome() {
        return nome;
    }
    //seta o nome
    private void setNome(String nome) {
        nome = nome.toUpperCase();
        this.nome = nome;
    }
    //retorna o endereco
    public String getEndereco() {
        return endereco;
    }
    //seta o endereco
    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
    //retorna o telefone
    public String getTelefone() {
        return telefone;
    }
    //seta o telefone
    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    //criando toString
    public String toString(){
        return "ID: " + getIdUsuario() + " Nome: " + getNome() + " Endereço: " + getEndereco() + " Telefone: " + getTelefone();
    }
    
}
