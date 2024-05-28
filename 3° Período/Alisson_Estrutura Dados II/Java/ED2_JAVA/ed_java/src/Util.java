public class Util {
    //static é publica, todo arquivo consegue acessar o valor
    public static boolean validarCpf (String cpf){

        if (cpf.length() == 3){
            return true;
        }
        return false;
    }
}
