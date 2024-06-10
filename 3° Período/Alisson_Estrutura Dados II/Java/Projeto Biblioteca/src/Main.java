import java.awt.event.InputEvent;
import java.util.Scanner;
import java.awt.im.InputContext;


public class Main {
    public static void main(String[] args) {
        Livro obj1 = new Livro("Cronicas de Narnia");
        obj1.setAutor("Marcelinho Carioca");
        obj1.setAnoPublicacao("1995");
        //System.out.println(obj1);

        Livro obj2 = new Livro("Magico de Oz");
        obj2.setAutor("Carlos Montenegro");
        obj2.setAnoPublicacao("1775");
        //System.out.println(obj2);

        Livro obj3 = new Livro("Harry Potter");
        obj3.setAutor("Adolfe");
        obj3.setAnoPublicacao("1975");
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


        int op = 0;
        Scanner scanner = new Scanner(System.in);
        do {     
            op = Biblioteca.menu(scanner);
            if (op == 1){
              String nome = scanner.next();
              String autor;
              int anoPublicacao;

            }
        } while (op != 5);
        

    }
}
