import ctypes
import os

class KeyMouseSimulation:
    def __init__(self):
        # Get the directory of the script
        script_directory = os.path.dirname(os.path.abspath(__file__))
        dll_path = os.path.join(script_directory, "kmbox_dll_64bit.dll")

        # Load the DLL
        self.kmboxA = ctypes.cdll.LoadLibrary(dll_path)

        # Set up the argument types and return types for KM_init
        self.kmboxA.KM_init.argtypes = [ctypes.c_ushort, ctypes.c_ushort]
        self.kmboxA.KM_init.restype = ctypes.c_ushort

        # Set up the argument types and return types for KM_move
        self.kmboxA.KM_move.argtypes = [ctypes.c_short, ctypes.c_short]
        self.kmboxA.KM_move.restype = ctypes.c_int

        # Initialize KMBox
        ts = self.kmboxA.KM_init(ctypes.c_ushort(0X99BA), ctypes.c_ushort(0xABCD))
        print("KMBox connected: {}".format(ts))

    def set_vidpid(self, VID: int, PID: int):
        self.kmboxA.KM_SetVIDPID(VID, PID)

    def press(self, vk_key: int):
        self.kmboxA.KM_press(ctypes.c_char(vk_key))

    def down(self, vk_key: int):
        self.kmboxA.KM_down(ctypes.c_char(vk_key))

    def up(self, vk_key: int):
        self.kmboxA.KM_up(ctypes.c_char(vk_key))

    def left(self, vk_key: int):
        self.kmboxA.KM_left(ctypes.c_char(vk_key))

    def right(self, vk_key: int):
        self.kmboxA.KM_right(ctypes.c_char(vk_key))

    def middle(self, vk_key: int):
        self.kmboxA.KM_middle(ctypes.c_char(vk_key))

    def side1(self, w: int):
        self.kmboxA.KM_side1(ctypes.c_char(w))

    def side2(self, w: int):
        self.kmboxA.KM_side2(ctypes.c_char(w))

    def move(self, short_x: int, short_y: int):
        self.kmboxA.KM_move(short_x, short_y)


    def click(self):
        self.left(1)
        self.left(0)


    def get_screen_size(self):
        width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        return width, height

    def posA(self):
        x1=win32api.GetCursorPos()[0]
        y1=win32api.GetCursorPos()[1]      
        return int(x1), int(y1)
    
    def posR(self):
        screen_width, screen_height = self.get_screen_size()
        x1,y1 = win32api.GetCursorPos()[0],win32api.GetCursorPos()[1]
        x = -(screen_width / 2 - x1) if x1 < screen_width / 2 else x1 - screen_width / 2
        y = -(screen_height / 2 - y1) if y1 < screen_height / 2 else y1 - screen_height / 2
        return int(x), int(y)

    def clickTo(self, short_x, short_y):
        short_x1 = short_x // int(1.6)
        short_y1 = short_y // int(1.6)
        self.move(short_x1, short_y1)
        if -2 <= short_x1 <= 2 and -1 <= short_y1 <= 0:
            self.left(1)
            start_time = time.time()
            while time.time() - start_time < 0.01:
                self.left(0)


    def clickTo2(self,short_x:int,short_y:int):
        short_x1 = short_x // int(1.6)
        short_y1 = short_y // int(1.6)
        self.move(short_x1, short_y1)
        if -2 <= short_x1 <= 2 and -1 <= short_y1 <= 0:
            start_time = time.time()
            self.left(1)
            while time.time() - start_time < 0.005:
                self.left(0)

                

    def clickTo3(self,short_x:int,short_y:int):
        if win32api.GetKeyState(0x05)<0 or win32api.GetKeyState(0x14):
            t = threading.Thread(target=self.clickTo(short_x,short_y))
            t.start()




            






# 本页面直接运行简单例子：
#a=KeyMouseSimulation() # chiamata in questo file
# a.move(100, 100)
    
# 其他页面调用运行简单例子：
# import kma
 #a=kma.KeyMouseSimulation() # quando lo richiami in altri file
#a.set_vidpid(0x99BA, 0xABCD)
#self.down(0xE1)
#self.up(0xE1)
