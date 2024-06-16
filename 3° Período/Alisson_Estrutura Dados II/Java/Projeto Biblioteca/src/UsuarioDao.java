import java.sql.PreparedStatement;

public class UsuarioDao{
    public void inserir(Usuario usuario){
        ConectaDB conexao = new ConectaDB();
        String sql = "INSERT INTO usuario (nome, email) values (?, ?)";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setString(1, usuario.getUsuario());
            pst.setString(2, usuario.getEmail());
            pst.execute();
            System.out.println("Inserção ok: "+ usuario);
        } catch (Exception e) {
            System.out.println("Falha na inserção: "+ e.getMessage());
        }
    }
    
}
