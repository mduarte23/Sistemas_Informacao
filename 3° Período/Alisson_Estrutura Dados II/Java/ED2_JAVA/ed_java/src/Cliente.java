
import javax.swing.JOptionPane;

public class Cliente {
    private String nome;
    private String cpf;
    private double saldo;

    //Obriga a passar o cpf obrigatoriamente no construtor
    public Cliente (String cpf){
        //this.cpf = cpf da variavel
        //cpf = parametro do construtor
        //this.cpf = cpf;
        this.setCpf(cpf);
    }

    // metodos modificadores de acesso
    // set -> modificador (parametros e nao retorna nada)
    // get -> acesso (não tem parametro e retorna valor do atributo)

    //não permite que o cpf seja alterado de fora da aplicaçao (outro arquivo)
    private void setCpf(String cpf){
        if (Util.validarCpf(cpf)){
            this.cpf = cpf;
        }else{
            System.out.println("CPF Inválido" + cpf);
            //cria uma janela de alerta com input
            String novoCPF = JOptionPane.showInputDialog(null, "Digite novo CPF");
            this.setCpf(novoCPF);
        }
        
    }

    public String getCpf(){
        return cpf;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    //cria o toString para imprimir conteudo pelo sout
    public String toString(){
        return "CPF: "+ getCpf()+ " |Nome: " + getNome() + " |Saldo: R$" + getSaldo();
    }
    
}
