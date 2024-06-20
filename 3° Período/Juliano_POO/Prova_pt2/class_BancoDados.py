import sqlite3
class BancoDados:
    def __init__(self):
        self.conexao = sqlite3.connect('filme.db')
        self.cursor = self.conexao.cursor()
        # Cria a tabela 'filmes' se não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filme (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano TEXT NOT NULL,
                genero TEXT NOT NULL,
                runtime TEXT NOT NULL,
                diretor TEXT NOT NULL
            )
        """)
    def inserir_filme(self, filme):
        self.cursor.execute("""
            INSERT INTO filme (titulo, ano, genero, runtime, diretor)
            VALUES (?, ?, ?, ?, ?)
        """, (filme.titulo, filme.ano, filme.genero, filme.runtime, filme.diretor))
        self.conexao.commit()

    def listar_filmes(self):
        self.cursor.execute("""
            SELECT id, titulo, ano, genero, runtime, diretor FROM filme
        """)
        return self.cursor.fetchall()

    def atualizar_filme(self, filme, filme_id):
        self.cursor.execute("""
            UPDATE filme SET
                titulo = ?,
                ano = ?,
                genero = ?,
                runtime = ?,
                diretor = ?
            WHERE id = ?
        """, (filme.titulo, filme.ano, filme.genero, filme.runtime, filme.diretor, filme_id))
        self.conexao.commit()

    def deletar_filme(self, filme_id):
        self.cursor.execute("""
            DELETE FROM filme WHERE id = ?
        """, (filme_id,))
        self.conexao.commit()