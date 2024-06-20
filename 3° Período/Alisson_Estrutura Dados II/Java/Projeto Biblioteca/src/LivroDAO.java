import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.LinkedList;

public class LivroDAO {
    private ConectaDB conexao;

    public LivroDAO(){
        conexao = new ConectaDB();
    }
    public void inserir(Livro livro){
        //ConectaDB conexao = new ConectaDB();
        String sql = "INSERT INTO livro(titulo, autor, ano) values(?, ?, ?)";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setString(1, livro.getTitulo());
            pst.setString(2, livro.getAutor());
            pst.setInt(3, livro.getAnoPublicacao());
            pst.execute();
            System.out.println("Insercao ok: "+ livro);
        } catch (Exception e) {
            System.out.println("Falha na inserção: "+ e.getMessage());
        }
    }

    public LinkedList<Livro> consultarTodos(){
        //ConectaDB conexao = new ConectaDB();
        String sql = "SELECT * FROM livro";
        LinkedList<Livro> lista = new LinkedList<Livro>();
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            //executar consulta
            ResultSet resultados = pst.executeQuery();
            //System.out.println(resultados);
            while (resultados.next()){
                //recupera dados do banco
                String titulo = resultados.getString("titulo");
                String autor = resultados.getString("autor");
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

    //implementar consulta por ID
    public Livro consultar (int id){
        //ConectaDB conexao = new ConectaDB();
        String sql = "SELECT * FROM livro WHERE id_livro = ?";
        //cria o obj mais nao seta nenhum valor
        Livro lista = null;
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            //executar consulta
            pst.setInt(1, id);
            ResultSet resultados = pst.executeQuery();

            //pegando os dados
            if (resultados.next()){ //se achar o registro no banco
                String titulo = resultados.getString("titulo");
                String autor = resultados.getString("autor");
                int ano = resultados.getInt("ano");
                int id_livro = resultados.getInt("id_livro");

                Livro livro = new Livro(titulo);
                
                livro.setAnoPublicacao(ano);
                livro.setAutor(autor);
                livro.setId(id_livro);
                return livro;
            }else{
                System.out.println("Não possui registro com o ID "+ id);
            }

        } catch (Exception e) {
            System.out.println("Falha na consulta: "+ e.getMessage());
        }
        return null;
    }

    //implementar excluir por id
    public void excluir(int id){
        //cria o obj Livro com o id que deseja excluir
        Livro liv = consultar(id);
        String sql = "DELETE FROM livro WHERE id_livro = ?";  
        
        try {
            //verifica se o id existe no BD
            if (liv.getId() == id){
                PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
                pst.setInt(1, id);
                
                System.out.println("Livro excluido com sucesso");
                pst.execute();
            }else{
                System.out.println(id + " não está cadastrado");
            }
        } catch (Exception e) {
            System.out.println("Falha na consulta livro: "+ e.getMessage());
        }
        
    }


    //implementar alterar
    //passar o livro com valores atulizados ja
    public void alterar(Livro livro, int id){
        String sql = "UPDATE livro SET titulo = ?, autor = ?, ano = ? WHERE id_livro = ?";
        try{
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setString(1, livro.getTitulo());
            pst.setString(2, livro.getAutor());
            pst.setInt(3, livro.getAnoPublicacao());
            pst.setInt(4, id);
            pst.execute();

            System.out.println("Livro atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta do livro: "+ e.getMessage());
        }
    }
}
