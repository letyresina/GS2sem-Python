'''
    Autora: Leticia Resina
    Objetivo do código: simular a inteligência artificial Julia do projeto MyHealth com funcionalidades 
    reduzidas, mas que condizem o mais próximo da solução final.
'''

# Imports

import time # intervalo de tempo para o usuário poder visualizar e processar as informações
import getpass # simular a entrada de senha de uma maneira segura (neste primeiro momento)
import bcrypt # criptografar senha, a nível de garantir integridade e segurança do usuário
import json # para abrir arquivos json externos da aplicação

# Variáveis que precisam ser criadas antes da inicialização do programa

#  Essa variável é somente um EXEMPLO não sendo necessariamente real -> por agora a nível de teste
conveniosParceiros = {
    'SUS',
    'HapVida',
    'Transmontano'
}

# Variável com os gêneros que existem, pensando na questão de melhor atendimento tanto da IA quanto nos atendimentos -> facilita na visualização dos exames e prescição de receitas
generos = {
    "Homem cis",
    "Homem trans",
    "Mulher cis",
    "Mulher trans",
    "Não-binário"
}

# Variável com dicas de saúde física
saudeFisica = {
    "1. Alimentação balanceada: Consuma uma variedade de alimentos, incluindo frutas, vegetais, grãos integrais, proteínas magras e gorduras saudáveis para garantir a ingestão de nutrientes essenciais;",
    "2. Atividade Física Regular: Pratique exercícios regularmente, incluindo atividades aeróbicas, treinamento de força e flexibilidade, para manter um corpo saudável e fortalecer o sistema cardiovascular e musculoesquelético;",
    "3. Hidratação Adequada: Beba água suficiente ao longo do dia para manter o corpo hidratado e apoiar funções metabólicas adequadas;",
    "4. Sono Reparador: Estabeleça uma rotina de sono consistente, visando 7-9 horas por noite, para promover a recuperação física e mental;",
    "5. Check-ups Regulares: Faça exames médicos de rotina e consulte profissionais de saúde regularmente para prevenção e detecção precoce de possíveis problemas de saúde."
}

# Variável com dicas de saúde mental
saudeMental = {
    "1. Prática de Mindfulness: Dedique tempo para a prática de mindfulness ou meditação, o que pode ajudar a reduzir o estresse, melhorar a concentração e promover o bem-estar emocional;",
    "2. Equilíbrio Trabalho-Vida: Estabeleça limites saudáveis entre trabalho e vida pessoal, reservando tempo para atividades recreativas e relacionamentos sociais;",
    "3. Compartilhamento de Sentimentos: Não hesite em falar sobre seus sentimentos com amigos, familiares ou um profissional de saúde mental, promovendo a expressão emocional e o suporte necessário;"
    "4. Atividades Recreativas: Reserve tempo para atividades que lhe tragam prazer e relaxamento, seja ler, ouvir música, praticar um hobby ou fazer atividades ao ar livre;",
    "5. Definição de Metas Realistas: Estabeleça metas alcançáveis para evitar sobrecarga e promover um senso de realização. Lembre-se que cada pessoa é única!"
}

# Variável com dicas de saúde social
saudeSocial = {
    "1. Criação de Vínculos Sociais: Cultive relacionamentos positivos e significativos, mantendo contato regular com amigos, familiares e comunidade;",
    "2. Empatia e Compaixão: Pratique a empatia ao se colocar no lugar dos outros e cultive a compaixão, promovendo um ambiente social mais saudável;",
    "3. Participação em Grupos Sociais: Junte-se a grupos ou comunidades que compartilhem seus interesses, promovendo um senso de pertencimento e apoio mútuo;",
    "4. Limitação do Uso de Redes Sociais: Utilize as redes sociais de maneira consciente, evitando comparações prejudiciais e limitando o tempo online para promover interações sociais face a face;",
    "5. Voluntariado e Ativismo: Participe de atividades voluntárias ou de causas sociais que você valoriza, contribuindo para um senso de propósito e impacto positivo na comunidade."
}

# Funções

def cadastro():
    """
        Função utilizada para simular o cadastro dentro da aplicação. Dentro dessa função, é simulado também
        a questão da integridade e segurança dos dados do usuário, ocultando a senha e criptografando em seguida.
    """

    # abre o arquivo para manter os dados anteriormente inseridos
    with open('usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)

    email: str = input("Digite seu e-mail: ")
    usuarioExiste = False
    for usuario in usuarios:
         if usuario['email'] == email: # Caso o usuário já tenha seu email cadastrado em nosso sistema
            usuarioExiste = True
            print("O email já está registrado em nosso sistema! Por favor, realize seu login com email e senha!")
            time.sleep(1)
              
    if not usuarioExiste: # Caso o usuário não tenha seu email cadastrado em nosso sistema
        nome: str = input("Digite seu nome completo: ").title()
        time.sleep(1)

        apelido: str = input("Digite como deseja ser chamado durante a nossa conversa: ").title()
        time.sleep(1)

        print("Para algumas questões na área da saúde, como por exemplo, resultados de exames e prescrição de medicamentos, é necessário sabermos seu gênero para melhor conduzirmos seus resultados.")
        print("Como você se identifica em termos de gênero?")
        for genero in generos:
            print(f"- {genero}")

        genero: str = input("Digite uma das opções acima: ")

        print("Você é um profissional na área da saúde?")
        print("\n 1 - Sim \n 2 - Não, sou paciente \n")

        try: # Validação de erro evitando 
            profissionalSaude: int = int(input("Informe a opção aqui: "))
            if (profissionalSaude < 1) or (profissionalSaude > 2):
                raise TypeError
            elif profissionalSaude == 1: # caso sim
                print("Qual a sua especialidade? Digite somente a especialidade, como exemplo Psicológo.")
                especialidade: str = input()
                print("Mais perguntas serão feitas ao decorrer da aplicação")

                print("Confira nossos convênios parceiros")
                for convenio in conveniosParceiros:
                    print(f"- {convenio}")
                
                convenioUser: str = input("Informe seu convênio aqui (mesmo que não seja parceiro (mesmo que não seja parceiro e por extenso como 'hapvida notredame intermédica'): ").lower()

                conveniosParceirosLower = {convenio.lower() for convenio in conveniosParceiros}

                if convenioUser in conveniosParceirosLower:
                    numConvenio: int = int(input("Digite seu número de cadastro: "))

                else:
                    print(f"O convênio {convenioUser} não faz parte dos nossos parceiros. Entretanto, te avisaremos caso a parceria seja feita!")
                    numConvenio: int = int(input("Digite seu número de cadastro, facilitará caso a parceria seja realizada: "))

                senha: str = getpass.getpass("Digite sua senha (ela está ocultada pela sua segurança): ")
                time.sleep(1)

                salt = bcrypt.gensalt() # gera um salt aleatório

                hashSenha = bcrypt.hashpw(senha.encode("utf-8"), salt)
                hashSenhaString = hashSenha.decode('utf-8')

                cadastro = {
                    "nome": nome,
                    "apelido": apelido,
                    "email": email,
                    "genero": genero,
                    "profissional": profissionalSaude,
                    "especialidade": especialidade,
                    "convenio": convenioUser,
                    "numero convenio": numConvenio,
                    "senha": hashSenhaString
                }

            elif profissionalSaude == 2: # Caso não
                print("Confira nossos convênios parceiros")
                for convenio in conveniosParceiros:
                    print(f"- {convenio}")
                
                convenioUser: str = input("Informe seu convênio aqui (mesmo que não seja parceiro e por extenso como 'hapvida notredame intermédica'): ").lower()

                conveniosParceirosLower = {convenio.lower() for convenio in conveniosParceiros}

                if convenioUser in conveniosParceirosLower:
                    numConvenio: int = int(input("Digite seu número de cadastro: "))

                else:
                    print(f"O convênio {convenioUser} não faz parte dos nossos parceiros. Entretanto, te avisaremos caso a parceria seja feita!")
                    numConvenio: int = int(input("Digite seu número de cadastro, facilitará caso a parceria seja realizada: "))

                senha: str = getpass.getpass("Digite sua senha (ela está ocultada pela sua segurança): ")
                time.sleep(1)

                salt = bcrypt.gensalt() # gera um salt aleatório

                hashSenha = bcrypt.hashpw(senha.encode("utf-8"), salt)
                hashSenhaString = hashSenha.decode('utf-8')

                
                cadastro = {
                    "nome": nome,
                    "apelido": apelido,
                    "email": email,
                    "genero": genero,
                    "profissional": profissionalSaude,
                    "convenio": convenioUser,
                    "cadastro convenio": numConvenio,
                    "senha": hashSenhaString
                }

            usuarios.append(cadastro)

            with open('usuarios.json', 'w', encoding='utf-8') as arquivoJSON:
                    json.dump(usuarios, arquivoJSON, indent=4, ensure_ascii=False)

            print("Cadastro feito com sucesso! Basta realizar seu login para acessar a Julia!")
            time.sleep(1)
            return cadastro

        except ValueError: # caso valor diferente de inteiro
            print("Por favor, informe somente números dentre as opções disponíveis!")
            time.sleep(1)
            
        except TypeError: # caso opção não existente no sistema
            print("Por favor, digite uma opção válida para prosseguir.")
            time.sleep(1)

def login():
    """
        Função criada para simular o login do usuário através do arquivo JSON contendo os dados dos usuários
        e a senha criptografada, em que o próprio sistema consegue descriptografar e fazer o acesso caso os dados
        estejam corretos.
    """

    with open('usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)
        
    global apelidoUsuario # Para facilitar comunicação com o usuário logado
    global emailUsuario # Para facilitar pegar o email nas demais funções
    global profissional

    encontrouUsuario = False
    senhaCorreta = False
    
    email: str = input("Digite seu email: ")

    for usuario in usuarios:
        emailUsuario = usuario['email']
        if emailUsuario == email:
            encontrouUsuario = True
            senha: str = getpass.getpass("Digite sua senha: ")
            if bcrypt.checkpw(senha.encode("utf-8"), usuario["senha"].encode("utf-8")):
                apelidoUsuario = usuario["apelido"]
                profissional = usuario["profissional"]
                time.sleep(1)
                print(f"Bem-vindo, {apelidoUsuario}!")  
                senhaCorreta = True
                return True
            
    if not encontrouUsuario: # caso não exista esse cadastro em nosso sistema
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        time.sleep(1)
        return False
    
    if encontrouUsuario and not senhaCorreta: # Caso exista o email mas a senha está incorreta
        print("A senha está incorreta! Tente novamente!")
        time.sleep(1)
        return False

def feedback():
    """
        Função criada para simular a inserção de feedback dos usuários e ficar salvo num banco de dados
        (nesse caso, um arquivo JSON) de forma anônima, garantindo maior espaço para usuários se expressarem.
    """
    with open('feedback.json', 'r', encoding='utf-8') as arquivo:
        feedbacks = json.load(arquivo)

    print("Todos os feedbacks são anônimos, não se preocupe!")
    feedbackUser: str = input("Informe seu feedback sobre a Julia aqui: ")

    # Chave inteira para rotas favoritas -> para facilitar a identificação de cada rota
    chave = 1

    if feedbacks:
        chavesInt = [int(chave) for chave in feedbacks.keys()]  # Preciso transformar em inteira para fazer a soma
        chave = str(max(chavesInt) + 1)  # Depois de somar, transformo para string para cadastrar na nova rota

    novoFeedback = {
        "Feedback": feedbackUser
    }

    feedbacks[chave] = novoFeedback  # Cadastro a nova rota dentro da chave

    with open('feedback.json', 'w', encoding='utf-8') as arquivo:
        json.dump(feedbacks, arquivo, indent=4, ensure_ascii=False)

    print("Feedback enviado com sucesso!")

def dicasSaude():
    """
        Função criada para facilitar a mostragem de dicas de saúde!
    """
    print("A saúde é dividida em 3 grandes áreas: física, mental e social.")
    time.sleep(1)
    print("Uma vida saudável significa ter o equiilibrio nessas 3 áreas em nossa vida. Vamos ver as dicas de cada uma delas para nos auxiliar no nosso dia a dia?")
    time.sleep(0.5)

    print("Dicas para saúde física:")
    for dicaF in saudeFisica:
        print(dicaF)
        time.sleep(1)
    
    print("Dicas para saúde mental:")
    for dicaM in saudeMental:
        print(dicaM)
        time.sleep(1)

    print("Dicas para saúde social:")
    for dicaS in saudeSocial:
        print(dicaS)
        time.sleep(1)

def menuOpcoesProfissional():
    """
        Função criada para o menu de opções para profissionais na área da saúde, facilitando o tratamento de erros
        e deixar o código mais limpo na parte da programação principal.
    """
    print("Como podemos te ajudar hoje?")
    print("\n 1 - Agendar uma consulta \n 2 - Resultado de exames de um paciente \n 3 - Lembretes de remédios \n 4 - Visualizar agenda \n 5 - Dicas de saúde \n 6 - Feedback sobre a Julia \n 7 - Registro de sintomas \n 8 - Psicológos na sua área \n 9 - Encerrar Julia")    
    try:
        opcao = int(input("Informe a opção desejada: "))
        if (opcao < 1) or (opcao > 9):
            raise TypeError
        return opcao
    except ValueError:
        print("Por favor, informe somente números dentre as opções disponíveis!")
        time.sleep(1)
    except TypeError:
        print("Por favor, digite uma opção válida para prosseguir.")
        time.sleep(1)

def menuOpcoesPaciente():
    """
        Função criada para o menu de opções para pacientes, facilitando o tratamento de erros
        e deixar o código mais limpo na parte da programação principal.
    """
    print("Como podemos te ajudar hoje?")
    print("\n 1 - Agendar consultas; \n 2 - Visualizar resultado de exames \n 3 - Lembretes de remédios \n 4 - Visualizar agenda de consultas \n 5 - Dicas de saúde \n 6 - Feedback sobre a Julia \n 7 - Registro de sintomas \n 8 - Psicológos na sua área \n 9 - Encerrar Julia")
    try:
        opcao = int(input("Informe a opção desejada: "))
        if (opcao < 1) or (opcao > 9):
            raise TypeError
        return opcao
    except ValueError:
        print("Por favor, informe somente números dentre as opções disponíveis!")
        time.sleep(1)
    except TypeError:
        print("Por favor, digite uma opção válida para prosseguir.")
        time.sleep(1)

# Programa principal

'''
    Enquanto o usuário não tiver logado, o usuário não poderá acessar as demais funcionalidades da aplicação
    segundo o estudo de caso e requisitos da aplicação definido pela PulseTech.
'''

logado = False # para facilitar construção do programa

while logado == False:
    print("Olá! Seja bem vindo(a) à Julia! Para prosseguir, é necessário que você esteja logado em nosso sistema!")
    print("Escolha a opção abaixo para continuar")
    print("\n 1 - Login \n 2 - Cadastro \n 3 - Encerrar à Julia \n")
    try: # Tratamento de erros para evitar paradas inesperadas durante o programa
        opcaoInicial = int(input("Escolha uma das opções acima: "))

        if (opcaoInicial < 1) or (opcaoInicial > 3):
            raise TypeError
        
        elif opcaoInicial == 1:
            # Opção de login
            loginUsuario = login()
            time.sleep(1)
            if loginUsuario == True: # caso deu tudo certo no login (não houve nenhum dado errado!)
                logado = True

        elif opcaoInicial == 2:
            # Opção de cadastro
            cadastro()
            time.sleep(1)
            print("Faça seu login, para sua segurança, para prosseguir com à Julia")
            loginUsuario = login()
            time.sleep(1)
            if loginUsuario == True: # caso deu tudo certo no login (não houve nenhum dado errado!)
                logado = True        
            
        elif opcaoInicial == 3:
            # Encerra a Julia sem continuar com as funcionalidades
            print("Agradecemos por utilizar à Julia!")
            break

    except ValueError:
        print("Por favor, informe somente números dentre as opções disponíveis!")
        time.sleep(1)

    except TypeError:
        print("Por favor, digite uma opção válida para prosseguir.")
        time.sleep(1)

if logado == True:
    print(f"Olá, {apelidoUsuario}. Seja bem-vindo(a) à Julia")
    while True:
        if profissional == 1:
            opcao = menuOpcoesProfissional()
            if opcao == 1:
                # Agendar uma consulta para profissionais na área
                print("Teste")
            elif opcao == 2:
                # Resultados de exame de um paciente
                print("Teste")
            elif opcao == 3:
                # Lembretes de remédios
                print("Teste")
            elif opcao == 4:
                # Visualizar agenda
                print("Teste")
            elif opcao == 5:
                # Dicas de saúde
                dicasSaude()
            elif opcao == 6:
                # Feedback sobre a Julia
                feedback()
            elif opcao == 7:
                # Registro de sintomas
                print("Teste")
            elif opcao == 8:
                # Psicológos na sua área
                print("Teste")
            elif opcao == 9:
                # Encerrando a Julia
                print("Obrigada por utilizar a Julia!")
                print("Deslogando...")
                time.sleep(1)
                break
        
        elif profissional == 2:
            opcao = menuOpcoesPaciente()
            if opcao == 1:
                # Agendar uma consulta
                print("Teste")
            elif opcao == 2:
                # Visualizar resultados de exames
                print("Teste")
            elif opcao == 3:
                # Lembretes de remédios
                print("Teste")
            elif opcao == 4:
                # Visualizar consultas marcadas
                print("Teste")
            elif opcao == 5:
                # Dicas de saúde
                dicasSaude()
            elif opcao == 6:
                # Feedback sobre a Julia
                feedback()
            elif opcao == 7:
                # Registros de sintomas
                print("Teste")
            elif opcao == 8:
                # Psicológos na sua área
                print("Teste")
            elif opcao == 9:
                # Encerrando a Julia
                print("Obrigada por utilizar a Julia!")
                print("Deslogando...")
                time.sleep(1)
                break