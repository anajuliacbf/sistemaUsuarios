
# O sistema de login deve permitir que novos usuários 
# sejam cadastrados, e que usuários existentes possam 
# fazer o login. O sistema deve alertar caso a senha 
# e login não estejam corretos.

# O sistema de login deve permitir que novos usuários sejam cadastrados
# O sistema não deve permitir que usuários duplicados sejam cadastrados
# Permitir que usuários existentes possam fazer o login
# O sistema deve alertar caso a senha e login não estejam corretos


'''
# O sistema de login deve permitir que novos usuários sejam cadastrados
1. Quais são os dados de entrada necessários?
    - usuário e senha
2. O que devo fazer com estes dados?
    - eu devo registrar usuário e senha que foi digitado
3. Quais são as restrições deste problema?
    - não devo permitir cadastro de usuários já existentes
4. Qual é resultado esperado?
    - um novo usuário e senha
5. Qual é a sequëncia de passos necessárias para chegar
ao resultado final?
    - receber o usuário
    - receber a senha
    - verificar se o usuário já existe
    - caso não exista, cadastrar aquele usuário e senha
'''

# Permitir que usuários existentes possam fazer o login
resposta = input('[1] - Cadastrar novo usuário [2] - Fazer login: ')
# armazenando os usuários existentes
usuarios = ['carol','amanda','jeff']
senhas = ['123456','abcdef','123abcd']

if resposta =='1':
    # recebendo um usuário
    usuario_digitado = input('Digite seu usuário: ')
    # O sistema não deve permitir que usuários duplicados sejam cadastrados
    if usuario_digitado in usuarios:
        print('usuário existente')
    else:
        # recebendo uma senha
        senha_digitada = input('Digite sua senha: ')
        # caso não exista, cadastrar aquele usuário e senha
        usuarios.append(usuario_digitado) #append = adicionar
        senhas.append(senha_digitada)
elif resposta == '2':
    # Permitir que usuários existentes possam fazer o login   
    # pedir usuário
    usuario_digitado = input('Digite seu usuário: ')
    #pedir senha
    senha_digitada = input('Digite sua senha: ')
    # preciso verificar se a senha providenciada para aquele
    # usuário é a mesma senha que está na lista de senhas
    encontrado = False
    for indice, usuario in enumerate(usuarios):
       if usuario_digitado == usuario and senha_digitada == senhas[indice]: #mt importante
           print('Login feito com sucesso.')
           encontrado = True
       elif encontrado == False:
            # O sistema deve alertar caso a senha e login não estejam corretos 
            print('usuário ou senha incorretos.')
else:
    print('Digite apenas 1 ou 2.')