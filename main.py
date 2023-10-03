import speech_recognition as sr
import pyttsx3
import yagmail
import datetime
import os
import pygame
from apscheduler.schedulers.background import BackgroundScheduler

class PersonalAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.remind_to_drink_water, 'interval', hours=1)
        self.scheduler.start()
        self.greet()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greet(self):
        current_hour = datetime.datetime.now().hour
        if 0 <= current_hour < 12:
            self.speak("Good Morning!")
        elif 12 <= current_hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("How can I assist you today?")

    def listen(self):
        with sr.Microphone() as source:
            self.speak("I'm listening...")
            audio = self.recognizer.listen(source, timeout=10)
            return audio

    def recognize_speech(self, audio):
        try:
            command = self.recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            self.speak("There was an error with the request.")
        return ""

    def send_email(self, to, subject, body):
        yag = yagmail.SMTP('YourEmail@gmail.com', 'YourEmailPassword')
        yag.send(to=to, subject=subject, contents=body)
        self.speak(f"Email sent to {to}")

    def tell_time(self):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")

    def remind_to_drink_water(self):
        self.speak("Reminder to drink water!")

    def open_file(self, file_path):
        try:
            os.startfile(file_path)
            self.speak(f"Opening file: {file_path}")
        except FileNotFoundError:
            self.speak("File not found.")
        except Exception as e:
            self.speak(str(e))

    def play_media(self, file_path):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.speak(f"Playing: {file_path}")
        except FileNotFoundError:
            self.speak("File not found.")
        except Exception as e:
            self.speak(str(e))

    def run(self):
        while True:
            audio = self.listen()
            command = self.recognize_speech(audio)

            if "send an email" in command:
                self.speak("To whom should I send the email?")
                to = self.recognize_speech(self.listen())
                self.speak("What should be the subject?")
                subject = self.recognize_speech(self.listen())
                self.speak("What should I write in the body?")
                body = self.recognize_speech(self.listen())
                self.send_email(to, subject, body)
            elif "what time is it" in command:
                self.tell_time()
            elif "open file" in command:
                self.speak("Please specify the file path to open.")
                file_path = self.recognize_speech(self.listen())
                self.open_file(file_path)
            elif "play music" in command:
                self.speak("Please specify the music file path to play.")
                file_path = self.recognize_speech(self.listen())
                self.play_media(file_path)
            elif "stop" in command:
                pygame.mixer.music.stop()  # Stop music if playing
                self.speak("Goodbye!")
                break

if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.run()
