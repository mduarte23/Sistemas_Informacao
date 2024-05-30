
import java.util.ArrayList;

public class AppTeste {
    public static void main(String[] args) {
        Cliente jose = new Cliente("134");
        Cliente maria = new Cliente("354");
        //alterando o objeto jose
        jose.setNome("Jose");
        jose.setSaldo(7.50);

        //alterando o objeto maria
        maria.setNome("Maria");
        maria.setSaldo(74.82);

        //impriminto os objetos
        System.out.println(jose);
        System.out.println(maria);
        //System.out.println(maria.toString());

        ArrayList<Cliente> cadastro = new ArrayList<Cliente>();
        cadastro.add(jose);
        cadastro.add(maria);
        System.out.println(cadastro);
    }
}
