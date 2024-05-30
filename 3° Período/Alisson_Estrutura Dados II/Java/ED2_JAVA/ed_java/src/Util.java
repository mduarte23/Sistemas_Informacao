public class Util {
    //static é publica, todo arquivo consegue acessar o valor
    public static boolean validarCpf (String cpf){

        if (cpf.length() == 11){
            if (primeiroDigito(cpf)){
                return true;
            }
            
        }
        return false;
    }

    public static boolean primeiroDigito(String cpf) {
        char[] cpfArray = cpf.toCharArray();
        int verificador1 = Integer.parseInt(String.valueOf(cpfArray[9]));
        int verificador2 = Integer.parseInt(String.valueOf(cpfArray[10]));
        int contador = 0;
        int soma = 0;
        int conversao = 0;
        for (int i = 10; i > 1; i--, contador++) {
            conversao = Integer.parseInt(String.valueOf(cpfArray[contador]));
            soma += conversao * i;
            //System.out.println(soma);
        }
        int resto = (soma * 10)%11;
        if (resto == 10){
            resto = 0;
        }
        int resto2 = segundoDigito(cpf);

        if ((resto == verificador1) && (resto2 == verificador2)){
            System.out.println("CPF Valido");
            segundoDigito(cpf);
            return true;
        }else{
            System.out.println("CPF invalido");
            return false;
        }
    }

    public static Integer segundoDigito(String cpf){
        char[] cpfArray = cpf.toCharArray();
        //int verificador2 = Integer.parseInt(String.valueOf(cpfArray[10]));
        int contador = 0;
        int soma = 0;
        int conversao = 0;
        for (int i = 11; i > 1; i--, contador++) {
            conversao = Integer.parseInt(String.valueOf(cpfArray[contador]));
            soma += conversao * i;
            //System.out.println(soma);
        }
        int resto = (soma * 10)%11;
        if (resto == 10){
            resto = 0;
        }
        return resto;
        //if (resto == verificador2){
        //    System.out.println("validado");
        //    return true;
        //}else{
        //    return false;
        //}
    }

    public static void main(String[] args) {
        primeiroDigito("08838824690");
    }
}

