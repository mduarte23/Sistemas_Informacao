
import java.util.LinkedList;
import java.util.Random;
import java.util.Scanner;

public class App {
    static LinkedList tabela[] = new LinkedList[26];
    static Scanner input = new Scanner(System.in);


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
            if (lista != null){
                int total = lista.size();
                System.out.println(i + " total: "+ total + " -> " + lista);
            }else{
                System.out.println(i + " total: "+ 0 + " -> " + lista);
            }
        }    
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

    public static int menu(){
       
        System.out.println("*****MENU*****");
        System.out.println("1- Buscar");
        System.out.println("2- Sair");
        System.out.print(">>>>");
        return input.nextInt();
    }

    public static void busca(String palavra){
        int categoria = hash(palavra);
        System.out.println("*****BUSCA*****");
        System.out.println("Categoria " + categoria);
        LinkedList lista = tabela[categoria];
        if (lista.contains(palavra)){
            System.out.println(palavra + " está presente.");
        }else{
            System.out.println(palavra + " não está presente");
        }
    }

    public static void main(String[] args) {
        //System.out.println("Olá");
        gerarNomes(50000);  
        imprimir();  
        int op = 0;
        do {
            op = menu();
            if (op == 1){
                System.out.println("Digite a palavra a ser procurada: ");
                String palavra = input.next();
                busca(palavra);
            }else if((op != 2) && (op != 1)){
                System.out.println("Opção invalida");
            }else{
                System.out.println("Saindo...");
            }
        } while (op != 2);   
    }
}

