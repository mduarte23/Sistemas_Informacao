package DAO;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.LinkedList;

import Conexao.ConectaBD;
import javax.swing.JOptionPane;
import model.Livro;
import model.Usuario;
public class UsuarioDAO {
    private ConectaBD conexao;

    public UsuarioDAO(){
        conexao = new ConectaBD();
    }

    public PreparedStatement pst(String sql) throws SQLException{
        PreparedStatement pst = conexao.getConexaoBD().prepareStatement(sql);
        return pst;
    }

    //Inserir um novo cliente
    public void inserir_usuario( Usuario usuario){
        //comando sql
        String sql = "INSERT INTO usuario (nome, endereco, telefone) values (?, ?, ?)";
        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, usuario.getNome());
            pst.setString(2, usuario.getEndereco());
            pst.setString(3, usuario.getTelefone());
            //executar o comando
            pst.execute();
            System.out.println("Usuário adicionado com sucesso");
        } catch (Exception e) {
            System.out.println("Falha na inserção do usuario: " + e.getMessage());
        }
    }

    //Consultar todos Clientes
    public LinkedList<Usuario> consultar_todos_usuarios(){
        //comando sql
        String sql = "SELECT * FROM usuario";
        //Cria uma LinkedList
        LinkedList<Usuario> lista = new LinkedList<Usuario>()
;
        try {
            PreparedStatement pst = pst(sql);
            ResultSet resultados = pst.executeQuery();
            //loop enquanto tiver dados
            while (resultados.next()){
                //recupera os dados do bd
                String nome = resultados.getString("nome");
                String endereco = resultados.getString("endereco");
                String telefone = resultados.getString("telefone");
                int id = resultados.getInt("id_usuario");

                //cria o obj Usuario
                Usuario usuario = new Usuario(nome);
                usuario.setEndereco(endereco);
                usuario.setTelefone(telefone);
                usuario.setIdUsuario(id);

                //adicionando o obj Usuario na lista
                lista.add(usuario);
            }
            return lista;

        } catch (Exception e) {
            System.out.println("Falha na consulta de usuario: "+ e.getMessage());
        }
        return null;
    }
    
    //Consulta passando o id
    public Usuario consultar_usuario(int id){
        //dados do bd
        String sql = "SELECT * FROM usuario WHERE id_usuario = ?";
        try{
            PreparedStatement pst = pst(sql);
            pst.setInt(1, id);
            ResultSet resultado = pst.executeQuery();

            //verifica se o id existe no bd
            if (resultado.next()){
                //pega os dados do bd
                String nome = resultado.getString("nome");
                String endereco = resultado.getString("endereco");
                String telefone = resultado.getString("telefone");
                
                //criar um obj Usuario
                Usuario usuario = new Usuario(nome);
                usuario.setEndereco(endereco);
                usuario.setTelefone(telefone);
                usuario.setIdUsuario(id);

                return usuario;
            }else{
                System.out.println("Não possui registro com o ID" + id);
            }
        } catch (Exception e){
            System.out.println("Falha na consulta do usuario: "+ e.getMessage());
        }
        return null;
    }

    //exclui o usuario por id
    public void excluir_usuario(int id){
        EmprestimoDAO emprestimoDAO = new EmprestimoDAO();
        //cria o obj Livro com o id que deseja excluir
        Usuario us = consultar_usuario(id);
        String sql = "DELETE FROM usuario WHERE id_usuario = ?";  
        
        try {
            //verifica se o id existe no BD
            if (us.getIdUsuario() == id){
                PreparedStatement pst = pst(sql);
                pst.setInt(1, id);
                boolean verificar = emprestimoDAO.verificar_emprestimo_usuario(id);
                if (verificar == true){
                    JOptionPane.showMessageDialog(null, "Usuario excluido com sucesso");
                    pst.execute();
                }
                else{
                    JOptionPane.showMessageDialog(null, "Não é possivel excluir usuario com emprestimo cadastrado, primeiro exclua o emprestimo");
                }
            }else{
                System.out.println(id + " não está cadastrado");
            }
        } catch (Exception e) {
            System.out.println("Falha na consulta usuario: "+ e.getMessage());
        }
    }

    //altera o usuario por id
    public void alterar_usuario(Usuario usuario, int id){
        String sql = "UPDATE usuario SET nome = ?, endereco = ?, telefone = ? WHERE id_usuario = ?";
        try{
            PreparedStatement pst = pst(sql);
            pst.setString(1, usuario.getNome());
            pst.setString(2, usuario.getEndereco());
            pst.setString(3, usuario.getTelefone());
            pst.setInt(4, id);
            pst.execute();

            System.out.println("Usuario atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta do usuario: "+ e.getMessage());
        }
    }

    //listar usuarios 
    public StringBuilder exibir_usuario(LinkedList<Usuario> usuario){
         
        StringBuilder sb = new StringBuilder();
        for (Usuario us : usuario) {
            sb.append("ID Usuário: ").append(us.getIdUsuario()).append(" | ")
            .append("Nome: ").append(us.getNome()).append(" | ")
            .append("Endereço: ").append(us.getEndereco()).append(" | ")
            .append("Telefone: ").append(us.getTelefone()).append("\n");
          
        }
        return sb;
    }

    //alterar todos dados do usuario
    public void alterar_usuario(int id, Usuario usuario){
        //comando sql
        String sql = "UPDATE usuario set nome = ? , endereco = ? , telefone = ? WHERE id_usuario = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, usuario.getNome());
            pst.setString(2, usuario.getEndereco());
            pst.setString(3, usuario.getTelefone());
            pst.setInt(4, id);

            pst.execute();
            System.out.println("Usuario atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de usuário: " + e.getMessage());
        }
    }

    //alterar nome do usuario
    public void alterar_nome(int id, String nome){      
        //deixando o nome maiusculo
        nome = nome.toUpperCase();
        //comando sql
        String sql = "UPDATE usuario set nome = ?  WHERE id_usuario = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, nome);
            pst.setInt(2, id);

            pst.execute();
            System.out.println("Usuário atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de usuário: " + e.getMessage());
        }
    }

    //alterar endereco do usuario
    public void alterar_endereco(int id, String endereco){
        //comando sql
        String sql = "UPDATE usuario set endereco = ?  WHERE id_usuario = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, endereco);
            pst.setInt(2, id);

            pst.execute();
            System.out.println("Usuario atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de usuário: " + e.getMessage());
        }
    }

    //alterar autor do livro
    public void alterar_telefone(int id, String telefone){
        //comando sql
        String sql = "UPDATE usuario set telefone = ?  WHERE id_usuario = ?";

        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, telefone);
            pst.setInt(2, id);

            pst.execute();
            System.out.println("Usuário atualizado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de usuário: " + e.getMessage());
        }
    }
}

