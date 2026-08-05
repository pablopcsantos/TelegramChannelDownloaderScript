*Read this in other languages: [English](README-en.md)*

---

*This Python script automates the download and organization of courses stored in Telegram channels. It reads the message history, converts structural texts into folders on the HD, and downloads all files, like videos and PDFs, directly to the correct modules, restoring the original structure.*

## IMPORTANT WARNING FOR BEGINNERS

* To use this tool, it is mandatory that you have the *Python* language installed on your computer. If you do not have it yet, search the official Python website to perform the download and installation before proceeding with the steps below.

## TELEGRAM COURSE EXTRACTOR AND ORGANIZER

* This Python *script* automates the entire process of *downloading* and organizing course files made available in Telegram channels. When executed, it scans the message history of the desired channel.
* Every time it identifies a structural text (such as a module title), it creates a corresponding folder on your hard drive. Then, it downloads all attached files, including videos, PDFs, spreadsheets, and compressed files, saving them directly into their respective folders. This ensures the restoration of the original course structure in a simple and automated way.

## TUTORIAL ON HOW TO RUN THE *SCRIPT*

### STEP 1: GET TELEGRAM CREDENTIALS

* Access the website `my.telegram.org` through your browser and *log in* using your mobile number.
* Click on the *API development tools* option.
* Fill in the `App title` and `Short name` fields with the name you desire, for example, ExtratorDeCursos. Under *Platform*, leave it as *Desktop*.
* Click the *Create application* button.
* On the next page, copy the values presented in `App api_id`, which is a sequence of numbers, and `App api_hash`, which is a sequence mixing letters and numbers. Save this data.

### STEP 2: PREPARE THE ENVIRONMENT

* Open your computer's *terminal* or command *prompt*.
* Install the necessary library for the *script* to work by typing the following command and pressing *Enter*:
  `pip install telethon`

### STEP 3: CONFIGURE THE *SCRIPT*

* Open the file `extrator_telegram.py` in any text editor.
* Right at the beginning of the file, you will see a settings section.
* Replace the `API_ID` and `API_HASH` fields with the values you obtained in step 1.
* In the `CANAL_ALVO` field, insert the link or the ID of the Telegram channel that contains the course (Ex: 't.me/channel_name').
* In the `PASTA_BASE` field, insert the full path of the folder on your computer or external HD where the course should be saved (Ex: 'C:\Users\Johndoe\Documents\Courses').
* Save the file with your changes.

### STEP 4: EXECUTE THE DOWNLOAD

* Return to your *terminal* or command *prompt*.
* Navigate to the folder where your *script* is saved and type the following command to start the program:
  `python extrator_telegram.py`
* As it will be the first time you run the program, it will ask you to confirm your identity. Enter your mobile number with the country code (for example, type the number +5511981456734 if your cell phone is (11) 98145-6734) and press *Enter*.
* Telegram will send a numeric verification code directly to the app on your cell phone.
* Type this code in the *terminal*.
* Done. From this moment on, the *script* will start working alone, creating the folders and downloading all the channel's materials to your computer.
