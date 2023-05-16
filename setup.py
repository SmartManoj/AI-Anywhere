extension_url = 'https://chrome.google.com/webstore/detail/copy-cookies/jcbpglbplpblnagieibnemmkiamekcdg'
import webbrowser
webbrowser.open(extension_url)
from pymsgbox import alert
alert(text='Please install the extension and click OK', title='Copy Cookies', button='OK')
webbrowser.open('https://bard.google.com')
from pyautogui import hotkey
from pyperclip import paste
old = paste()
hotkey('ctrl', 'shift', 'k')
new = paste()
if old == new:
    alert(text='It is not Google Chrome. So, please click the extension to copy the cookies.', title='Copy Cookies', button='OK')
    new = paste()

import json
new = json.loads(new)
# get __Secure-1PSID from new
cookie_name = '__Secure-1PSID'
for i in new:
    if i['name']==cookie_name:
        key = i['value']
        print(key)
        # _BARD_API_KEY
        import os
        os.system('setx _BARD_API_KEY ' + key)
        # write to .env file
        with open('.env', 'w') as f:
            f.write('_BARD_API_KEY=' + key)
        break
else:
    print(cookie_name + ' not found')