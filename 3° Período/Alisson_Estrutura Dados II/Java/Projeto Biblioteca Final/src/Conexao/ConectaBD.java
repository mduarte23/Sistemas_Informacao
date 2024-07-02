package Conexao;

import java.sql.Connection;
import java.sql.DriverManager;

//classe para conectar com BD
public class ConectaBD {
    //faz a conexao com BD
    private Connection conexao;
    //construtor para conectar no BD
    public ConectaBD() {
        //url do banco de dados
        String url = "jdbc:mariadb://localhost:3306/biblioteca";
        String user = "root";
        String pwd = "98245803";

        try{
            conexao = DriverManager.getConnection(url, user, pwd);
            System.out.println("Conexão com BD realizada");
        } catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println("Não encontrado o drive");
        }
    }

    //metodo que retorna a conexao com o BD
    public Connection getConexaoBD(){
        return conexao;
    }
    
}
