import os
import re
from telethon.sync import TelegramClient
from telethon.errors import FileReferenceExpiredError # Importação nova para tratar o erro // New import to handle the error

# ==========================================
# CONFIGURAÇÕES - PREENCHA COM SEUS DADOS // SETTINGS - FILL IN YOUR DETAILS
# ==========================================
API_ID = 'SEU_API_ID_AQUI' 
API_HASH = 'SEU_API_HASH_AQUI'
CANAL_ALVO = 'link_do_canal_ou_ID' # Ex: 't.me/nome_do_canal' // Ex: 't.me/channel_name'
PASTA_BASE = r'D:\Cursos\NomeDoCurso' # Caminho do seu HD externo ou interno // Path to your external or internal hard drive

# Nome da sessão (cria um arquivo .session na pasta para não pedir login toda vez) // Session name (creates a .session file in the folder so it doesn't ask for login every time)
SESSAO = 'minha_sessao_telegram'

def limpar_nome_pasta(nome):
    """Remove caracteres inválidos para nomes de pastas no Windows/Linux. // Removes invalid characters for folder names in Windows/Linux."""
    # Remove quebras de linha e limita o tamanho // Removes line breaks and limits the size
    nome = nome.replace('\n', ' ').strip()
    nome = nome[:50] # Limita a 50 caracteres para evitar caminhos muito longos // Limits to 50 characters to avoid very long paths
    return re.sub(r'[\\/*?:"<>|]', "", nome)

async def main():
    # Cria a pasta base se não existir // Creates the base folder if it does not exist
    if not os.path.exists(PASTA_BASE):
        os.makedirs(PASTA_BASE)

    print(f"Conectando ao canal: {CANAL_ALVO} // Connecting to the channel: {CANAL_ALVO}")
    print("DICA: Pressione Ctrl + C no terminal a qualquer momento para encerrar o script. // TIP: Press Ctrl + C in the terminal at any time to terminate the script.\n")
    
    # Pasta padrão caso o canal comece com vídeos antes de qualquer texto // Default folder in case the channel starts with videos before any text
    pasta_atual = os.path.join(PASTA_BASE, "00_Sem_Modulo")
    
    # Flag para controlar a automação da opção 4 // Flag to control the automation of option 4
    pular_identicos_automaticamente = False
    
    # iter_messages com reverse=True lê da mais antiga para a mais nova // iter_messages with reverse=True reads from the oldest to the newest
    async for mensagem in client.iter_messages(CANAL_ALVO, reverse=True):
        
        # 1. Identifica se é uma mensagem apenas de texto (Nome do Módulo) // 1. Identifies if it is a text-only message (Module Name)
        if mensagem.text and not mensagem.media:
            nome_limpo = limpar_nome_pasta(mensagem.text)
            
            # Evita criar pastas vazias se a mensagem for só um espaço em branco // Avoids creating empty folders if the message is just a blank space
            if nome_limpo: 
                pasta_atual = os.path.join(PASTA_BASE, nome_limpo)
                if not os.path.exists(pasta_atual):
                    os.makedirs(pasta_atual)
                    print(f"\n[+] Nova pasta de módulo criada: {nome_limpo} // [+] New module folder created: {nome_limpo}")
        
        # 2. Identifica se a mensagem contém mídia // 2. Identifies if the message contains media
        elif mensagem.media and hasattr(mensagem, 'file') and mensagem.file:
            # Garante que a pasta atual existe // Ensures the current folder exists
            if not os.path.exists(pasta_atual):
                os.makedirs(pasta_atual)
                
            # Extrai o nome do arquivo (ou cria um genérico se não tiver nome) // Extracts the file name (or creates a generic one if it has no name)
            nome_arquivo = mensagem.file.name
            if not nome_arquivo:
                extensao = mensagem.file.ext or ".bin"
                nome_arquivo = f"arquivo_sem_nome_{mensagem.id}{extensao}"
                
            caminho_esperado = os.path.join(pasta_atual, nome_arquivo)
            caminho_final = caminho_esperado
            tamanho_remoto_bytes = mensagem.file.size or 0
            pular_arquivo = False
            
            # 3. Validação de arquivo já existente // 3. Validation for already existing file
            if os.path.exists(caminho_esperado):
                tamanho_local_bytes = os.path.getsize(caminho_esperado)
                
                # Conversão para MB // Conversion to MB
                tam_local_mb = tamanho_local_bytes / (1024 * 1024)
                tam_remoto_mb = tamanho_remoto_bytes / (1024 * 1024)
                
                # Se a opção 4 já foi ativada antes e os arquivos são idênticos, pula direto // If option 4 was already activated and the files are identical, skip directly
                if pular_identicos_automaticamente and tamanho_local_bytes == tamanho_remoto_bytes:
                    print(f"    [!] Arquivo idêntico encontrado e ignorado automaticamente: {nome_arquivo} // Identical file found and automatically skipped: {nome_arquivo}")
                    continue
                
                print(f"\n[!] Conflito encontrado: O arquivo '{nome_arquivo}' já existe na pasta. // Conflict found: The file '{nome_arquivo}' already exists in the folder.")
                print(f"    - Tamanho na pasta // Size in folder: {tam_local_mb:.2f} MB")
                print(f"    - Tamanho no Telegram // Size in Telegram: {tam_remoto_mb:.2f} MB")
                
                while True:
                    print("\n    Escolha uma ação: // Choose an action:")
                    print("    1 - Baixar arquivo do Telegram inserindo um número na frente (Ex: Arquivo (2).ext) // Download Telegram file adding a number to the name (Ex: File (2).ext)")
                    print("    2 - Ignorar arquivo do Telegram e pular para o próximo // Ignore Telegram file and skip to the next")
                    print("    3 - Substituir arquivo da pasta pelo do Telegram // Replace folder file with the Telegram one")
                    
                    # Exibe a opção 4 apenas se os tamanhos forem exatamente iguais // Displays option 4 only if the sizes are exactly the same
                    if tamanho_local_bytes == tamanho_remoto_bytes:
                        print("    4 - Ignorar o arquivo do Telegram cujo download estava sendo preparado e iniciar o preparo do arquivo seguinte da lista; durante a atual sessão de downloads, repita esse processo para todos os arquivos da lista que apresentem o mesmo nome e mesmo tamanho. // Ignore the Telegram file whose download was being prepared and start preparing the next file on the list; during the current download session, repeat this process for all files on the list that have the same name and size.")
                    
                    escolha = input("    Digite a opção desejada // Enter the desired option: ").strip()
                    
                    if escolha == '1':
                        base, ext = os.path.splitext(nome_arquivo)
                        contador = 2
                        novo_nome = f"{base} ({contador}){ext}"
                        caminho_final = os.path.join(pasta_atual, novo_nome)
                        
                        # Garante que o número gerado também não exista // Ensures the generated number also does not exist
                        while os.path.exists(caminho_final):
                            contador += 1
                            novo_nome = f"{base} ({contador}){ext}"
                            caminho_final = os.path.join(pasta_atual, novo_nome)
                            
                        print(f"    -> Opção 1: O arquivo será baixado como '{novo_nome}' // Option 1: The file will be downloaded as '{novo_nome}'\n")
                        break
                        
                    elif escolha == '2':
                        pular_arquivo = True
                        print("    -> Opção 2: Download ignorado. // Option 2: Download ignored.\n")
                        break
                        
                    elif escolha == '3':
                        os.remove(caminho_esperado)
                        print("    -> Opção 3: O arquivo antigo foi removido. Iniciando substituição... // Option 3: The old file was removed. Starting replacement...\n")
                        break
                    
                    elif escolha == '4' and tamanho_local_bytes == tamanho_remoto_bytes:
                        pular_identicos_automaticamente = True
                        pular_arquivo = True
                        print("    -> Opção 4: Download ignorado. A regra automática foi ativada para os próximos arquivos idênticos. // Option 4: Download ignored. The automatic rule was activated for the next identical files.\n")
                        break
                        
                    else:
                        print("    [X] Opção inválida. Por favor, digite uma opção válida. // Invalid option. Please enter a valid option.")
            
            # Se o usuário escolheu pular o arquivo, o loop segue para a próxima mensagem // If the user chose to skip the file, the loop moves to the next message
            if pular_arquivo:
                continue

            print(f"    Baixando arquivo na pasta '{os.path.basename(pasta_atual)}'... // Downloading file to folder '{os.path.basename(pasta_atual)}'...")
            
            # O callback exibe o progresso do download no terminal // The callback displays the download progress in the terminal
            def progresso(recebido, total):
                print(f"    Progresso // Progress: {recebido * 100 / total:.1f}%", end='\r')
            
            # Bloco de tentativa com tratamento para referência expirada // Try block with handling for expired reference
            try:
                # O parâmetro 'file' agora recebe o 'caminho_final', respeitando a decisão do usuário // The 'file' parameter now receives 'caminho_final', respecting the user's decision
                caminho_baixado = await client.download_media(
                    mensagem, 
                    file=caminho_final, 
                    progress_callback=progresso
                )
                if caminho_baixado:
                    print(f"\n    Concluído: {os.path.basename(caminho_baixado)} // Completed: {os.path.basename(caminho_baixado)}")
                    
            except FileReferenceExpiredError:
                print("\n    [!] Referência expirada. Solicitando novo acesso ao Telegram e retomando... // Expired reference. Requesting new access to Telegram and resuming...")
                # Pede os dados da mensagem novamente para renovar o "ticket" // Requests the message data again to renew the "ticket"
                mensagem_atualizada = await client.get_messages(CANAL_ALVO, ids=mensagem.id)
                
                # Tenta fazer o download mais uma vez com a referência nova // Tries to download once more with the new reference
                caminho_baixado = await client.download_media(
                    mensagem_atualizada, 
                    file=caminho_final, 
                    progress_callback=progresso
                )
                if caminho_baixado:
                    print(f"\n    Concluído após renovação: {os.path.basename(caminho_baixado)} // Completed after renewal: {os.path.basename(caminho_baixado)}")

# Inicia o cliente com tratamento para encerramento manual // Starts the client with handling for manual termination
try:
    with TelegramClient(SESSAO, API_ID, API_HASH) as client:
        # O loop do Telethon executa a função assíncrona // The Telethon loop executes the asynchronous function
        client.loop.run_until_complete(main())
except KeyboardInterrupt:
    print("\n\n[!] Processo cancelado pelo usuário. Encerrando o extrator de forma segura... // Process canceled by the user. Terminating the extractor safely...")
except Exception as e:
    print(f"\n\n[X] Ocorreu um erro inesperado: {e} // An unexpected error occurred: {e}")
