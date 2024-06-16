//import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
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
