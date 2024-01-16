"""                                  Hey this is Girth GPT, Im built using alil knowlege of python and this code
                                      replying back. I 
                                      Im ovibously no professional so any pointers would be helpful.
                                      
                                      
                                      
                                      
                                      
"""




import os

#!pip install gtts
from gtts import gTTS

#!pip install webbrowser
import webbrowser

#!pip install webchatgpt
from WebChatGPT import ChatGPT  

#!pip install speechrecognition
import speech_recognition as sr

import subprocess

"""
--------Need mpg123 downlaoded to process audio files--------------

$ Sudo apt install mpg113




"""

import requests







log = []


def logger(command):
    with open('log_file', 'a') as log_file:
        print('Girth logging')
        
        
        log_file.write('\n'.join(map(str, log)) + '\n')
        print('Girthy Log Dumped')







def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
            print("Smelling For Girth")
            recognizer.adjust_for_ambient_noise(source)
            
            audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("the Girth Mule said:\n", command)
        return command.lower()
    except sr.UnknownValueError:
        print("could not smell Girth")
            
        return None
    except sr.RequestError:
        print("can't get through boss")
        return None


audio_process = None



def respond(response_text):
    global audio_prcoess
 
    print(response_text)
    s = response_text
    file = "file.mp3"
    tts = gTTS(s, lang='en')
    tts.save(file)
    audio_process = subprocess.Popen(["mpg123", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #os.system("mpg123 " + file)
def shutup():
    global audio_process

    # Check if the process is running and terminate it
    if audio_process is not None and audio_process.poll() is None:
        audio_process.terminate()
        audio_process = None
        
        
        
        
tasks = set()
listeningToTask = False

def delete_task(task_to_delete):
    global tasks
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        respond("Task removed: " + task_to_delete)
    else:
        respond("Task not found: " + task_to_delete)

def run_cider():
    try:
        subprocess.Popen(["cider"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Cider is running in the background.")
    except Exception as e:
        print(f"Error running cider: {e}")

def run_cura():
    try:
        subprocess.Popen(["cura"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Cura is running in the background.")
    except Exception as e:
        print(f"Error running cura: {e}")

def run_bot(command, girth):
    try:
        
        summary = "im girth mule. you're my 'mr. meseeks' only reply like he would"
        master_key = summary + command
        response = girth.chat(master_key)
        log.append("Girth GPT:"+ response + '\n')
        
        respond(response)
        
      
            
    except Exception as e:
        print(f"Error contacting MotherShip: {e}")

def main():
    global tasks
    global listeningToTask
    
    
    """
    Must have cookies from chatGPT profile saved to path
    """
    girth = ChatGPT("/home/mintymule/Documents/ai base/chat.openai.com.cookies.json")

    while True:
        command = listen_for_command()
        Keyword = "smart"

        if command and Keyword in command:
             log.append("Girth Mule:"+ command +'\n')
             if listeningToTask:
                tasks.add(command)
                listeningToTask = False
                respond("Adding " + command + " to your task list. You have " + str(len(tasks)) + " currently in your list.")

             elif "add a task" in command:
                listeningToTask = True
                respond("Sure Girthy, what's the task?")
             elif "list tasks" in command:
                if tasks:
                    respond("Sure, Girthy. Your tasks are:")
                    for i, task in enumerate(tasks, 1):
                        respond(f"{i}. {task}")
                else:
                    respond("No tasks currently in your list, Girthy.")
             elif "delete task" in command:
                task_to_delete = command.replace("delete task", "").strip()
                delete_task(task_to_delete)
             elif "open google" in command:
                respond("Opening Girth's Internet")
                webbrowser.open("http://www.google.com")
             elif "open carry" in command:
                 respond("Opening Girths Kaggle")
                 os.system("/opt/google/chrome/google-chrome --profile-directory=Default --app-id=ajdemkepbiggbelkgicfebbjokenncei")
             elif "open thonny" in  command:
                 respond("opening Thonny, code on, Girth")
                 os.system("thonny")
             elif "open kira" in command:
                respond("opening Cura, 3d print on, my boi")
                run_cura()
             elif "exit" in command:
                respond("Goodbye Girth, the realest there ever was. Wake me up soon.")
                break
             elif "open music" in command:
                respond("Playing Girth Jams")
                run_cider()
             elif "shut up" in command:
                 respond("Sorry Girth")
                 shutup()
                 
               
             elif "virus" in command:
                 respond("Hacking, real shit, bussin forreal forreal, my nigga. damn big hacks G")
                 import turtley
                 turtley.yoo()

             else:
                print("Contacting Mother Ship")
                
                
                run_bot(command, girth)
                logger(command)
            
        
    
                
if __name__ == "__main__":
    main()
    

