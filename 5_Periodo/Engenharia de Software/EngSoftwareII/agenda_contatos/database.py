import pymysql

class Conexao:
    _instancia = None
    _conexao = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Conexao, cls).__new__(cls)
            try:
                cls._conexao = pymysql.connect("agenda")  
                print("Conexão com o banco de dados estabelecida.")
            except pymysql.Error as e:
                print(f"Erro ao conectar com o banco de dados: {e}")
        return cls._instancia

    def get_conexao(self):
        return self._conexao