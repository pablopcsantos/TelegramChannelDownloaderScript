*Read this in other languages: [English](README-en.md)*

---

*Este script em Python automatiza o download e a organização de cursos armazenados em canais do Telegram. Ele lê o histórico de mensagens, converte textos estruturais em pastas no HD e baixa todos os arquivos, como vídeos e PDFs, diretamente para os módulos corretos, restaurando a estrutura original.*

## AVISO IMPORTANTE PARA INICIANTES

* Para utilizar esta ferramenta, é obrigatório que você possua a linguagem *Python* instalada no seu computador. Caso ainda não tenha, procure pelo site oficial do Python para realizar o download e a instalação antes de prosseguir com os passos abaixo.

## EXTRATOR E ORGANIZADOR DE CURSOS DO TELEGRAM

* Este *script* em Python automatiza todo o processo de *download* e organização de arquivos de cursos disponibilizados em canais do Telegram. Ao ser executado, ele varre o histórico de mensagens do canal desejado.
* Toda vez que identifica um texto estrutural (como o título de um módulo), ele cria uma pasta correspondente no seu disco rígido. Em seguida, ele baixa todos os arquivos anexados, incluindo vídeos, PDFs, planilhas e arquivos compactados, salvando-os diretamente nas respectivas pastas. Isso garante a restauração da estrutura original do curso de forma simples e automatizada.

## TUTORIAL DE COMO EXECUTAR O *SCRIPT*

### PASSO 1: OBTER CREDENCIAIS DO TELEGRAM

* Acesse o site `my.telegram.org` através do seu navegador e faça *login* utilizando o seu número de celular.
* Clique na opção *API development tools*.
* Preencha os campos `App title` e `Short name` com o nome que desejar, por exemplo, ExtratorDeCursos. Em *Platform*, deixe como *Desktop*.
* Clique no botão *Create application*.
* Na página seguinte, copie os valores apresentados em `App api_id`, que é uma sequência de números, e `App api_hash`, que é uma sequência misturando letras e números. Guarde esses dados.

### PASSO 2: PREPARAR O AMBIENTE

* Abra o *terminal* ou *prompt* de comando do seu computador.
* Instale a biblioteca necessária para o *script* funcionar digitando o seguinte comando e apertando *Enter*:
  `pip install telethon`

### PASSO 3: CONFIGURAR O *SCRIPT*

* Abra o arquivo `extrator_telegram.py` em qualquer editor de texto.
* Logo no início do arquivo, você verá uma seção de configurações.
* Substitua os campos de `API_ID` e `API_HASH` pelos valores que você obteve no passo 1.
* No campo `CANAL_ALVO`, insira o link ou a identificação do canal do Telegram que contém o curso (Ex: 't.me/nome_do_canal').
* No campo `PASTA_BASE`, insira o caminho completo da pasta no seu computador ou HD externo onde o curso deve ser salvo (Ex: 'C:\Users\Fulano\Documents\Cursos').
* Salve o arquivo com as suas alterações.

### PASSO 4: EXECUTAR O DOWNLOAD

* Volte ao seu *terminal* ou *prompt* de comando.
* Navegue até a pasta onde o seu *script* está salvo e digite o seguinte comando para iniciar o programa:
  `python extrator_telegram.py`
* Como será a primeira vez que você roda o programa, ele pedirá que você confirme sua identidade. Digite seu número de celular com o código do país (por exemplo, digite o número +5511981456734 caso o seu celular seja (11) 98145-6734) e aperte *Enter*.
* O Telegram enviará um código numérico de verificação diretamente para o aplicativo no seu celular.
* Digite esse código no *terminal*.
* Pronto. A partir desse momento, o *script* começará a trabalhar sozinho, criando as pastas e baixando todos os materiais do canal para o seu computador.
