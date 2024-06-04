
import java.util.LinkedList;
import javax.sound.sampled.SourceDataLine;
import javax.swing.text.html.FormView;

public class Biblioteca {
    private LinkedList<Livro> dados;

    public Biblioteca(){
        dados = new LinkedList<Livro>();
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

}
