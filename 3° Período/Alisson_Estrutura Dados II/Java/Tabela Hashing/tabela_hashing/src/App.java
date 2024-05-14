
import java.util.LinkedList;

public class App {
    static LinkedList tabela[] = new LinkedList[26];



    //def hash() (define funçao)
    public static int hash(String valor){
        valor = valor.toLowerCase();
        //pega a primeira letra da variavel
        //System.out.println(valor.charAt(0));
        //transforma a letra no numero correspondente pela tabela Ascii
        int codigoAscii = valor.charAt(0);
        int resto = (codigoAscii+7) % 26;

        //System.out.println(codigoAscii%26 + " " + resto);
        return resto;
    }

    public static void adiciona(String valor){
        int categoria = hash(valor);
        if (tabela[categoria] == null){
            tabela[categoria] = new LinkedList();
        }
        tabela[categoria].add(valor);
        //System.out.println(tabela[categoria]);
    }



    public static void main(String[] args) {
        System.out.println("Olá");
        

        adiciona("Astrogildo");
        adiciona ("Silvio Santos");
        adiciona("Zuleide");
        adiciona ("adolfo");
        //imprimir toda a tabela
        for (LinkedList lista : tabela) {
            
            System.out.println(lista);
        }
        
    }
}

