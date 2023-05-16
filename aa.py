from bardapi import Bard
import os
from dotenv import load_dotenv
load_dotenv()
bard = Bard(timeout=20)
prompt = '''You are an advanced AI assistant in Chrome Dev Tools. Now an element is selected at $0. Just send the JS code for the following task and nothing else.
Input: Get the text content of the element.
Output: $0.textContent
Input: Get the value of the element.
Output: $0.value
Input:
'''
# https://en.wikipedia.org/wiki/List_of_banks_in_India
# list the first row of the selected table
# calculate time
import time
from chatgpt_wrapper import send_msg
# register a shortcut key
from pynput import keyboard
from pyperclip import paste,copy
from pyautogui import hotkey
# beep sound
import winsound
def beep():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

def process():
    beep()
    old = paste()
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    new = paste()

    # response = bard.get_answer(prompt+new)['content']
    response = send_msg(prompt+new).split('Output: ')[-1].strip()
    print(response)
    copy(response)
    hotkey('ctrl', 'v')
    copy(old)


with keyboard.GlobalHotKeys({
        '<alt>+z': process
        }) as h:
    h.join()