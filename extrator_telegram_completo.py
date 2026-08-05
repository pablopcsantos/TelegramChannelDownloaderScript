import os
import re
from telethon.sync import TelegramClient
from telethon.tl.types import DocumentAttributeVideo

# ==========================================
# CONFIGURAÇÕES - PREENCHA COM SEUS DADOS
# ==========================================
API_ID = 'SEU_API_ID_AQUI' 
API_HASH = 'SEU_API_HASH_AQUI'
CANAL_ALVO = 'link_do_canal_ou_ID' # Ex: 't.me/nome_do_canal'
PASTA_BASE = r'D:\Cursos\NomeDoCurso' # Caminho do seu HD externo

# Nome da sessão (cria um arquivo .session na pasta para não pedir login toda vez)
SESSAO = 'minha_sessao_telegram'

def limpar_nome_pasta(nome):
    """Remove caracteres inválidos para nomes de pastas no Windows/Linux."""
    # Remove quebras de linha e limita o tamanho
    nome = nome.replace('\n', ' ').strip()
    nome = nome[:50] # Limita a 50 caracteres para evitar caminhos muito longos
    return re.sub(r'[\\/*?:"<>|]', "", nome)

async def main():
    # Cria a pasta base se não existir
    if not os.path.exists(PASTA_BASE):
        os.makedirs(PASTA_BASE)

    print(f"Conectando ao canal: {CANAL_ALVO}")
    
    # Pasta padrão caso o canal comece com vídeos antes de qualquer texto
    pasta_atual = os.path.join(PASTA_BASE, "00_Sem_Modulo")
    
    # iter_messages com reverse=True lê da mais antiga para a mais nova
    async for mensagem in client.iter_messages(CANAL_ALVO, reverse=True):
        
        # 1. Identifica se é uma mensagem apenas de texto (Nome do Módulo)
        if mensagem.text and not mensagem.media:
            nome_limpo = limpar_nome_pasta(mensagem.text)
            
            # Evita criar pastas vazias se a mensagem for só um espaço em branco
            if nome_limpo: 
                pasta_atual = os.path.join(PASTA_BASE, nome_limpo)
                if not os.path.exists(pasta_atual):
                    os.makedirs(pasta_atual)
                    print(f"\n[+] Nova pasta de módulo criada: {nome_limpo}")
        
        # 2. Identifica se a mensagem contém mídia (Vídeo ou Documento)
        elif mensagem.media:
            # Garante que a pasta atual existe
            if not os.path.exists(pasta_atual):
                os.makedirs(pasta_atual)
            
            # Verifica se é um arquivo de vídeo
            is_video = False
            if hasattr(mensagem.media, 'document'):
                for atributo in getattr(mensagem.media.document, 'attributes', []):
                    if isinstance(atributo, DocumentAttributeVideo):
                        is_video = True
                        break

            # Se quiser baixar PDFs e outros arquivos junto, remova o "if is_video:" 
            # e deixe apenas o download.
            if is_video:
                print(f"    Baixando vídeo na pasta '{os.path.basename(pasta_atual)}'...")
                
                # O callback exibe o progresso do download no terminal
                def progresso(recebido, total):
                    print(f"    Progresso: {recebido * 100 / total:.1f}%", end='\r')
                
                # Realiza o download
                caminho_arquivo = await client.download_media(
                    mensagem, 
                    file=pasta_atual, 
                    progress_callback=progresso
                )
                print(f"\n    Concluído: {os.path.basename(caminho_arquivo)}")

# Inicia o cliente
with TelegramClient(SESSAO, API_ID, API_HASH) as client:
    # O loop do Telethon executa a função assíncrona
    client.loop.run_until_complete(main())
