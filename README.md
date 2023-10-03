# Voice-controlled-personal-assistant.
AI aid for tasks via voice cmd.

### Project Description: Voice-Controlled Personal Assistant

**Objective**: 
The objective of the project is to create a personal desktop assistant that responds to voice commands to perform a variety of tasks, such as sending emails, telling the time, opening files, playing media, and providing reminders, thereby automating and simplifying various day-to-day tasks for the user.

**Key Libraries and Functions**:

### 1. **speech_recognition**
   - **Recognizer()**: Initiates a recognizer instance which will recognize the speech.
   - **Microphone()**: Captures voice input through the system’s microphone.
   - **recognize_google(audio)**: Converts the audio captured by the microphone into text using Google's speech recognition API.

### 2. **pyttsx3**
   - **init()**: Initializes the text-to-speech engine.
   - **say(text)**: Converts the text to speech.
   - **runAndWait()**: Blocks while processing all the currently queued commands.

### 3. **yagmail**
   - **SMTP(username, password)**: Establishes a connection to the email server.
   - **send(to, subject, contents)**: Sends an email with the specified subject and contents to the recipient.

### 4. **pygame**
   - **mixer.init()**: Initializes the mixer module for playing sound.
   - **mixer.music.load(file_path)**: Loads a music file for playback.
   - **mixer.music.play()**: Plays the loaded music file.

### 5. **apscheduler**
   - **BackgroundScheduler()**: Initializes a scheduler to run jobs in the background.
   - **add_job(func, trigger, args)**: Adds a job to the scheduler and sets the trigger and arguments.

### 6. **datetime**
   - **datetime.now()**: Returns the current date and time.
   - **strftime(format)**: Formats datetime objects as strings.

### 7. **os**
   - **startfile(path)**: Opens the file with its associated application.

### Core Functionalities:

- **Voice Commands**: Interprets and processes user voice commands.
- **Sending Emails**: Sends emails with specified subject and body to the designated recipient.
- **Time Telling**: Vocalizes the current time upon request.
- **Water Reminder**: Provides a voice reminder to drink water every hour.
- **File Opening**: Opens a specified file with its default application.
- **Media Playback**: Plays specified audio and video files.
- **Customizable**: Can be further customized and expanded for additional functionalities based on user needs.

### Motive:

The motive behind this project is to facilitate user interaction with their computer, enabling them to perform an array of tasks hands-free, merely using voice commands. This could especially be useful for individuals with specific accessibility needs, enhancing their computing experience by providing a vocal interface to execute commands and perform tasks in a smooth and user-friendly manner. It stands as a testament to the potential of integrating voice technology and artificial intelligence in user-system interaction, paving the way for future innovations in assistive technology.
