package DAO;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.LinkedList;

import javax.swing.JOptionPane;

import Conexao.ConectaBD;
import java.sql.SQLException;
import model.Livro;



public class LivroDAO {
    private ConectaBD conexao;
    //realizo a conexao com o banco de dados
    public LivroDAO(){
        conexao = new ConectaBD();
    }
    public PreparedStatement pst(String sql) throws SQLException{
        PreparedStatement pst = conexao.getConexaoBD().prepareStatement(sql);
        return pst;
    }
    //Inserir um novo livro
    public void inserir_livro(Livro livro){
        //comando do SQL
        String sql = "INSERT INTO livro (titulo, autor, ano_publicacao) values (?, ?, ?)";
        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, livro.getTitulo());
            pst.setString(2, livro.getAutor());
            pst.setInt(3, livro.getAnoPublicacao());
            //executa para o bd
            pst.execute();
            System.out.println("Livro inserido com sucesso!");
        } catch (Exception e) {
            System.out.println("Falha na inserção: " + e.getMessage());
        }
    }

    //Consultar todos os livro
    public LinkedList consultar_todos_livros(){
        //comando para o sql
        String sql = "SELECT * FROM livro";
        //cria uma LinkedList
        LinkedList<Livro> lista = new LinkedList<Livro>();
        try {
            PreparedStatement pst = pst(sql);
            //Execulta a consulta
            ResultSet resultados = pst.executeQuery();
            //loop enquanto tiver resultados no bd
            while (resultados.next()){
                //recupera os dados do bd
                String titulo = resultados.getString("titulo");
                String autor = resultados.getString("autor");
                int ano = resultados.getInt("ano_publicacao");
                int id = resultados.getInt("id_livro");
                //cria o obj Livro
                Livro livro = new Livro(titulo);
                livro.setAutor(autor);
                livro.setAnoPublicacao(ano);
                livro.setIdLivro(id);
                //adiciona o Livro na lista
                lista.add(livro);
            }
            return lista;
        } catch (Exception e) {
            System.out.println("Falha na consulta do livro: " + e.getMessage());
        }
        return null;
    }

    //Consulta livro passando o ID
    public Livro consultar_livro(int id){
        //Comando do sql
        String sql = "Select * from livro WHERE id_livro = ?";       
        try {
            PreparedStatement pst = pst(sql);
            //executar a consulta
            pst.setInt(1, id);
            ResultSet resultado = pst.executeQuery();

            //pega os dados se achar o registro no bd
            if (resultado.next()){
                //pega os dados do bd
                String titulo = resultado.getString("titulo");
                String autor = resultado.getString("autor");
                int ano = resultado.getInt("ano_publicacao");

                //insere os dados no Livro
                Livro livro = new Livro(titulo);
                livro.setAnoPublicacao(ano);
                livro.setAutor(autor);
                livro.setIdLivro(id);

                return livro;
            }else{
                System.out.println("Não possui registro com o ID " + id);
            }
        } catch (Exception e) {
            System.out.println("Falha na consulta do livro: " + e.getMessage());
        }
        return null;
    }

    //Excluir livro por id
    public void excluir_livro(int id){
        EmprestimoDAO emprestimoDAO = new EmprestimoDAO();
        //cria o obj Livro com o id que deseja excluir
        Livro livro = consultar_livro(id);
        //Comando sql
        String sql = "DELETE FROM livro WHERE id_livro = ?";

        try {
            //verifica se o id exesto no bd
            if (livro.getIdLivro() == id){
                PreparedStatement pst = pst(sql);
                pst.setInt(1, id);
                boolean verificar = emprestimoDAO.verificar_emprestimo_livro(id);
                if (verificar == true){
                    JOptionPane.showMessageDialog(null, "Livro excluido com sucesso");
                    pst.execute();
                }
                else{
                    JOptionPane.showMessageDialog(null, "Não é possivel excluir livro com emprestimo cadastrado, primeiro exclua o emprestimo");
                }
                
                
            }else{
                //se o id nao for estiver no bd
                System.out.println(id + " não está cadastrado.");
            }
        } catch (Exception e) {
            System.out.println("Falha na consulta do livro: "+ e.getMessage());
        }
    }

    //listar livros 
    public StringBuilder exibir_livros(LinkedList<Livro> livro){
         //public void exibirEmprestimos(LinkedList<Emprestimo> lista) {
        StringBuilder sb = new StringBuilder();
        for (Livro liv : livro) {
            sb.append("ID Livro: ").append(liv.getIdLivro()).append(" | ")
            .append("Título: ").append(liv.getTitulo()).append(" | ")
            .append("Autor: ").append(liv.getAutor()).append(" | ")
            .append("Ano Publicação: ").append(liv.getAnoPublicacao()).append("\n"); 
        }
        return sb;
    }

    //alterar todos dados do livro
    public void alterar_livro(int id, Livro livro){
        //comando sql
        String sql = "UPDATE livro set titulo = ? , autor = ? , ano_publicacao = ? WHERE id_livro = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, livro.getTitulo());
            pst.setString(2, livro.getAutor());
            pst.setInt(3, livro.getAnoPublicacao());
            pst.setInt(4, id);

            pst.execute();
            System.out.println("Livro atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de livro: " + e.getMessage());
        }
    }
    //alterar titulo do livro
    public void alterar_titulo(int id, String titulo){      
        //deixando o titulo maiusculo
        titulo = titulo.toUpperCase();
        //comando sql
        String sql = "UPDATE livro set titulo = ?  WHERE id_livro = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, titulo);
            pst.setInt(2, id);

            pst.execute();
            System.out.println("Livro atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de livro: " + e.getMessage());
        }
    }

    //alterar autor do livro
    public void alterar_autor(int id, String autor){
        //comando sql
        String sql = "UPDATE livro set autor = ?  WHERE id_livro = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, autor);
            pst.setInt(2, id);

            pst.execute();
            System.out.println("Livro atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de livro: " + e.getMessage());
        }
    }

    //alterar autor do livro
    public void alterar_ano(int id, int ano){
        //comando sql
        String sql = "UPDATE livro set ano_publicacao = ?  WHERE id_livro = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setInt(1, ano);
            pst.setInt(2, id);

            pst.execute();
            System.out.println("Livro atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de livro: " + e.getMessage());
        }
    }
}
