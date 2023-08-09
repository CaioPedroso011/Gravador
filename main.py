import cv2
import numpy as np
import pyautogui
import ctypes


ctypes.windll.kernel32.FreeConsole()
SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 15.0
name = 'C:\\Users\\Public\\Videos\\rec.avi' #local onde sera salvo a gravação
out = cv2.VideoWriter(name, fourcc, fps, (SCREEN_SIZE))
record_seconds = 60  #alterar para a quantidade de segundos que quer gravar

for i in range(int(record_seconds * fps)):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) == ord("%"):
        break
cv2.destroyAllWindows()
out.release()
