
import java.util.Scanner;

//import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Biblioteca bib = new Biblioteca();
        Biblioteca user = new Biblioteca();
         
        while (true) { 
            System.out.println("-----MENU-----");
            System.out.println("1- Cadastro de livros:");
            System.out.println("2-Cadastro de usuários:");
            System.out.println("0- Sair:");
            System.out.println("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine();
            
            if(opcao == 1){
                System.out.println("-----MENU-----");
                System.out.println("1- Inserir Livro:");
                System.out.println("2- Busca livro por ID:");
                System.out.println("3- Remover livro por ID:");
                System.out.println("4- Listar livros:");
                System.out.println("0- Menu anterior:");
                int opcao2 = scanner.nextInt();
                scanner.nextLine();

                if (opcao2 == 1){
                    System.out.println("Digite o título do livro:");
                    String titulo = scanner.nextLine();
                    System.out.println("Digite o autor do livro:");
                    String autor = scanner.nextLine();
                    System.out.println("Digite o ano de publicação do livro:");
                    int ano = scanner.nextInt();

                    Livro livro = new Livro(titulo);
                    livro.setAutor(autor);
                    livro.setAnoPublicacao(ano);

                    bib.inserir(livro);

                }else if (opcao2 == 2){
                    System.out.println("Digite o ID do livro que deseja buscar:");
                    int id = scanner.nextInt();
                    bib.consultaID(id);
                }else if (opcao2 == 3){
                    System.out.println("Digite o ID do livro que deseja remover:");
                    int id = scanner.nextInt();
                    bib.remover(id);
                }else if (opcao2 == 4){
                    bib.listarTodos(); 
                }else if (opcao2 == 0){
                    System.out.println("Retornando...");
                
                }else{
                    System.out.println("Opcao inválida. Tente novamente.");
                }
            }else if (opcao == 2){
                System.out.println("-----MENU-----");
                System.out.println("1- Inserir usuário:");
                System.out.println("2- Buscar usuário por ID:");
                System.out.println("3- Remover usuário por ID:");
                System.out.println("4- Listar usuários:");
                System.out.println("0- Menu anterior:");
                int opcao2 = scanner.nextInt();
                scanner.nextLine();

                if (opcao2 == 1){
                    System.out.println("Digite o nome do usuário:");
                    String nome = scanner.nextLine();
                    System.out.println("Digite o email do usuário:");
                    String email = scanner.nextLine();
                    
                    Usuario usuario = new Usuario(nome);
                    usuario.setEmail(email);

                    user.inserirUsuario(usuario);
                }else if (opcao2 == 2){
                    System.out.println("Digite o ID do usuário que deseja buscar:");
                    int id = scanner.nextInt();

                    user.consultaIDUsuario(id);
                }else if (opcao2 == 3){
                    System.out.println("Digite o ID do usuário que deseja remover:");
                    int id = scanner.nextInt();

                    user.removerUsuario(id);
                }else if (opcao2 == 4){
                    user.listarTodosUsuarios();
                }else if (opcao2 == 0){
                    System.out.println("Retornando...");
                    
                }else{
                    System.out.println("Opcao inválida. Tente novamente.");
                }
            }else if  (opcao== 0){
                System.out.println("Saindo...");
                scanner.close();
                return;
            }else{
                System.out.println("Opçcão inválida, tente novamente.");
                }
        }
    }
}

        /* 

        Livro obj1 = new Livro("Cronicas de Narnia");
        obj1.setAutor("Marcelinho Carioca");
        obj1.setAnoPublicacao(1995);
        //System.out.println(obj1);

        //int indice1 = Livro.getContador();
        
        //String indice = "livro"+ Livro.getContador();
        //System.out.println(indice);

        Livro obj2 = new Livro("Magico de Oz");
        obj2.setAutor("Carlos Montenegro");
        obj2.setAnoPublicacao(1775);
        //System.out.println(obj2);

        Livro obj3 = new Livro("Harry Potter");
        obj3.setAutor("Adolfe");
        obj3.setAnoPublicacao(1975);
        //System.out.println(obj2);

        //instanciar biblioteca
        Biblioteca bib = new Biblioteca();
        bib.inserir(obj1);
        bib.inserir(obj2);
        bib.inserir(obj3);
        bib.inserir(obj3);
        //System.out.println(bib);

        bib.listarTodos();

        bib.consultaID(2);

        bib.remover(4);

        bib.listarTodos();

        Usuario user1 = new Usuario("Marcelo");
        user1.setEmail("marcelo@hotmail.com");
        //System.out.println(user1);

        Usuario user2 = new Usuario("Alysson");
        user2.setEmail("alysson@gmail.com");
        //System.out.println(user2);

        Usuario user3 = new Usuario("Ely");
        user3.setEmail("ely@gmail.com");
        //System.out.println(user3);

        //instanciar biblioteca
        Biblioteca user = new Biblioteca();
        user.inserirUsuario(user1);
        user.inserirUsuario(user2);
        user.inserirUsuario(user3);
        //System.out.println(bib);

        user.listarTodosUsuarios();

        user.consultaIDUsuario(2);

        user.removerUsuario(4);

        user.listarTodosUsuarios();

        
    }
}
*/