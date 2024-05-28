import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class App {
    //parametro para imprimir
    public static void imprimir(int vetor[]){
        System.out.println(vetor);
        for (int j = 0; j < vetor.length; j++) {
            System.out.println(j + ": " + vetor[j]);
        }
    }
    //executa a partir do main
    public static void main(String[] args) throws Exception {
        /*
        vetor - array 
        ED ESTATICA
        - tamanho não vai ser alterado
        - tipo nome[] = new tipo[]
        - tipo []nome = new tipo[]
        */ 

        int idade[] = new int[10];
        idade[0] = 5;
        String valor = "8";
        //converter String para numero
        idade[3] = Integer.parseInt(valor);
        idade[1]= 2;
        idade[2]= 9;

        imprimir(idade);

        //Collection ArrayList
        //cria um vetor dinamico
        System.out.println("COLLECTION");
        ArrayList<Integer> vetor = new ArrayList<Integer>();
        System.out.println(vetor.size());
        System.out.println(vetor.isEmpty()); // retorna verdadeiro ou falso se a lista esta vazia
        vetor.add(65);
        vetor.add(36);
        System.out.println(vetor.size());
        System.out.println(vetor);
        Collections.sort(vetor); //Ordenar a lista
        System.out.println(vetor);


        //ordenar vetor idade
        Arrays.sort(idade);
        imprimir(idade);

        
    }
}
