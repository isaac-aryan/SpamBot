#Bot that spams text in any text field or textbox

#Imported Stuff
import pyautogui, time

time.sleep(5)

f = open("spamtext", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
