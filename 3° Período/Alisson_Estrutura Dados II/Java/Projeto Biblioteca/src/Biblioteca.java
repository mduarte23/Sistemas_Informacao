
import java.util.LinkedList;
import javax.sound.sampled.SourceDataLine;
import javax.swing.text.html.FormView;
import java.util.Scanner;


public class Biblioteca {
    private LinkedList<Livro> dados;
    private LinkedList<Usuario> dadosUsuarios;
    static Scanner input = new Scanner(System.in);

    public Biblioteca(){
        dados = new LinkedList<Livro>();
        dadosUsuarios = new LinkedList<Usuario>();
    }

    public void inserir(Livro livro){
        if (dados.contains(livro)){
            System.out.println("Livro já inserido");
        }else{
            dados.add(livro);
        }
    }

    public void listarTodos(){
        for (int i = 0; i < dados.size(); i++) {
           System.out.println(dados.get(i));
        }    
    }

    public Livro consultaID(int id){
        for (Livro livro : dados) {
            if (livro.getId() == id){
                System.out.println("Livro encontrado");
                System.out.println(livro);
                return livro;
            }
        }
        System.out.println(id + " não está cadastrado");
        return null;
    }

    public void remover(int id){
        for (Livro livro : dados) {
            if (livro.getId() == id){
                System.out.println("Livro removido com sucesso");
                dados.remove(livro);
            }
        }
    }
/* 
    public static int menu(){
       
        System.out.println("*****MENU*****");
        System.out.println("1- Inserir Livro");
        System.out.println("2- Busque Livro por ID");
        System.out.println("3- Remova Livro por ID");
        System.out.println("4- Liste todos Livros");
        System.out.println("5- Sair");
        System.out.print(">>>>");
        return input.nextInt();
    }

    */

    public void inserirUsuario(Usuario usuario){
        if (dadosUsuarios.contains(usuario)){
            System.out.println("Usuário já inserido");
        }else{
            dadosUsuarios.add(usuario);
        }
    }

    public void listarTodosUsuarios(){
        for (int i = 0; i < dadosUsuarios.size(); i++) {
           System.out.println(dadosUsuarios.get(i));
        }    
    }

    public Usuario consultaIDUsuario(int id_usuario){
        for (Usuario usuario : dadosUsuarios) {
            if (usuario.getId_Usuario() == id_usuario){
                System.out.println("Usuário encontrado");
                System.out.println(usuario);
                return usuario;
            }
        }
        System.out.println(id_usuario + " não está cadastrado");
        return null;
    }

    public void removerUsuario(int id_usuario){
        for (Usuario usuario : dadosUsuarios) {
            if (usuario.getId_Usuario() == id_usuario){
                System.out.println("Usuário removido com sucesso");
                dados.remove(usuario);
            }
        }
    }
}
