import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.LinkedList;
public class UsuarioDao{
    private ConectaDB conexao;

    public UsuarioDao(){
        conexao = new ConectaDB();
    }

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


    public LinkedList<Livro> consultarTodosUsuarios(){
        String sql = "SELECT * FROM usuario";
        LinkedList<Usuario> lista = new LinkedList<Usuario>();
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            //executar consulta
            ResultSet resultados = pst.executeQuery();
            //System.out.println(resultados);
            while (resultados.next()){
                //recupera dados do banco
                String nome = resultados.getString("nome");
                String email = resultados.getString("email");
                int ano = resultados.getInt("ano");
                int id = resultados.getInt("id_livro");
                //cria o obj java
                Livro obj = new Livro(titulo);
                obj.setAutor(autor);
                obj.setAnoPublicacao(ano);
                obj.setId(id);
                //adicionando o obj Livro na lista
                lista.add(obj);
            }
            return lista;
        } catch (Exception e) {
            System.out.println("Falha na consulta livro: "+ e.getMessage());
        }
        return null;
    }
}
