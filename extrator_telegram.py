import os
import re
from telethon.sync import TelegramClient
from telethon.tl.types import DocumentAttributeVideo

# ==========================================
# CONFIGURAÇÕES - PREENCHA COM SEUS DADOS // SETTINGS - FILL IN YOUR DETAILS
# ==========================================
API_ID = 'SEU_API_ID_AQUI' 
API_HASH = 'SEU_API_HASH_AQUI'
CANAL_ALVO = 'link_do_canal_ou_ID' # Ex: 't.me/nome_do_canal'
PASTA_BASE = r'D:\Cursos\NomeDoCurso' # Caminho do seu HD externo // Path to your external hard drive

# Nome da sessão (cria um arquivo .session na pasta para não pedir login toda vez)
# Session name (creates a .session file in the folder so it doesn't ask for a login every time)
SESSAO = 'minha_sessao_telegram'

def limpar_nome_pasta(nome):
    """Remove caracteres inválidos para nomes de pastas no Windows/Linux.""" # Remove characters that are invalid for folder names in Windows/Linux.
    # Remove quebras de linha e limita o tamanho // # Removes line breaks and limits the size
    nome = nome.replace('\n', ' ').strip()
    nome = nome[:50] # Limita a 50 caracteres para evitar caminhos muito longos // # Limits to 50 characters to avoid excessively long paths
    return re.sub(r'[\\/*?:"<>|]', "", nome)

async def main():
    # Cria a pasta base se não existir // # Creates the base folder if it doesn't exist
    if not os.path.exists(PASTA_BASE):
        os.makedirs(PASTA_BASE)

    print(f"Conectando ao canal: {CANAL_ALVO}")
    
    # Pasta padrão caso o canal comece com vídeos antes de qualquer texto // # Default folder in case the channel starts with videos before any text
    pasta_atual = os.path.join(PASTA_BASE, "00_Sem_Modulo")
    
    # iter_messages com reverse=True lê da mais antiga para a mais nova // # iter_messages with reverse=True reads from oldest to newest
    async for mensagem in client.iter_messages(CANAL_ALVO, reverse=True):
        
        # 1. Identifica se é uma mensagem apenas de texto (Nome do Módulo) // # 1. Identifies whether it is a text-only message (Module Name)
        if mensagem.text and not mensagem.media:
            nome_limpo = limpar_nome_pasta(mensagem.text)
            
            # Evita criar pastas vazias se a mensagem for só um espaço em branco // # Avoid creating empty folders if the message is just a blank space
            if nome_limpo: 
                pasta_atual = os.path.join(PASTA_BASE, nome_limpo)
                if not os.path.exists(pasta_atual):
                    os.makedirs(pasta_atual)
                    print(f"\n[+] Nova pasta de módulo criada: {nome_limpo}")
        
        # 2. Identifica se a mensagem contém mídia (Vídeo ou Documento) // # 2. Identifies whether the message contains media (video or document)
        elif mensagem.media:
            # Garante que a pasta atual existe // # Ensures the current directory exists
            if not os.path.exists(pasta_atual):
                os.makedirs(pasta_atual)
            
            # Verifica se é um arquivo de vídeo // # Checks if it is a video file
            is_video = False
            if hasattr(mensagem.media, 'document'):
                for atributo in getattr(mensagem.media.document, 'attributes', []):
                    if isinstance(atributo, DocumentAttributeVideo):
                        is_video = True
                        break

            # Se quiser baixar PDFs e outros arquivos junto, remova o "if is_video:" e deixe apenas o download.
            # If you want to download PDFs and other files as well, remove "if is_video:" and keep only the download.
            if is_video:
                print(f"    Baixando vídeo na pasta '{os.path.basename(pasta_atual)}'...")
                
                # O callback exibe o progresso do download no terminal // # The callback displays the download progress in the terminal
                def progresso(recebido, total):
                    print(f"    Progresso: {recebido * 100 / total:.1f}%", end='\r')
                
                # Realiza o download // # Downloads the file
                caminho_arquivo = await client.download_media(
                    mensagem, 
                    file=pasta_atual, 
                    progress_callback=progresso
                )
                print(f"\n    Concluído: {os.path.basename(caminho_arquivo)}")

# Inicia o cliente // # Starts the client
with TelegramClient(SESSAO, API_ID, API_HASH) as client:
    # O loop do Telethon executa a função assíncrona // # The Telethon loop executes the asynchronous function
    client.loop.run_until_complete(main())
