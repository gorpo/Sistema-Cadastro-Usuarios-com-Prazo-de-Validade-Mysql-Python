import pymysql.cursors
from datetime import date


#cria conexao com banco de dados
conexao = pymysql.connect(host = 'localhost',
                          user= 'root',
                          password='',
                          db='aula',
                          charset='utf8mb4', cursorclass= pymysql.cursors.DictCursor )

#define todos usuarios e adms como não autenticado
autenticado = False





def logarcadastrar(autenticado):



    #sistema de login --------------------->
    if decisao == 1:
        nome = input('nome:')
        senha= input('senha:')
        # loop varrendo todas linhas da tabela usuarios no banco de dados
        for linha in resultado:
            #se usuario e senha inseridos forem igual usuario e senha do banco de dados
            if nome == linha['nome'] and senha == linha['senha']:
                # se nivel de usuario = 1 loga como user normal
                if linha['nivel'] == 1:
                    administrador = False
                #se nivel de usuario = 2  loga como administrador
                elif linha['nivel'] == 2:
                    administrador = True
                #permite autenticar setando como True, caso contrário sempre será False a autenticaçao
                autenticado = True
                break
            else:
                autenticado = False
        if not autenticado:
            print('usuario ou senha invalido')




    #cadastrar usuarios------------------------------------------------------------------------------->
    elif decisao == 2:
        usuarioexistente = 0
        print('Area de cadastro')
        nome = input('usuario:')
        senha = input('senha:')
        data_expiracao = input('data de expiração:')
        #loop varrendo todas linhas da tabela usuarios no banco de dados
        for linha in resultado:
            # se usuario e senha inseridos forem igual usuario e senha do banco de dados
            if nome == linha['nome'] and senha == linha['senha']:
                #define que usuario ja existe para nao ter cadastros repetidos
                usuarioexistente = 1
        if usuarioexistente == 1:
            print('Usuario ja cadastrado, tente nome ou senha diferente.')
            administrador = False
        # se nome e senha de usuarios nao existem no servidor cadastra
        elif usuarioexistente == 0:
            try:
                #faz a conexao com o cursor do mysql
                with conexao.cursor() as cursor:
                    #codigo mysql para ser executado inserindo dentro da tabela usuarios os valores de nome, senha, nivel, e expiraçao
                    cursor.execute(f"insert into usuarios values ('{nome}','{senha}','1','{data_expiracao}')")
                    #grava os dados no banco de dados
                    conexao.commit()
                print('usuario cadastrado com sucesso')
                administrador = False
            except:
                print('erro ao inserir os dados')





    #deletar usuarios------------------------------------------------------------------------------------>
    elif decisao == 3:
        try:
            # faz a conexao com o cursor do mysql
            with conexao.cursor() as cursor:
                print('deletar usuarios')
                usuario = input('usuario:')
                #codigo mysql para ser executado
                usuario = f"DELETE FROM usuarios WHERE nome='{usuario}';"
                #executa o codigo mysql no banco de dados
                cursor.execute(usuario)
                #grava o codigo no banco de dados
                conexao.commit()
                print('usuario deletado com sucesso')
                administrador = False
        except:
            print('ocorreu um erro')
    #retorna o valor de autenticado True ou False para podermos seguir com o sistema
    #retorna True ou False para administrador, para saber se é um adm ou nao!

    return autenticado, administrador










#se os usuarios nao estao autenticados--------------------------------->
while not autenticado:
    decisao = int(input('1 para logar 2 para cadastrar 3 para deletar'))
    try:
        # faz a conexao com o cursor do mysql
        with conexao.cursor() as cursor:
            # seleciona tudo da tabela usuarios
            cursor.execute('select * from usuarios')
            #armazena todos os dados selecionados da tabela usuarios em uma variavel
            resultado = cursor.fetchall()
            #print(resultado)
    except:
        print('erro ao conectar ao banco de dados')


    #inicia o sistema de logar cadastrar e deletar usuarios-------->>
    autenticado, administrador = logarcadastrar(autenticado)



#se os usuarios ou adms estao autenticados---------------------------->
if autenticado:
    #verifica a validade do programa
    for linha in resultado:
        #pega o dia de hoje na maquina, trocar isto por uma data -global-
        hoje = date.today()
        #se o dia for igual o dia que esta como prazo de expiração no banco de dados, nao permite mais o uso do programa
        if hoje.strftime("%d/%m/%Y") == linha['data']:
            print('tempo de uso expirado')
    # se for um administrador logado, aqui começará a parte que os administradores terao acesso
    if administrador == True:
        print('insira a programaçao voltada ao administrador aqui')
    # se for um usuario logado, aqui começa a parte que usuarios logados terao acesso
    if administrador == False:
        print('insira a programaçao voltada ao usuario aqui')



#========================== FIM DO CODIGO =====================================





