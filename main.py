from dotenv import load_dotenv
load_dotenv()

system_prompt = '''You are an advanced AGI assistant in Chrome Dev Tools. Now an element is selected at $0. Just send the JS code for the following task and nothing else without code block.
'''
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Get the text content of the element."},
    {"role": "assistant", "content": "$0.textContent"},
    {"role": "user", "content": "Get the value of the element."},
    {"role": "assistant", "content": "$0.value"},
]
import winsound

import litellm

def send_msg(msg):
    response = litellm.completion(
        model="gemini/gemini-2.0-flash",
        messages=messages + [{"role": "user", "content": msg}],
    )
    return response['choices'][0]['message']['content']

from pynput import keyboard
from pyperclip import paste,copy
from pyautogui import hotkey
def beep():
    duration = 100  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

def process():
    beep()
    old_content = paste()
    for _ in range(1):
        hotkey('ctrl', 'c')
        new_content = paste()
        if new_content != old_content:
            break
        hotkey('ctrl', 'a')

    response = send_msg(new_content).split('Output: ')[-1].strip()
    print(response)
    copy(response)
    hotkey('ctrl', 'v')
    copy(old_content)


with keyboard.GlobalHotKeys({
        '<alt>+z': process
        }) as h:
    print('Listening for Alt+z...')
    h.join()