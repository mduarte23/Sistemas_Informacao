package DAO;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.LinkedList;

import Conexao.ConectaBD;
import java.sql.SQLException;
import java.text.DateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import javax.swing.JOptionPane;
import javax.xml.crypto.Data;
import model.Emprestimo;
import model.Livro;
import model.Usuario;


public class EmprestimoDAO {
    private ConectaBD conexao;

    public EmprestimoDAO(){
        conexao = new ConectaBD();
    }

    public PreparedStatement pst(String sql) throws SQLException{
        PreparedStatement pst = conexao.getConexaoBD().prepareStatement(sql);
        return pst;
    }

    //realizar emprestimo
    public void emprestimo(Emprestimo emprestimo){
        //comando bd
        String sql = "INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao, emprestado) values (?, ?, ?, ?, ?)";
        try {
            PreparedStatement pst = pst(sql);
            pst.setInt(1,emprestimo.getIdLivro());
            pst.setInt(2, emprestimo.getIdUsuario());
            pst.setString(3, emprestimo.getDataEmprestimo());
            pst.setString(4, emprestimo.getDevolucao());
            pst.setBoolean(5, emprestimo.isEmprestimo());

            pst.execute();
            System.out.println("Emprestimo cadastrado com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na inserção do emprestimo: "+ e.getMessage());
        }
    }

    public void devolver(int id){
        //comando sql
        String sql = "UPDATE emprestimo SET emprestado = false WHERE id_emprestimo = ? ";

        try {
            PreparedStatement pst = pst(sql);
            pst.setInt(1, id);
            pst.execute();
            System.out.println("Livro devolvido com sucesso.");
        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo: "+ e.getMessage());
        }    
    }

    // consultar emprestimo de um usuario
    public LinkedList historico_id(int id){
        String sql = "SELECT * FROM emprestimo WHERE id_usuario = ?";
        LinkedList lista = new LinkedList<>();
        
        UsuarioDAO usuario = new UsuarioDAO();
        Usuario us = usuario.consultar_usuario(id);


        //pega os dados do Usuario
        int id_us = us.getIdUsuario();
        String nome = us.getNome();
        //Cria o HashMap de Usuario
        HashMap<Integer, String> mapa_us = new HashMap<Integer, String>();
        //insere o id e o nome do usuario
        mapa_us.put(id_us, nome);
        

        try {
            PreparedStatement pst = pst(sql);
            pst.setInt(1, id);
            ResultSet resultados = pst.executeQuery();

            //cria um loop enquanto tiver dados
            while (resultados.next()){
                //recuperar dados do bd
                int id_emprestimo = resultados.getInt("id_emprestimo");
                int id_usuario = resultados.getInt("id_usuario");
                String data = resultados.getString("data_emprestimo");
                int id_livro = resultados.getInt("id_livro");
                boolean emprestado = resultados.getBoolean("emprestado");
                String data_devolucao = resultados.getString("data_devolucao");

                LivroDAO livro = new LivroDAO();
                Livro lv = livro.consultar_livro(id_livro);
                
                //pega os dados do Usuario
                int id_lv = lv.getIdLivro();
                String titulo = lv.getTitulo();
                //cria o HashMap do Livro
                HashMap<Integer, String> mapa_lv = new HashMap<Integer, String>();
                //Insere o ID e titulo do livro
                mapa_lv.put(id_lv, titulo);

                HashMap<Boolean, String> mapa_boolean = new HashMap<Boolean, String>(); 

                if (emprestado == true){
                    mapa_boolean.put(emprestado, "Emprestado");
                }else{
                    mapa_boolean.put(emprestado, "Devolvido");
                }

                //cria uma lista
                ArrayList list = new ArrayList<>();
                //adiciona os valores na lista
                list.add(id_emprestimo);
                list.add(mapa_us.get(id));
                list.add(mapa_lv.get(id_lv));
                list.add(data);
                list.add(data_devolucao);
                list.add(mapa_boolean.get(emprestado));
                //adiciona a lista no LinkedList
                lista.add(list);
                
            }
            return lista;

        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo: "+ e.getMessage());
        }
        return null;
    }

    public LinkedList emprestimos_ativos(){
        String sql = "SELECT * FROM emprestimo WHERE emprestado = true";
        LinkedList lista = new LinkedList<>();
        try {
            PreparedStatement pst = pst(sql);

            ResultSet resultados = pst.executeQuery();
            //loop enquanto tem resultados
            while (resultados.next()){
                //recuperar dados do bd
                int id_emprestimo = resultados.getInt("id_emprestimo");
                int id_usuario = resultados.getInt("id_usuario");
                String data = resultados.getString("data_emprestimo");
                int id_livro = resultados.getInt("id_livro");
                boolean emprestado = resultados.getBoolean("emprestado");
                String data_devolucao = resultados.getString("data_devolucao");

                //Criar HashMap de Usuario
                UsuarioDAO usuario = new UsuarioDAO();
                Usuario us = usuario.consultar_usuario(id_usuario);
                //pega os dados do Usuario
                int id_us = us.getIdUsuario();
                String nome = us.getNome();
                //Cria o HashMap de Usuario
                HashMap<Integer, String> mapa_us = new HashMap<Integer, String>();
                //insere o id e o nome do usuario
                mapa_us.put(id_us, nome);

                //cria o HashMap de Livro
                LivroDAO livro = new LivroDAO();
                Livro lv = livro.consultar_livro(id_livro);
                
                //pega os dados do Usuario
                int id_lv = lv.getIdLivro();
                String titulo = lv.getTitulo();
                //cria o HashMap do Livro
                HashMap<Integer, String> mapa_lv = new HashMap<Integer, String>();
                //Insere o ID e titulo do livro
                mapa_lv.put(id_lv, titulo);
                //cria o HashMap de Booleano
                HashMap<Boolean, String> mapa_boolean = new HashMap<Boolean, String>(); 
                //trata pra confirmar se esta ativo e insere no hashMap
                if (emprestado == true){
                    mapa_boolean.put(emprestado, "Emprestado");
                }else{
                    mapa_boolean.put(emprestado, "Devolvido");
                }
                
                //cria uma lista
                ArrayList list = new ArrayList<>();
                //adiciona os valores na lista
                list.add(id_emprestimo);
                list.add(mapa_us.get(id_us));
                list.add(mapa_lv.get(id_lv));
                list.add(data);
                list.add(data_devolucao);
                list.add(mapa_boolean.get(emprestado));
                //adiciona a lista no LinkedList
                lista.add(list);
            }
            return lista;
        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo: "+ e.getMessage());
        }
        return null;
    }

    //listar emprestimos 
    public StringBuilder exibir_emprestimos(LinkedList<ArrayList<Object>> emprestimo){

       StringBuilder sb = new StringBuilder();
       for (ArrayList emp : emprestimo) {
           sb.append("ID: ").append(emp.get(0)).append(" | ")
           .append("Usuario: ").append(emp.get(1)).append(" | ")
           .append("Livro: ").append(emp.get(2)).append(" | ")
           .append("Data Emprestimo: ").append(emp.get(3)).append(" | ")
           .append("Data Devolução: ").append(emp.get(4)).append(" | ")
           .append("Status: ").append(emp.get(5)).append("\n");
         
       }
       return sb;
   }

   public StringBuilder multa_atraso(LinkedList<ArrayList<Object>> atraso){
        StringBuilder sb = new StringBuilder();

        for (ArrayList at : atraso){
            sb.append("ID: ").append(at.get(0)).append(" | ")
            .append("Usuario: ").append(at.get(1)).append(" | ")
            .append("Livro: ").append(at.get(2)).append(" | ")
            .append("Data de devolução: ").append(at.get(3)).append(" | ")
            .append("Dias atrasados: ").append(at.get(4)).append(" | ")
            .append("Multa: R$").append(at.get(5)).append(" \n ");
        }
        return sb;
   }
   //retorna os emprestimos atrasados
   public LinkedList<ArrayList<Object>> emprestimos_atrasados(String data, float valor){
        String sql = "SELECT * FROM emprestimo WHERE data_devolucao < ?";
        
        LinkedList lista = new LinkedList<>();
        try {
            PreparedStatement pst = pst(sql);
            pst.setString(1, data);
            ResultSet resultados = pst.executeQuery();
            //loop enquanto tem resultados
            while (resultados.next()){
                //recuperar dados do bd
                int id_emprestimo = resultados.getInt("id_emprestimo");
                int id_usuario = resultados.getInt("id_usuario");
                int id_livro = resultados.getInt("id_livro");
                String data_devolucao = resultados.getString("data_devolucao");
                //String data_emprestimo = resultados.getString("data_emprestimo");



                //calcula a diferenca em dias
                long dias = dias_atrasados(data_devolucao, data);
                //calcula o valor de multa
                float valor_multa = multa(valor, dias);
                
                //Criar HashMap de Usuario
                UsuarioDAO usuario = new UsuarioDAO();
                Usuario us = usuario.consultar_usuario(id_usuario);
                //pega os dados do Usuario
                int id_us = us.getIdUsuario();
                String nome = us.getNome();
                //Cria o HashMap de Usuario
                HashMap<Integer, String> mapa_us = new HashMap<Integer, String>();
                //insere o id e o nome do usuario
                mapa_us.put(id_us, nome);

                //cria o HashMap de Livro
                LivroDAO livro = new LivroDAO();
                Livro lv = livro.consultar_livro(id_livro);
                
                //pega os dados do Usuario
                int id_lv = lv.getIdLivro();
                String titulo = lv.getTitulo();
                //cria o HashMap do Livro
                HashMap<Integer, String> mapa_lv = new HashMap<Integer, String>();
                //Insere o ID e titulo do livro
                mapa_lv.put(id_lv, titulo);
                
                
                //cria uma lista
                ArrayList list = new ArrayList<>();
                //adiciona os valores na lista
                list.add(id_emprestimo);
                list.add(mapa_us.get(id_us));
                list.add(mapa_lv.get(id_lv));
                list.add(data_devolucao);
                list.add(dias);
                list.add(valor_multa);
                //adiciona a lista no LinkedList
                lista.add(list);
            }
            return lista;
        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo: "+ e.getMessage());
        }
        return null;
   }

     //calcula a diferenca de dias 
     public  long dias_atrasados(String data_devolucao, String data) {
        //formata a data para Date
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate dataAtual = LocalDate.parse(data, formatter);
        LocalDate dataDevolucao = LocalDate.parse(data_devolucao, formatter);
        //calcula a diferenca de dias 
        return ChronoUnit.DAYS.between(dataDevolucao, dataAtual);
    }

    //calcula o valor da multa
    public float multa(float valor, long dias){
        float valor_multa = valor * dias;
        return valor_multa;
    }

    public void excluir_emprestimo(int id){
        String sql = "DELETE  FROM emprestimo WHERE id_emprestimo = ?";
        try {
            PreparedStatement pst = pst(sql);
            pst.setInt(1, id);
            pst.execute();
            System.out.println("Emprestimo excluido com sucesso!");
        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo: "+ e.getMessage());
        }
    }



    public boolean verificar_emprestimo_usuario(int id){
        String sql = "SELECT * FROM emprestimo WHERE id_usuario = ?";
        try {
            PreparedStatement pst = pst(sql);
            pst.setInt(1, id);
            ResultSet resultados = pst.executeQuery();
            if (resultados.next()){
                return false;
            }
            return true;

        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo");
        }
        return false;
    }
    public boolean verificar_emprestimo_livro(int id){
        String sql = "SELECT * FROM emprestimo WHERE id_livro = ?";
        try {
            PreparedStatement pst = pst(sql);
            pst.setInt(1, id);
            ResultSet resultados = pst.executeQuery();
            if (resultados.next()){
                return false;
            }
            return true;

        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo");
        }
        return false;
    }

    //exibir todos emprestimos
    public LinkedList exibir_todos_emprestimos(){
        String sql = "SELECT * FROM emprestimo";
        LinkedList lista = new LinkedList<>();
        try {
            PreparedStatement pst = pst(sql);
            ResultSet resultados = pst.executeQuery();
            while (resultados.next()){
                //recupera os dados do BD
                int id_emprestimo = resultados.getInt("id_emprestimo");
                int id_usuario = resultados.getInt("id_usuario");
                int id_livro = resultados.getInt("id_livro");
                boolean emprestado = resultados.getBoolean("emprestado");
                String data_emprestimo = resultados.getString("data_emprestimo");
                String data_devolucao = resultados.getString("data_devolucao");

                //cria o UsuarioDAO e Usuario
                UsuarioDAO usuarioDAO = new UsuarioDAO();
                Usuario usuario = usuarioDAO.consultar_usuario(id_usuario);
                //pega os dados do usuario
                int id_us = usuario.getIdUsuario();
                String nome = usuario.getNome();
                //cria o hashMap do usuario
                HashMap<Integer, String> mapa_usuario = new HashMap<Integer, String>();
                //insere os dados no HashMap
                mapa_usuario.put(id_us, nome);

                //cria o LivroDAO e Livro
                LivroDAO livroDAO = new LivroDAO();
                Livro livro = livroDAO.consultar_livro(id_livro);
                //pega os dados do livro
                int id_lv = livro.getIdLivro();
                String titulo = livro.getTitulo();
                //cria o hashMap do livro
                HashMap<Integer, String> mapa_livro = new HashMap<Integer, String>();
                //insere os dados no HashMap
                mapa_livro.put(id_lv, titulo);

                //cria o HashMap de Boolean
                HashMap<Boolean, String> mapa_boolean = new HashMap<Boolean, String>();
                //verifica se é verdadeiro ou falso e insere no mapa
                if (emprestado == true) { 
                    mapa_boolean.put(emprestado, "Emprestado");
                }else{
                    mapa_boolean.put(emprestado, "Devolvido");
                }

                //cria uma ArrayList
                ArrayList list = new ArrayList<>();
                //insere os valores na lista
                list.add(id_emprestimo);
                list.add(mapa_usuario.get(id_us));
                list.add(mapa_livro.get(id_lv));
                list.add(data_emprestimo);
                list.add(data_devolucao);
                list.add(mapa_boolean.get(emprestado));
                //adiciona a ArrayList na LinkedList
                lista.add(list);
            }
            return lista;
        } catch (Exception e) {
            System.out.println("Falha na consulta de emprestimo: "+ e.getMessage());
        }
        return null;
    }
}


