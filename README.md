# Telegram Channel Downloader Script

*Read this in other languages: [English](README-en.md)*

---

*Este script em Python automatiza o download e a organização de conteúdos armazenados em canais do Telegram. Ele lê o histórico de mensagens, converte textos estruturais em pastas no HD e baixa todos os arquivos, como vídeos e PDFs, diretamente para os módulos corretos, restaurando a estrutura original.*

## ⚠️ AVISO IMPORTANTE PARA INICIANTES

* Para utilizar esta ferramenta, é obrigatório que você possua a linguagem *Python* instalada no seu computador. Caso ainda não tenha, procure pelo site oficial do Python para realizar o download e a instalação antes de prosseguir com os passos abaixo.

## 📂 EXTRATOR E ORGANIZADOR DE CANAIS DO TELEGRAM

* Este *script* em Python automatiza todo o processo de *download* e organização de arquivos disponibilizados em canais do Telegram. Ao ser executado, ele varre o histórico de mensagens do canal desejado.
* Toda vez que identifica um texto estrutural (como o título de um módulo), ele cria uma pasta correspondente no seu disco rígido. Em seguida, ele baixa todos os arquivos anexados, incluindo vídeos, PDFs, planilhas e arquivos compactados, salvando-os diretamente nas respectivas pastas. Isso garante a restauração da estrutura original dos conteúdos de forma simples e automatizada.

## 🚀 TUTORIAL DE COMO EXECUTAR O *SCRIPT*

### Passo 01 - Obter Credenciais Do Telegram

* Acesse o site `my.telegram.org` através do seu navegador e faça *login* utilizando o seu número de celular.
* Clique na opção *API development tools*.
* Preencha os campos `App title` e `Short name` com o nome que desejar, por exemplo, ExtratorDeCanais. Em *Platform*, deixe como *Desktop*.
* Clique no botão *Create application*.
* Na página seguinte, copie os valores apresentados em `App api_id`, que é uma sequência de números, e `App api_hash`, que é uma sequência misturando letras e números. Guarde esses dados.

### Passo 02 - Preparar o Ambiente

* Abra o *terminal* ou *prompt* de comando do seu computador.
* Instale a biblioteca necessária para o *script* funcionar digitando o seguinte comando e apertando *Enter*:
  `pip install telethon`

### Passo 03 - Configurar o *Script*

* Abra o arquivo `extrator_telegram.py` em qualquer editor de texto.
* Logo no início do arquivo, você verá uma seção de configurações.
* Substitua os campos de `API_ID` e `API_HASH` pelos valores que você obteve no passo 1.
* No campo `CANAL_ALVO`, insira o link ou a identificação do canal do Telegram que contém os arquivos (Ex: 't.me/nome_do_canal').
* No campo `PASTA_BASE`, insira o caminho completo da pasta no seu computador ou HD externo onde os arquivos dos canais devem ser salvos (Ex: 'C:\Users\Fulano\Documents\DownloadTelegram').
* Salve o arquivo com as suas alterações.

### Passo 04 - Executar o Download

* Volte ao seu *terminal* ou *prompt* de comando.
* Navegue até a pasta onde o seu *script* está salvo e digite o seguinte comando para iniciar o programa:
  `python extrator_telegram.py`
* Como será a primeira vez que você roda o programa, ele pedirá que você confirme sua identidade. Digite seu número de celular com o código do país (por exemplo, digite o número +5511981456734 caso o seu celular seja (11) 98145-6734) e aperte *Enter*.
* O Telegram enviará um código numérico de verificação diretamente para o aplicativo no seu celular.
* Digite esse código no *terminal*.
* Pronto. A partir desse momento, o *script* começará a trabalhar sozinho, criando as pastas e baixando todos os materiais do canal para o seu computador.

### ⚙️ FUNCIONALIDADES RELACIONADAS À EXECUÇÃO DO SCRIPT

* Encerramento Seguro: Após iniciado o download dos arquivos, o processo pode ser interrompido de forma segura e imediata a qualquer momento pressionando Ctrl + C no terminal.
* Resolução Inteligente de Conflitos: Se o script detectar que um arquivo com o mesmo nome já existe na sua pasta, ele pausará o download e exibirá o tamanho de ambos os arquivos (o local e o do Telegram). Você poderá então escolher entre três ações: baixar uma nova cópia numerada (ex: "Arquivo (2).mp4"), pular este download e seguir para o próximo, ou substituir o arquivo antigo local pelo novo.

### 👤 AUTORIA E DESENVOLVIMENTO

Script de automação desenvolvido na linguagem Python de forma independente por [**Pablo Phillipe Cândido dos Santos**](http://lattes.cnpq.br/9500873674712528), destinada ao download e à organização de arquivos disponibilizados em canais do Telegram, com restauração automatizada da estrutura de origem dos materiais.

O desenvolvimento contou com a utilização de ferramentas de inteligência artificial generativa como recurso auxiliar no processo de desenvolvimento, mantendo-se sob responsabilidade do autor a concepção, implementação, integração e verificação do projeto.
