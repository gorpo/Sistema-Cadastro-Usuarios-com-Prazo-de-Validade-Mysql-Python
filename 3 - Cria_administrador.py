import pymysql.cursors

#faz a conexao com o banco de dados
conexao = pymysql.connect(host = 'localhost',
                          user = 'root',
                          password = '',
                           db = 'aula',
                          charset = 'utf8mb4',
                          cursorclass = pymysql.cursors.DictCursor)



with conexao.cursor() as cursor:          # faz a conexao com o cursor do mysql
    cursor.execute(f"insert into usuarios values ('admin','admin','2','20/05/3000')")
    conexao.commit()                     #gravação do comando no banco de dados