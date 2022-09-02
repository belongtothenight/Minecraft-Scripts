import pythoncom
import pyHook


def uMad(event):
    return False


hm = pyHook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()

# https://stackoverflow.com/questions/7529991/disable-or-lock-mouse-and-keyboard-in-python
