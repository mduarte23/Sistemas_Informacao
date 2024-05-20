
import java.util.LinkedList;
import java.util.Random;

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
        //imprimir();
    }

    public static void imprimir(){
        //funçao para imprimir toda a tabela
        for (int i = 0; i < tabela.length; i++) {
            LinkedList lista = tabela[i];
            int total = lista.size();
            System.out.println(i + " total: "+ total + " -> " + lista);
        }
        
        //for (LinkedList lista : tabela) {
         //   System.out.println(lista);
       // }
    }

    public static void gerarNomes (int qtdPalavras){
        //gera palavras aleatorias
        Random rnd = new Random();
        for (int i = 0; i < qtdPalavras; i++) {
            int qtdLetras = rnd.nextInt(3,9);
            String palavra = "";
            for (int j = 0; j < qtdLetras; j++) {
                char letra = (char)(rnd.nextInt(97, 123));
                palavra += letra;
            }
            adiciona(palavra);
        }
        
    }

    public static void main(String[] args) {
        //System.out.println("Olá");
        gerarNomes(500);  
        imprimir();     
    }
}

