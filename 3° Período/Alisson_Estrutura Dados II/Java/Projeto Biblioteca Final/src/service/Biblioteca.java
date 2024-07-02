package service;

import DAO.EmprestimoDAO;
import DAO.LivroDAO;
import DAO.UsuarioDAO;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.LinkedList;
import javax.swing.JOptionPane;
import model.Emprestimo;
import model.Livro;
import model.Usuario;

public class Biblioteca {
    //obter a data atual
    private LocalDate data_atual(){
        LocalDate dataAtual = LocalDate.now();
        return dataAtual;
    }
    //calcula a data de devolucao
    private LocalDate data_devolucao (LocalDate data, int dias) {
        return data.plusDays(dias);
    }
    //transforma a data em String para passar para o bd
    private String data_string(LocalDate data){
        //define o formato da data
        DateTimeFormatter formatador = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        //converte a data em String      
        String data_string = data.format(formatador);
        return data_string;
    }

    //verifica se esta inserindo dados na opcao
    //recebe a variavel para exibir o nome na janela
    private String verificacao(String variavel){
        //cria uma variavel com valor null
        String variavel_local = null;
        while (true){
            variavel_local = JOptionPane.showInputDialog("Digite o " + variavel +":");
            //se o usuario cancela retorna null
            if (variavel_local == null){
                return null;
            //se for preenchida retorna o valor preenchido
            }else if (!variavel_local.trim().isEmpty()) {
                return variavel_local;
            }
        }
    }
   
    //verifica se foi apertado o botao de cancelar
    private void cancelar(String variavel){
        if (variavel == null){
            //se foi cancelado chama o menu principal 
            menu_principal();
        }
    }


    //menu principal
    public void  menu_principal(){
        //cria a variavel com valor null para entrar no loop
        String opcao = null;
        while (opcao == null) { 
            opcao = JOptionPane.showInputDialog("Escolha a opcao:\n1-Livro\n2-Usuário\n3-Emprestimo\n4-Sair");
            if (opcao == null) {
                // Caso o usuário cancele a entrada
                JOptionPane.showMessageDialog(null, "Saindo do programa.");
                System.exit(0);
                //break;
                
            }
            else if (opcao.equals("1")){
                menu_livro();
            }else if (opcao.equals("2")){
                menu_usuario();
            }else if (opcao.equals("3")){
                menu_emprestimo();
            }else if (opcao.equals("4")){
                JOptionPane.showMessageDialog(null, "Saindo do programa");
                System.exit(0);
                break;
            }else{
                //caso escolha uma opcao nao listada reinicia o loop
                opcao = null;
            }
        }
        //return null;
    }
        
    //menu do livro
    private void menu_livro(){
        //cria o obj Livro e LivroDAO
        LivroDAO livroDAO = new LivroDAO();
        Livro livro = null;
        //cria a variavel com valor null para entrar no loop
        String opcao = null;
        while (opcao == null) { 
            opcao = JOptionPane.showInputDialog("Escolha a opcao:\n1-Adicionar Livro\n2-Atualizar livro por ID\n3-Excluir Livro por ID\n4-Consultar livro por ID\n5-Listar todos Livros\n6-Menu anterior");
            //verifica se foi cancelado a opcao,  volta para o menu principal
            cancelar(opcao);
            //insere um novo livro no banco de dados
            if (opcao.equals("1")){
                //pega os dados para inserir no obj Livro
                //cria a variavel com o nome dela para aparecer na janela
                String titulo = "titulo";
                //chama a funcao para receber o valor
                titulo = verificacao(titulo);
                //verifica se foi apertado o botao cancelar
                cancelar(titulo);
                //cria a variavel com o nome dela para aparecer na janela
                String autor = "autor";
                //chama a funcao para receber o valor
                autor = verificacao(autor);
                //verifica se foi apertado o botao cancelar
                cancelar(autor);
                
                //Pegar ano tratando erros
                int ano;
                while (true){
                    //verifica se o ano digitado é numero
                    try {   
                        //cria a variavel com o nome dela para aparecer na janela
                        String ano_string = "ano de publicação";
                        //chama a funcao para receber o valor
                        ano_string = verificacao(ano_string);
                        //verifica se foi apertado o botao cancelar
                        cancelar(ano_string);
                        //converte a string em numero
                        ano = Integer.parseInt(ano_string);
                        break;
                    } catch (Exception e) {
                        //caso nao seja numero
                        JOptionPane.showMessageDialog(null, "Entrada inválida, digite o ano de publicaçao em números:");

                    }
                }
                //insere o obj Livro
                livro = new Livro(titulo);
                livro.setAutor(autor);
                livro.setAnoPublicacao(ano);
                //insere o obj LivroDAO
                livroDAO.inserir_livro(livro);
                //mensagem de confirmacao
                JOptionPane.showMessageDialog(null, "Livro inserido com sucesso!");

            }
            //Atualizar livro
            else if(opcao.equals("2")){
                //listar todos livros
                LinkedList lista = livroDAO.consultar_todos_livros();
                //cria a variavel id
                int id;
                //cria obj StringBuilder (para listar os livros disponíveis)
                StringBuilder sb = livroDAO.exibir_livros(lista);
                //pega o id exibindo a msg 
                String id_string = JOptionPane.showInputDialog("Lista de livros cadastrados\n" + sb.toString() + "\nDigite o ID que deseja alterar:");
                cancelar(id_string);
                //converte o id em numero
                id = Integer.parseInt(id_string);
                //sub menu de opções de atualização
                String op = null;
                while (op == null){
                    op = JOptionPane.showInputDialog("O que você deseja alterar: \n1-Todos os dados \n2-Título \n3-Autor \n4-Ano de publicação"); 
                    //verifica se usuario cancelou
                    cancelar(op);
                    
                    //altera todos os dados
                    if (op.equals("1")){
                        //cria a variavel com o nome dela para aparecer na janela
                        String titulo = "titulo";
                        //chama a funcao para receber o valor
                        titulo = verificacao(titulo);
                        //verifica se foi apertado o botao cancelar
                        cancelar(titulo);
                        //cria a variavel com o nome dela para aparecer na janela
                        String autor = "autor";
                        //chama a funcao para receber o valor
                        autor = verificacao(autor);
                        //verifica se foi apertado o botao cancelar
                        cancelar(autor);
                        //Pegar ano tratando erros
                        int ano;
                        while (true){
                        //verifica se o ano digitado é numero
                        try {   
                            //cria a variavel com o nome dela para aparecer na janela
                            String ano_string = "ano de publicação";
                            //chama a funcao para receber o valor
                            ano_string = verificacao(ano_string);
                            //verifica se foi apertado o botao cancelar
                            cancelar(ano_string);
                            //converte a string em numero
                            ano = Integer.parseInt(ano_string);
                            break;
                        } catch (Exception e) {
                            //caso nao seja numero
                            JOptionPane.showMessageDialog(null, "Entrada inválida, digite o ano de publicaçao em números:");
                        }
                    }

                    //insere o obj Livro
                    livro = new Livro(titulo);
                    livro.setAutor(autor);
                    livro.setAnoPublicacao(ano);
                    //insere o obj LivroDAO
                    livroDAO.alterar_livro(id, livro);
                    //mensagem de confirmacao
                    JOptionPane.showMessageDialog(null, "Livro alterado com sucesso!");
                }
                    else if (op.equals("2")) {                   
                        //cria a variavel com o nome dela para aparecer na janela
                        String titulo = "titulo";
                        //chama a funcao para receber o valor
                        titulo = verificacao(titulo);
                        //verifica se foi apertado o botao cancelar
                        cancelar(titulo);
                        //funcao para alterar o titulo
                        livroDAO.alterar_titulo(id, titulo);
                        //mensagem de execucao
                        JOptionPane.showMessageDialog(null, "Livro alterado com sucesso!");
                    }else if (op.equals("3")){
                        String autor = "autor";
                        //chama a funcao para receber o valor
                        autor = verificacao(autor);
                        //verifica se foi apertado o botao cancelar
                        cancelar(autor);
                        //funcao para alterar o autor
                        livroDAO.alterar_autor(id, autor);
                        //mensagem de execucao
                        JOptionPane.showMessageDialog(null, "Livro alterado com sucesso!");

                    }else if (op.equals("4")){
                        //Pegar ano tratando erros
                        int ano;
                        while (true){
                            //verifica se o ano digitado é numero
                            try {   
                                //cria a variavel com o nome dela para aparecer na janela
                                String ano_string = "ano de publicação";
                                //chama a funcao para receber o valor
                                ano_string = verificacao(ano_string);
                                //verifica se foi apertado o botao cancelar
                                cancelar(ano_string);
                                //converte a string em numero
                                ano = Integer.parseInt(ano_string);
                                break;
                            } catch (Exception e) {
                                //caso nao seja numero
                                JOptionPane.showMessageDialog(null, "Entrada inválida, digite o ano de publicaçao em números:");
                            }
                        }
                        //funcao para alterar o ano do livro
                        livroDAO.alterar_ano(id, ano);
                        //mensagem de execucao
                        JOptionPane.showMessageDialog(null, "Livro alterado com sucesso!");
                        
                    }else if (op == null){
                        //volta para o menu principal
                        menu_principal();
                    }else{
                        //caso a opcao deseja nao esteja listada, reinica o loop
                        op = null;
                    }
                }
            }
            //excluir livro por id    
            else if (opcao.equals("3")){
                //listar todos livros
                LinkedList lista = livroDAO.consultar_todos_livros();
                int id;
                //cria obj StringBuilder (para listar os livros disponíveis)
                StringBuilder sb = livroDAO.exibir_livros(lista);
                //pega o id exibindo a msg 
                String id_string = JOptionPane.showInputDialog("Lista de livros cadastrados\n" + sb.toString() + "\nDigite o ID que deseja excluir:");
                //converte o id em numero
                cancelar(id_string);
                id = Integer.parseInt(id_string); 
                
                //funcao para excluir 
                livroDAO.excluir_livro(id);
                //mensagem de execucao
                //JOptionPane.showMessageDialog(null, "Livro excluido com sucesso!");  
            }
            //consultar dados do livro por id
            else if (opcao.equals("4")){
                int id;
                //pega o id exibindo a msg
                String id_string = JOptionPane.showInputDialog("Digite o ID do livro que deseja consultar:");
                cancelar(id_string);
                //converte o id de string para int
                id = Integer.parseInt(id_string);
                //funcao para consultar livro por id
                livro = livroDAO.consultar_livro(id);
                //mensagem exibindo informacoes do livro
                JOptionPane.showMessageDialog(null, livro);

            }
            //listar todos livros
            else if (opcao.equals("5")){
                LinkedList lista = livroDAO.consultar_todos_livros();
                //cria obj StringBuilder (para listar os livros disponíveis)
                StringBuilder sb = livroDAO.exibir_livros(lista);
                //mensagem exibindo todos livros
                JOptionPane.showMessageDialog(null,"Lista de livros cadastrados\n" + sb.toString());

            }
            //retorna para o menu principal
            else if (opcao.equals("6")){
                menu_principal();
            }else{
                //caso insira uma opcao nao listada
                opcao = null;
            }
            //reiniciar o loop
            opcao = null;
        }
    }
   
    //menu de usuário
    private void menu_usuario(){
        //cria o Usuario e UsuarioDAO
        UsuarioDAO usuarioDAO = new UsuarioDAO();
        Usuario usuario = null;
        EmprestimoDAO emprestimoDAO = new EmprestimoDAO();
        //cria a opcao com valor null para entrar no loop
        String opcao = null;
        while (opcao == null) { 
            opcao = JOptionPane.showInputDialog("Escolha a opcao:\n1-Adicionar Usuário\n2-Atualizar usuário por ID\n3-Excluir usuário por ID\n4-Consultar usuário por ID\n5-Listar todos usuários\n6-Menu anterior");
            if (opcao == null) {
                // Caso o usuário cancele a entrada, retorna para o menu inicial
                menu_principal();
            }
            //insere um novo livro no banco de dados
            if (opcao.equals("1")){
                //pega os dados para inserir no obj Livro
                //cria a variavel com o nome que será exibido na tela
                String nome = "nome";
                //chama a funcao para receber o nome do cliente
                nome = verificacao(nome);
                //verifica se foi apertado o botao cancelar
                cancelar(nome);
                //cria a variavel com o nome que será exibido na tela
                String endereco = "endereco";
                //chama a funcao para receber o endereco do cliente
                endereco = verificacao(endereco);
                //verifica se foi apertado o botao cancelar
                cancelar(endereco);
                //cria a variavel com o nome que será exibido na tela
                String telefone = "telefone";
                //chama a funcao para receber o telefone do cliente
                telefone = verificacao(telefone);
                //verifica se foi apertado o botao cancelar
                cancelar(telefone);
                
                //cria o obj Usuario
                usuario = new Usuario(nome);
                usuario.setEndereco(endereco);
                usuario.setTelefone(telefone);
                //cria o obj UsuarioDAO
                usuarioDAO.inserir_usuario(usuario);
                //mensagem de execucao
                JOptionPane.showMessageDialog(null, "Usuario inserido com sucesso!");
            }
            //Atualizar usuario
            else if(opcao.equals("2")){
                //listar todos usuario
                LinkedList lista = usuarioDAO.consultar_todos_usuarios();
                int id;
                //cria obj StringBuilder (para listar os livros disponíveis)
                StringBuilder sb = usuarioDAO.exibir_usuario(lista);
                //pega o id exibindo a msg 
                String id_string = JOptionPane.showInputDialog("Lista de usuários cadastrados\n" + sb.toString() + "\nDigite o ID que deseja alterar:");
                cancelar(id_string);
                //converte o id de String para int
                id = Integer.parseInt(id_string);
                cancelar(id_string);
                //cria a variaval com valor null para entrar no loop
                String op = null;
                while (op == null){
                    op = JOptionPane.showInputDialog("O que você deseja alterar: \n1-Todos os dados \n2-Nome \n3-Endereco \n4-Telefone"); 
                    //verifica se usuario cancelou a entrada, retorna para o menu principal
                    if (op == null){
                        menu_principal();
                    }
                    else if (op.equals("1")){
                        //cria a variavel com o nome que será exibido na tela
                        String nome = "nome";
                        //chama a funcao para receber o telefone do cliente
                        nome = verificacao(nome);
                        //verifica se foi apertado o botao cancelar
                        cancelar(nome);
                        //cria a variavel com o nome que será exibido na tela
                        String endereco = "endereco";
                        //chama a funcao para receber o telefone do cliente
                        endereco = verificacao(endereco);
                        //verifica se foi apertado o botao cancelar
                        cancelar(endereco);
                        //cria a variavel com o nome que será exibido na tela
                        String telefone = "telefone";
                        //chama a funcao para receber o telefone do cliente
                        telefone = verificacao(telefone);
                        //verifica se foi apertado o botao cancelar
                        cancelar(telefone);
                        
                        //insere os dados no Usuario
                        usuario = new Usuario(nome);
                        usuario.setEndereco(endereco);
                        usuario.setTelefone(telefone);
                        //funcao para alterar o usuario
                        usuarioDAO.alterar_usuario(id, usuario);
                        //mensagem de execucao
                        JOptionPane.showMessageDialog(null, "Usuário alterado com sucesso!");
                    }
                    else if (op.equals("2")) {                   
                        //cria a variavel com o nome que será exibido na tela
                        String nome = "nome";
                        //chama a funcao para receber o telefone do cliente
                        nome = verificacao(nome);
                        //verifica se foi apertado o botao cancelar
                        cancelar(nome);
                        //funcao que altera o nome do usuario
                        usuarioDAO.alterar_nome(id, nome);
                        //mensagem de execucao
                        JOptionPane.showMessageDialog(null, "Usuario alterado com sucesso!");

                    }else if (op.equals("3")){
                        //cria a variavel com o nome que será exibido na tela
                        String endereco = "endereco";
                        //chama a funcao para receber o telefone do cliente
                        endereco = verificacao(endereco);
                        //verifica se foi apertado o botao cancelar
                        cancelar(endereco);
                        //funcao para alterar o endereco
                        usuarioDAO.alterar_endereco(id, endereco);
                        //mensagem de execucao
                        JOptionPane.showMessageDialog(null, "Usuário alterado com sucesso!");

                    }else if (op.equals("4")){
                        //cria a variavel com o nome que será exibido na tela
                        String telefone = "telefone";
                        //chama a funcao para receber o telefone do cliente
                        telefone = verificacao(telefone);
                        //verifica se foi apertado o botao cancelar
                        cancelar(telefone);
                        //funcao para alterar o telefone
                        usuarioDAO.alterar_telefone(id, telefone);
                        //mensagem de execucao
                        JOptionPane.showMessageDialog(null, "Usuário alterado com sucesso!");
                    }else {
                        //reinicia o loop caso a opcao digitada nao esteja listada
                        op = null;
                    }
                }
            }
            //excluir usuario por id    
            else if (opcao.equals("3")){
                //listar todos usuarios
                LinkedList lista = usuarioDAO.consultar_todos_usuarios();
                int id;
                //cria obj StringBuilder (para listar os usuarios disponíveis)
                StringBuilder sb = usuarioDAO.exibir_usuario(lista);
                //pega o id exibindo a msg 
                String id_string = JOptionPane.showInputDialog("Lista de usuários cadastrados\n" + sb.toString() + "\nDigite o ID que deseja excluir:");
                cancelar(id_string);
                id = Integer.parseInt(id_string);  
                
                usuarioDAO.excluir_usuario(id); 
                //JOptionPane.showMessageDialog(null, "Usuário excluido com sucesso!");  
               

            //consultar dados do usuário por id
            }else if (opcao.equals("4")){
                int id;
                //recebe o id exibindo a mensagem 
                String id_string = JOptionPane.showInputDialog("Digite o ID do usuario que deseja consultar:");
                cancelar(id_string);
                //converte o id String em int
                id = Integer.parseInt(id_string);
                //funcao para consultar usuario
                usuario = usuarioDAO.consultar_usuario(id);
                //mensagem exibindo as informacoes do usuario
                JOptionPane.showMessageDialog(null, usuario);
            }
            //listar todos usuarios
            else if (opcao.equals("5")){
                //listar todos livros
                LinkedList lista = usuarioDAO.consultar_todos_usuarios();
                //cria obj StringBuilder (para listar os usuarios)
                StringBuilder sb = usuarioDAO.exibir_usuario(lista);
                //exibe a mensagem com as informacoes 
                JOptionPane.showMessageDialog(null,"Lista de usuarios cadastrados\n" + sb.toString());

            }else if (opcao.equals("6")){
                menu_principal();;
            }else{
                //reinicia o loop caso a opcao nao esteja listada
                opcao = null;
            }
            //manter o loop ativo
            opcao = null;
        }
    }

    private void menu_emprestimo(){
        EmprestimoDAO emprestimoDAO = new EmprestimoDAO();
        Emprestimo emprestimo = null;
        LivroDAO livroDAO = new LivroDAO();
        Livro livro = null;
        UsuarioDAO usuarioDAO = new UsuarioDAO();
        Usuario usuario = null;

        String opcao = null;
        while (opcao == null) { 
            opcao = JOptionPane.showInputDialog("Escolha a opcao:\n1-Realizar empréstimo\n2-Devolução de livro ID\n3-Histórico de emprestimos de usuario por ID\n4-Consultar empréstimo ativos\n5-Consultar emprestimos atrasados\n6-Excluir emprestimo por ID\n7-Menu anterior");
            //verifica se usuario cancelou a entrada
            cancelar(opcao);
            //insere um novo emprestimo
            if (opcao.equals("1")){
                //pega os dados para inserir no obj Emprestimo
                //listar todos livros
                LinkedList lista_livro = livroDAO.consultar_todos_livros();
                int id_livro;
                //cria obj StringBuilder (para listar os livros disponíveis)
                StringBuilder sb = livroDAO.exibir_livros(lista_livro);
                //pega o id_Livro exibindo a msg 
                
                String id_livro_string = JOptionPane.showInputDialog("Lista de livros cadastrados\n" + sb.toString() + "\nDigite o ID do livro que deseja emprestar:");
                cancelar(id_livro_string);
                id_livro = Integer.parseInt(id_livro_string);
                //listar todos usuarios
                LinkedList lista_usuario = usuarioDAO.consultar_todos_usuarios();
                int id_usuario;
                //cria obj StringBuilder (para listar os livros disponíveis)
                StringBuilder sb1 = usuarioDAO.exibir_usuario(lista_usuario);
                //pega o id_Livro exibindo a msg 
                String id_usuario_string = JOptionPane.showInputDialog("Lista de usuários cadastrados\n" + sb1.toString() + "\nDigite o ID do usuário que deseja emprestar:");
                cancelar(id_usuario_string);
                id_usuario = Integer.parseInt(id_usuario_string);
                //pega a data atual
                String data_atual = data_string(data_atual());
                //gera a data de devolucao para 5 dias apos o cadastro
                LocalDate data_devolucao_date = data_devolucao(data_atual(), 5);

                String data_devolucao = data_string(data_devolucao_date);

                //cria o obj Emprestimo
                emprestimo = new Emprestimo(id_livro);
                emprestimo.setIdUsuario(id_usuario);
                emprestimo.setEmprestimo(true);
                emprestimo.setDataEmprestimo(data_atual);
                emprestimo.setDevolucao(data_devolucao);
                //cria o obj UsuarioDAO
                emprestimoDAO.emprestimo(emprestimo);
                JOptionPane.showMessageDialog(null, "Emprestimo cadastrado com sucesso!");

            //devolver livro
            }else if(opcao.equals("2")){
                //listar todos usuario
                LinkedList<ArrayList<Object>> lista = emprestimoDAO.emprestimos_ativos();
                int id;
                //cria obj StringBuilder (para listar os emprestimos)
                StringBuilder sb = emprestimoDAO.exibir_emprestimos(lista);
                //pega o id exibindo a msg 
                
                String id_string = JOptionPane.showInputDialog("Lista de livros emprestados\n" + sb.toString() + "\nDigite o ID que deseja alterar:");
                cancelar(id_string);
                id = Integer.parseInt(id_string);
                emprestimoDAO.devolver(id);
                JOptionPane.showMessageDialog(null, "Livro devolvido com sucesso!");

                
            //Consultar historico de cliente   
            }else if (opcao.equals("3")){
                //listar todos usuarios
                LinkedList<Usuario> lista = usuarioDAO.consultar_todos_usuarios();
                
                int id;
                //cria obj StringBuilder (para listar os usuarios disponíveis)
                StringBuilder sb = usuarioDAO.exibir_usuario(lista);
                //pega o id exibindo a msg 
                String id_string = JOptionPane.showInputDialog("Lista de usuários cadastrados\n" + sb.toString() + "\nDigite o ID que deseja consultar o historico:");
                cancelar(id_string);   
                id = Integer.parseInt(id_string); 
                LinkedList lista_historico = emprestimoDAO.historico_id(id);
                StringBuilder sb1 = emprestimoDAO.exibir_emprestimos(lista_historico);

                JOptionPane.showMessageDialog(null, sb1);  

            //listar todos emprestimos ativos
            }else if (opcao.equals("4")){
                LinkedList<ArrayList<Object>> lista = emprestimoDAO.emprestimos_ativos();

                StringBuilder sb = emprestimoDAO.exibir_emprestimos(lista);

                JOptionPane.showMessageDialog(null, sb);

            //listar emprestimos atrasados com multa
            }else if (opcao.equals("5")){
                String data = data_string(data_atual());
                //valor da multa por dia
                float multa = 5;
                LinkedList<ArrayList<Object>> lista = emprestimoDAO.emprestimos_atrasados(data, multa);

                StringBuilder sb;
                sb = emprestimoDAO.multa_atraso(lista);

                JOptionPane.showMessageDialog(null, sb);

            }else if (opcao.equals("6")){
                LinkedList<ArrayList<Object>> lista = emprestimoDAO.exibir_todos_emprestimos();

                StringBuilder sb = emprestimoDAO.exibir_emprestimos(lista);
                
                String id_string = JOptionPane.showInputDialog("Emprestimos cadastrados\n" + sb.toString() + "\nDigite o ID que deseja consultar o excluir:");
                cancelar(id_string);
                int id = Integer.parseInt(id_string); 
                cancelar(id_string);   
                emprestimoDAO.excluir_emprestimo(id);
                JOptionPane.showMessageDialog(null, "Emprestimo excluido com sucesso");
            
            }else if (opcao.equals("7")){
                menu_principal();
            }else {
                opcao = null;
            }
            //manter o loop
            opcao = null;
        }
    }
}
