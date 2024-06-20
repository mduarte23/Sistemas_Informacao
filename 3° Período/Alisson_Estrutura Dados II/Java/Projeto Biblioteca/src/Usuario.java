public class Usuario {
    //static String getContadorUsuario;
    private int idUsuario;
    private String nome;
    private String email;
    //private static int contadorUsuario = 0;
    
    public Usuario(String nome){
        this.setUsuario(nome);
        //contadorUsuario ++;
        //this.setId_Usuario(contadorUsuario);
    }
    public void setId_Usuario(int idUsuario){
        this.idUsuario = idUsuario;
    }

    private void setUsuario(String nome){
        nome = nome.toUpperCase();
        this.nome = nome;
    }

    public int getContador_Usuario(){
        return  this.idUsuario;
    }
    

    public String getUsuario(){
        return this.nome;
    }

    public int getId_Usuario(){
        System.out.println(idUsuario);
        return this.idUsuario;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getEmail(){
        return this.email;
    }

    //criar toString 
    public String toString(){
        return "ID: " + getId_Usuario() + " Nome: " + getUsuario() + " Email: " + getEmail();
    }
}
