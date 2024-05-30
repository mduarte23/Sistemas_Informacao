import mysql.connector

class BancoDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='127.0.0.1', user='root', passwd='98245803', database= 'poo')
        self.cursor = self.conexao.cursor()

        #cria a tabela 'cliente' se nao existir
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS empresa(
                                id INT PRIMARY KEY AUTO_INCREMENT,
	                            nome VARCHAR(75) NOT NULL,
	                            endereco VARCHAR(50) NOT NULL,
	                            contato VARCHAR(50) NOT NULL,
	                            ramo VARCHAR(50) NOT NULL,
	                            telefone VARCHAR(25) NOT NULL
                            )
                            
                        """)
    
    def inserir_empresa(self, empresa):
        self.cursor.execute("""
            INSERT INTO empresa (nome, endereco, contato, ramo, telefone)
            VALUES (%s,%s,%s, %s, %s)
        """, (empresa.nome, empresa.endereco, empresa.contato, empresa.ramo, empresa.telefone))
        self.conexao.commit()

    def listar_empresas(self):
        self.cursor.execute("""
            SELECT id, nome, endereco, contato, ramo, telefone FROM empresa            
        """)
        return self.cursor.fetchall()
    
    def atualizar_empresa(self, empresa, empresa_id):
        self.cursor.execute("""
            UPDATE empresa SET
                nome = %s,
                endereco = %s,
                contato = %s,
                ramo = %s,
                telefone = %s
            WHERE id = %s
        """, (empresa.nome, empresa.endereco, empresa.contato, empresa.ramo, empresa.telefone, empresa_id))
        self.conexao.commit()

    def deletar_empresa(self, empresa_id):
        self.cursor.execute("""
            DELETE FROM empresa WHERE id = %s
        """, (empresa_id,))
        self.conexao.commit()