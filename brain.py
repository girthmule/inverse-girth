import os
from gtts import gTTS
import webbrowser
from WebChatGPT import ChatGPT  
import speech_recognition as sr
import subprocess
import requests
import ears
import mouth


log = []


def logger(command):
    with open('log_file', 'a') as log_file:
        print('Girth logging')
        
        log_file.write('\n'.join(map(str, log)) + '\n')
        print('Girthy Log Dumped')


def run_bot(command, girth):
    try:
        
        summary = "im girth mule. you're my 'mr. meseeks' only reply like he would"
        master_key = summary + command
        response = girth.chat(master_key)
        log.append("Girth GPT:"+ response + '\n')
        
        mouth.respond(response)
    except Exception as e:
        print(f"Error contacting MotherShip: {e}")

