'''
    Autora: Leticia Resina
    Objetivo do código: simular a inteligência artificial Julia do projeto MyHealth com funcionalidades 
    reduzidas, mas que condizem o mais próximo da solução final.
'''

# Imports

import time # intervalo de tempo para o usuário poder visualizar e processar as informações
import getpass # simular a entrada de senha de uma maneira segura (neste primeiro momento)
import requests # para acessar à API
from datetime import datetime # para ajudar no registro de diagnóstico
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

# Variável para simular psicológos próximos à sua área que atendem presencialmente, o objetivo futuro seja que sejam psicológos cadastrados
psicologosPresencial = {
    "Tatiana Rocha",
    "Maria Fogueta",
    "Lahgolas",
    "Tabs"
}

# Variável para simular psicológos próximos à sua área (ou não) que atendem on-line, o objetivo futuro seja que sejam psicológos cadastrados
psicologosOnline = {
    "Tatiana Rocha",
    "Leticia Resina",
    "Catherine Pinkerton",
    "Ana Carolina"
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

def carregarDoencas():
    with open("doencas.json", "r", encoding='utf-8') as file:
        doencas = json.load(file)
    return doencas

def calcularSimilaridade(sintomasUsuario, sintomasDoenca):
    """
        Função criada para transformar tanto o sintomas informados pelo usuário quanto os sintomas presentes
        no arquivo de doencas.json em conjuntos, e fazer essa interseção entre esses conjuntos e comparar qual
        doença tem mais similariedade com os sintomas colocados. Futuramente, mais doenças serão inseridas!
    """
    intersecao = len(set(sintomasUsuario) & set(sintomasDoenca))
    uniao = len(set(sintomasUsuario) | set(sintomasDoenca))
    similaridade = intersecao / uniao if uniao > 0 else 0
    return similaridade

def diagnosticar(doencas, sintomasUsuario, limiar_minimo=3):
    """
        É uma função criada para fazer esse diagnóstico em base da similariedade e o que for mais similar
        entre eles.
    """
    if len(sintomasUsuario) < limiar_minimo:
        return "Insira pelo menos 3 sintomas para um diagnóstico mais preciso."

    melhorDiagnostico = None
    melhorSimilaridade = 0

    for doenca, sintomasDoenca in doencas.items():
        similaridade = calcularSimilaridade(sintomasUsuario, sintomasDoenca)

        if similaridade > melhorSimilaridade:
            melhorDiagnostico = doenca
            melhorSimilaridade = similaridade

    return melhorDiagnostico

def salvarRegistro(cep, diagnostico):
    """
        Salvar a doença nos registros.json para caso mais doenças sejam inseridas, seria alarmante a situação
        pros médicos e começar a pensar em soluções em base das datas.
    """
    try:
        with open("registros.json", "r", encoding='utf-8') as file:
            registros = json.load(file)
    except FileNotFoundError:
        registros = {}

    data = datetime.now().strftime("%Y-%m-%d")

    if cep not in registros:
        registros[cep] = []

    registros[cep].append({"data": data, "diagnostico": diagnostico})

    with open("registros.json", "w", encoding='utf-8') as file:
        json.dump(registros, file, indent=2)

def preDiagnostico():
    """
        Função responsável por dar o pré-diagnóstico para os usuários com base de seus sintomas
    """
    doencas = carregarDoencas()

    print("Informe os sintomas que você está sentindo, separados por vírgula:")
    sintomasUsuario = input().split(", ")

    diagnostico = diagnosticar(doencas, sintomasUsuario)

    if diagnostico:
        if diagnostico.startswith("Insira pelo menos"):
            print(diagnostico)
        else:
            print(f"Com base nos sintomas informados, você pode estar com {diagnostico}.")
            time.sleep(1)
            print("ATENÇÃO: NÃO SE AUTOMEDIQUE!")
            time.sleep(1)
            print("É aconselhável consultar um médico para um diagnóstico mais preciso.")
            time.sleep(1)

            print("Para nos auxiliar, caso seja um surto em sua cidade e possamos analisar de forma rápida, vamos adicionar em registros juntamente com a data.")
            print("Fique tranquilo(a), será registrado de forma anônima, respeitando sua privacidade!. Tudo bem?")
            time.sleep(1)
            
            try:
                cep: str = input("Informe o CEP (SOMENTE NÚMEROS!): ")
                url = f'https://viacep.com.br/ws/{cep}/json/'

                resposta = requests.get(url)

                if resposta.status_code == 200: # ou requests.codes.ok
                    dicionario = resposta.json()
                    print(f"Rua: {dicionario['logradouro']}")
                    print(f"Cidade: {dicionario['localidade']}")
                    print(f"Estado: {dicionario['uf']}")
                    time.sleep(1)

                    # Salvar o registro anonimamente
                    salvarRegistro(cep, diagnostico)
                    time.sleep(1)

                elif resposta.status_code == 400: # Bad Request
                    print("ERRO: O CEP deve ter 8 caracteres")
                    time.sleep(1)

            except requests.exceptions.RequestException as e:
                print(f"ERRO: {e}")
                print("Não foi possível acessar à API!")
                time.sleep(1)

            except Exception as mensagem:
                print(f"ERRO: {mensagem}")
                time.sleep(1)
    else:
        print("Não foi possível determinar um diagnóstico com base nos sintomas informados.")
        time.sleep(1)

def encontrarPsicologo():
    """
        Função criada para simular a busca de psicológos na área informada pelo usuário através de seu CEP.
    """
    try:
        cep = input("Informe o CEP (SOMENTE NÚMEROS!): ")
        url = f'https://viacep.com.br/ws/{cep}/json/'

        resposta = requests.get(url)

        if resposta.status_code == 200: # ou requests.codes.ok
            dicionario = resposta.json()
            print(f" Psicológos próximos ao CEP:{dicionario['cep']}")
            print("Psicológos presencial")
            for psicologo in psicologosPresencial:
                print(psicologo)
            print("-----------------------------------------------------")
            print("Psicológos on-line")
            for psicologo in psicologosOnline:
                print(psicologo)        

        elif resposta.status_code == 400: # Bad Request
            print("ERRO: O CEP deve ter 8 caracteres")

    except ConnectionError:
        print("ERRO: Não foi possível acessar à API!")

    except Exception as mensagem:
        print(f"ERRO: {mensagem}")

def carregarLembretes():
    """
        Função para carregar os lembretes de remédios do arquivo JSON.
    """
    try:
        with open('lembretes.json', 'r', encoding='utf-8') as arquivo:
            lembretes = json.load(arquivo)
    except FileNotFoundError:
        lembretes = {}
    return lembretes

def salvarLembretes(lembretes):
    """
        Função para salvar os lembretes de remédios no arquivo JSON
    """
    with open('lembretes.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lembretes, arquivo, indent=4, ensure_ascii=False)

def adicionarLembrete(lembretes, email, remedio, titulo, horario):
    """
        Função para adicionar um lembrete de remédio
    """
    if email not in lembretes:
        lembretes[email] = {}  

    # Obter a próxima chave única inteira
    chave = 1
    if lembretes[email]:
        chavesInt = [int(chave) for chave in lembretes[email].keys()]
        chave = str(max(chavesInt) + 1)

    # Cria o lembrete de remédio
    lembrete = {
        "remedio": remedio,
        "titulo": titulo,
        "horario": horario
    }

    lembretes[email][chave] = lembrete  

    salvarLembretes(lembretes)

    print("Lembrete salvo com sucesso!")
    time.sleep(1)

def visualizarLembretes(lembretes, email):
    """
        Função para visualizar lembretes de remédios de um usuário
    """
    if email in lembretes and lembretes[email]:
        print(f"\nLembretes de remédios:")
        for chave, lembrete in lembretes[email].items():
            print(f"{lembrete['titulo']} - Remédio: {lembrete['remedio']} - Horário: {lembrete['horario']}")
            time.sleep(1)
    else:
        print(f"Nenhum lembrete de remédio encontrado! Que tal cadastrar alguns?")
        time.sleep(1)

def editarLembretes(lembretes, email):
    """
        Função criada para editar lembretes já pré-cadastrados em nosso sistema.
    """
    if email not in lembretes:
        print("Você não possui lembretes cadastrados! Que tal cadastrar alguns?")
        time.sleep(1)
    else:
        tituloEditar = input("Informe o título que deseja editar: ")
        lembreteEncontrado = False
        time.sleep(1)

        for chave, lembrete in lembretes[email].items():
            if lembrete['titulo'] == tituloEditar:
                lembreteEncontrado = True
                print("O que você deseja editar para editar?")
                print("\n 1 - Titulo \n 2 - Remédio \n 3 - Horário \n")
                try:
                    opcaoEditar = int(input("Digite a opção aqui: "))

                    if (opcaoEditar < 1) or (opcaoEditar > 3):
                        raise TypeError
                    
                    elif opcaoEditar == 1:
                        novoTitulo = input("Digite o novo título do remédio: ")
                        lembrete['titulo'] = novoTitulo
                        time.sleep(1)

                    elif opcaoEditar == 2:
                        novoRemedio = input("Informe o novo remédio: ")
                        lembrete['remedio'] = novoRemedio
                        time.sleep(1)

                    elif opcaoEditar == 3:
                        novoHorario = input("Informe o novo horário: ")
                        lembrete['horario'] = novoHorario
                        time.sleep(1)
                    
                    salvarLembretes(lembretes)
                    print("Lembrete alterado com sucesso!")
                    time.sleep(1)

                except ValueError: # caso valor diferente de inteiro
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    time.sleep(1)
                    
                except TypeError: # caso opção não existente no sistema
                    print("Por favor, digite uma opção válida para prosseguir.")
                    time.sleep(1)

        if not lembreteEncontrado:
            print(f"O título {tituloEditar} não foi encontrado! Tente novamente")
            time.sleep(1)

def excluirLembrete(lembretes, email):
    """
        Função criada para excluir lembretes pré-cadastrados em nosso sistema.
    """

    if emailUsuario not in lembretes: # Caso o usuário não possua nenhuma lembrete favorita
        print("Você não possui lembretes cadastrados! Que tal cadastrar alguns?")
        time.sleep(1)

    else: # Caso possua
        encontrouLembrete = False
        titulo = input("Qual título do lembrete que você deseja excluir? \n")
        chaveRemover = []
        for chave, item in lembretes[email].items():
            if item["titulo"] == titulo:
                encontrouLembrete = True # se encontra, passa a ser verdadeiro para prosseguir
                print(f"Você tem certeza que deseja remover {titulo} de seus lembretes?") 
                # Para o usuário ter certeza e não excluir nada sem desejar
                print("\n 1 - Sim \n 2 - Não \n")

                try: # tratamento de erros para evitar paradas indesejadas durante o programa
                    opcaoCerteza = int(input("Informe a opção desejada aqui: "))
                    if (opcaoCerteza < 1) or (opcaoCerteza > 2):
                        raise TypeError
                    
                    elif opcaoCerteza == 1:
                            chaveRemover.append(chave)

                    elif opcaoCerteza == 2:
                        print("Nenhum lembrete foi removida!")
                        time.sleep(1)

                except ValueError: # caso valor diferente de inteiro
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    time.sleep(1)
                    
                except TypeError: # caso opção não existente no sistema
                    print("Por favor, digite uma opção válida para prosseguir.")
                    time.sleep(1)

        for chave in chaveRemover:
            del lembretes[emailUsuario][chave]
            print("Lembrete removido com sucesso!")
            time.sleep(1)

        if not lembretes[emailUsuario]: 
            del lembretes[emailUsuario] # Deleta do arquivo JSON

        if not encontrouLembrete: # caso o lembrete chamada não exista no sistema
            print(f"O lembrete não existe! Tente novamente, ou cadastre em nosso sistema para editar/excluir.")

    salvarLembretes(lembretes)

def gerenciarLembretes(email):
    """
        Função principal para gerenciar os lembretes de remédios
    """
    lembretes = carregarLembretes()

    while True:
        print("\n 1 - Adicionar lembrete de remédio \n 2 - Visualizar lembretes de remédios \n 3 - Editar lembrete \n 4 - Excluir lembrete \n 5 - Voltar ao menu principal \n")
        opcaoLembrete = input("Escolha uma opção: ")
        if opcaoLembrete == '1':
            remedio = input("Digite o remédio: ")
            titulo = input("Digite o título do lembrete: ")
            horario = input("Digite o horário do lembrete (ex: 08:00): ")
            adicionarLembrete(lembretes, email, remedio, titulo, horario)
        elif opcaoLembrete == '2':
            visualizarLembretes(lembretes, email)
        elif opcaoLembrete == '3':
            editarLembretes(lembretes, email)
        elif opcaoLembrete == '4':
            excluirLembrete(lembretes, email)
        elif opcaoLembrete == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

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
                gerenciarLembretes(emailUsuario)
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
                preDiagnostico()
            elif opcao == 8:
                # Psicológos na sua área
                encontrarPsicologo()
                time.sleep(1)
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
                gerenciarLembretes(emailUsuario)
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
                preDiagnostico()
            elif opcao == 8:
                # Psicológos na sua área
                encontrarPsicologo()
                time.sleep(1)
            elif opcao == 9:
                # Encerrando a Julia
                print("Obrigada por utilizar a Julia!")
                print("Deslogando...")
                time.sleep(1)
                break