
import java.util.LinkedList;



/*
import java.util.Scanner;

public class MainDB {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LivroDAO objDAO = new LivroDAO();
        UsuarioDao userDao = new UsuarioDao();
         
        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Inserir livro");
            System.out.println("2. Inserir usuário");
            System.out.println("3. Sair");
            System.out.println("4- testes");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); // Consumir a nova linha

            if (opcao == 1) {
                System.out.print("Digite o título do livro: ");
                String titulo = scanner.nextLine();
                System.out.print("Digite o autor do livro: ");
                String autor = scanner.nextLine();
                System.out.print("Digite o ano de publicação do livro: ");
                int anoPublicacao = scanner.nextInt();
                scanner.nextLine(); // Consumir a nova linha
                    
                Livro liv = new Livro(titulo);
                liv.setAutor(autor);
                liv.setAnoPublicacao(anoPublicacao);
                objDAO.inserir(liv);
                    
                System.out.println("Livro inserido com sucesso!");
                    
            }else if(opcao == 2){
                System.out.print("Digite o nome do usuário: ");
                String nome = scanner.nextLine();
                System.out.print("Digite o email do usuário: ");
                String email = scanner.nextLine();
                    
                Usuario user = new Usuario(nome);
                user.setEmail(email);
                userDao.inserir(user);
                    
                System.out.println("Usuário inserido com sucesso!");
                    
            }else if (opcao ==3){ 
                System.out.println("Saindo...");
                scanner.close();
                return;
            }else if (opcao == 4){
                consultarTodos();
            }
            
            
            
            else{   
                System.out.println("Opção inválida. Tente novamente.");
                break;
            }                
        }
            
    }
}
    */

public class MainDB {
    public static void main(String[] args) {
        /* 
        Livro liv = new Livro("O senhor dos anéis");
        liv.setAutor("J. R. R. Tolkien");
        liv.setAnoPublicacao(1953);
    
        LivroDAO objDAO = new LivroDAO();
        //objDAO.inserir(liv);
    
        Usuario user = new Usuario("Matheus");
        user.setEmail("matheus@gmail.com");
    
        UsuarioDao userDao = new UsuarioDao();
        //userDao.inserir(user);

        //LinkedList<Livro> dados = objDAO.consultarTodos();
        //System.out.println(dados);

        //Livro livroConsulta = objDAO.consultar(2);
        //System.out.println(livroConsulta);

        //objDAO.excluir(8);

        //Livro livro = new Livro("Teste");
        //livro.setAutor("teste");
        //livro.setAnoPublicacao(2000);
        //LivroDAO livroDAO = new LivroDAO();

        //livroDAO.alterar(livro, 9);

        //LinkedList<Livro> dados = objDAO.consultarTodos();
        //System.out.println(dados);
        */

        //Usuario user = new Usuario("Teste");
        //user.setEmail("teste@email");

        //UsuarioDao userDao = new UsuarioDao();
        //userDao.inserir(user);
        
        //LinkedList<Usuario> dados = userDao.consultarTodosUsuarios();
        //System.out.println(dados);
    
        //Usuario usuarioConsulta = userDao.consultarUsuario(3);
        //System.out.println(usuarioConsulta);
        
        //userDao.excluirUsuario(8);

        Usuario usuario = new Usuario("Teste1");
        usuario.setEmail("email.com");
        
        UsuarioDao usuarioDAO = new UsuarioDao();

        usuarioDAO.alterarUsuario(usuario, 2);

        LinkedList<Usuario> dados = usuarioDAO.consultarTodosUsuarios();
        System.out.println(dados);
        
        }
    }
