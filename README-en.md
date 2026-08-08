# Telegram Channel Downloader Script

*Read this in other languages: [Português](README.md)*

---

*This Python script automates the download and organization of content stored in Telegram channels. It reads the message history, converts structural texts into folders on the hard drive, and downloads all files, such as videos and PDFs, directly into the correct modules, restoring the original structure.*

## ⚠️ IMPORTANT NOTICE FOR BEGINNERS

* To use this tool, it is mandatory that you have the *Python* language installed on your computer. If you don't have it yet, look for the official Python website to download and install it before proceeding with the steps below.

## 📂 TELEGRAM CHANNEL EXTRACTOR AND ORGANIZER

* This Python *script* automates the entire process of *downloading* and organizing files made available in Telegram channels. When executed, it scans the message history of the desired channel.
* Every time it identifies a structural text (such as a module title), it creates a corresponding folder on your hard drive. It then downloads all attached files, including videos, PDFs, spreadsheets, and compressed files, saving them directly into their respective folders. This ensures the original structure of the content is restored in a simple and automated way.

## 🚀 TUTORIAL ON HOW TO RUN THE *SCRIPT*

### Step 01 - Obtain Telegram Credentials

* Go to `my.telegram.org` in your browser and *log in* using your phone number.
* Click on the *API development tools* option.
* Fill in the `App title` and `Short name` fields with any name you like, for example, ExtratorDeCanais. For *Platform*, leave it as *Desktop*.
* Click the *Create application* button.
* On the next page, copy the values shown in `App api_id`, which is a sequence of numbers, and `App api_hash`, which is a sequence mixing letters and numbers. Save this information.

### Step 02 - Prepare the Environment

* Open your computer's *terminal* or command *prompt*.
* Install the library required for the *script* to work by typing the following command and pressing *Enter*:
  `pip install telethon`

### Step 03 - Configure the *Script*

* Open the `extrator_telegram.py` file in any text editor.
* Right at the beginning of the file, you'll see a settings section.
* Replace the `API_ID` and `API_HASH` fields with the values you obtained in step 1.
* In the `CANAL_ALVO` field, enter the link or identifier of the Telegram channel that contains the files (e.g., 't.me/channel_name').
* In the `PASTA_BASE` field, enter the full path of the folder on your computer or external hard drive where the channel files should be saved (e.g., 'C:\Users\JohnDoe\Documents\DownloadTelegram').
* Save the file with your changes.

### Step 04 - Run the Download

* Go back to your *terminal* or command *prompt*.
* Navigate to the folder where your *script* is saved and type the following command to start the program:
  `python extrator_telegram.py`
* Since this will be the first time you run the program, it will ask you to confirm your identity. Enter your phone number with the country code (for example, enter +5511981456734 if your phone number is (11) 98145-6734) and press *Enter*.
* Telegram will send a numeric verification code directly to the app on your phone.
* Enter that code in the *terminal*.
* Done. From this point on, the *script* will start working on its own, creating the folders and downloading all the channel's materials to your computer.

### ⚙️ FEATURES RELATED TO SCRIPT EXECUTION

* Safe Shutdown: Once the file download has started, the process can be safely and immediately interrupted at any time by pressing Ctrl + C in the terminal.
* Smart Conflict Resolution: If the script detects that a file with the same name already exists in your folder, it will pause the download and display the size of both files (the local one and the one on Telegram). You can then choose between three actions: download a new numbered copy (e.g., "File (2).mp4"), skip this download and move on to the next one, or replace the old local file with the new one.

### 👤 AUTHORSHIP AND DEVELOPMENT

Automation script developed in Python independently by [**Pablo Phillipe Cândido dos Santos**](http://lattes.cnpq.br/9500873674712528), intended for downloading and organizing files made available in Telegram channels, with automated restoration of the materials' original structure.

The development made use of generative artificial intelligence tools as an auxiliary resource in the development process, with the conception, implementation, integration, and verification of the project remaining the author's responsibility.
