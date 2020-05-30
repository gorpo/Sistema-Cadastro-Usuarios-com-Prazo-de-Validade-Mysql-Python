import pymysql.cursors



#faz a conexao com o banco de dados
conexao = pymysql.connect(host = 'localhost',
                          user = 'root',
                          password = '',
                          db = 'aula',
                          charset = 'utf8mb4',
                          cursorclass = pymysql.cursors.DictCursor)


with conexao.cursor() as cursor:          # faz a conexao com o cursor do mysql
    tabela = f'create table usuarios ({"nome varchar(50), senha varchar(50), nivel int not null, data varchar(10)"})'
    cursor.execute(tabela)               #execução do comando no banco de dados
    conexao.commit()                     #gravação do comando no banco de dados

