import pymysql.cursors



#faz a conexao com o banco de dados
conexao = pymysql.connect(host = 'localhost',
                          user = 'root',
                          password = '',
                          charset = 'utf8mb4',
                          cursorclass = pymysql.cursors.DictCursor)



with conexao.cursor() as cursor:                    # faz a conexao com o cursor do mysql
    tabela = 'create database aula'                 #comando mysql  a ser executado
    cursor.execute(tabela)                          #execução do comando no banco de dados
    conexao.commit()                                #gravação do comando no banco de dados