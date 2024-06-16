public class MainDB {
    public static void main(String[] args) {
        Livro liv = new Livro("O senhor dos anéis");
        liv.setAutor("J. R. R. Tolkien");
        liv.setAnoPublicacao(1953);

        LivroDAO objDAO = new LivroDAO();
        objDAO.inserir(liv);

        Usuario user = new Usuario("Matheus");
        user.setEmail("matheus@gmail.com");

        UsuarioDao userDao = new UsuarioDao();
        userDao.inserir(user);
        }        
    }
