import display
import time
import buttons

from machine import Pin
from neopixel import NeoPixel

blub = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00;\x00\x00\x00(\x08\x06\x00\x00\x00@g\x82\x86\x00\x00\x00\tpHYs\x00\x00\x07f\x00\x00\x07f\x01\xc7\x87\x1e\xc9\x00\x00\x00\x19tEXtSoftware\x00www.inkscape.org\x9b\xee<\x1a\x00\x00\x08+IDATh\x81\xe5\x9a\x7fl\x9de\x15\xc7?\xe7y\xef]\x7f\xb2\x1f\xdd\x9a\xfd\xb8\x05:\x03\xc4 cY \x93\xcd\xcdy]\xbbb\x81\t3T\x12\x8d\x81\x98\x00\x0eR\xa5\xb6\xdd\x1cjs%2\xbaM~,\x13D\x8d\x11A3\x86\xe8T\xd8V\xba\xa5a\x10\x04\x03q\x0e\xa7Q\xb7\xd9\xba\xdev\xb8\xb1\xael\xfdy\xef\xfb\x1c\xff\xb8\xbd\xd8\xdd\xbe\xf7\xde\xf7\xb67`\xe27\xb9\x7f\xbc\xcf9\xcf9\xdf\xef\xfb\xbc?\xce\xfb\x9c+\xaaJ:To\xe8\xb9\x03\xd5\xfb\x80\n\xe0\x95\xb85_\xee\xd86\xfft\xda\t\x19\x10n\xec\x9d\xe38Z\x87\xea2\x812\x85\x7f\x0b\xf2\xca\x90L{\xee\xd5\xd69\xe7&\x13\xb3v\xd3\xc9\xf2x\xcc}\\\x85U\xc0iE~z\xb6\xbf\xf7\x917\x9f\xbc&\xe6\xe5/\xe9\xc4V7G\x9f\x04\xee\x1c?\xa6\xca\x9f\x08\xb2z\xff\x83\xa1ws!\xb5\xa6\xb9\xe7\x1eE7\x03\x17y\x98O\xa1\xdc\xdb\xbe5\xb4+\x97\x98\xd77t\x97\xb9\x01\xe9\x00\xaeN1\xbd\x1e\x1c.\xaa\xd9\xb3\xbd\xec\xbd\xd49\xc6\x93\xdc\x86\xe8\xdd\xa4\x08\x05\x10a\xb1\xb8\xb4_\xdf\xd0]\xe6\x97Tus\xf4\x01Ew\xe0-\x14\xa0\x1ca\xe7XN\x7f17\x1e\x9f\xe1\x06L\x1b\x13\x85\x02\\\x17+\x1c\xfa\x89\xd7<O\xb1\xaa4\xa5\xcd\xa4,q\x83\xf2R\xf8\xbe\xce\x99YI5\xf5T\x01\xf7g\xf3\x03D\x95\xed5M\'\xae\xca\xe6\x18\x8e\x9c*\xc5\x16\xec\x05\xbd6\x83\xdb\xba\xaa\xafG\xafH\x1d\xf4\x14\x0b\x842fT\xae\t\x06\x83m\xd5\x1b\x8f\xcf\xc8LM[\x00\xc9\xec\xf3>\x82jL\xc6\x13\xb36\xd2[\x1c\x18\x18}\x01X\x96%\x96\x88\xd1\x05\xa9\x83\xdeb\x85m\xd9\x98),\xc5\x16\xec\xab\xad?3\xdd\xcb^\xbb\xe9d9\xc2\xf2lq.\x88i\xb91\x1c!\xe0e\x0bG:\x0b\x87\x06\xdc_\x03\xab\xb2\x06\x12\xfe^T\xea\xfc!u\xd8Sl{k\xe8\x9b\x82n\xf1\xc1\xef\xbaX\xe1\xd0\xbe\x15\x1bNO\xb8\x1fG\xdc\xf8\xc2t\xf13\x90,e0:/u\xf8\xda\xbb\xde\n:\x03\xc1] k|D\xe9\n\x18\xa7\xe6\xb7-\xf3\x07S\ri\xc9\xb4o\xad\xd8\x88\xea\x0e\x1f\xc1\x97\x15\xdb\x91\t\x82\x1d\xd4\xfa\x98;\x11\x1a\x8b\x8f?\xac\xab\xc3)\x9b9\xefg\x027\xf9\x98\xdd\x15p\x9cO\xed\xdd<\xaf\xd3\xcb\x98V\xac*\xba\x7f[E=\xca\xe3Y\xf9\t\xcb\x8b\xec\xc8\x9ep\xe4Tirl\x9a\xd1c\x80\xeb\x83\xe0x\x9c-\xef\xac<\x95<\x88D0}\x95=O\xa9r\x9b\x8f\xb9\x19\x85B\x96\xcb,!8t/\xf0\x83\xac\xa9\x84\x15\x81\x81\x91=5M\xef\x94\x00\xbc\xb0\xf9\x92>\xa0\xc3\x07\xc9\xff\xe6\x83\xdd\xbbv%N\x90\x08\xf2\xea@\xf4\t\xd0/\xf8\x98\x9aU(\xf8\xb8\xa7T\xd1\xfd[C\xeb\x81\x1ff\xcf)+\xad\xc4w/o\xe8.J\x1c\xf2-\xfc\xaf\xee\x908\xee\x03\x90\x10Z\xd5\x18\xdd\x81\xc7\xbb\xde\x03\xbe\x84\x82\xcf\x07\x88*\xba\xa2$\xf4\x15\x85g|\xb8W\x95\x04\xd8\x1d\x8et\x16\xb6\xb7\x86^Gi\x04\xd2\xd7\xa4\t\xc4Qno\xdf|\xc9q\x80\xea\xa6\xee\x87\x10\xd6\xfb\xc8\xe5[(d(\x17\xbdPW\x87\xd3W\xd9\xf3\x94\xafKK\xa5-^:zsGK\xe5puS\xb4\x0e\xc3\xa3(\xf3\'\xfaqT\x0cw\xbf\xd4\x1a:\x00P\xd5\x1c\xfd\xae\xc0&\x1ftr\x12\n9\x8a\x85\x84\xe0\xb3\x0b\xa3\xcf\xf8{h\xc8\xbe\xe0\xf0\xe0\xcd{\xb6_6\xb26\xd2[<<`oPX\xa60KTO\xa9\xc8\xc1\xb2\x92\xfe\x97v\xb5\\9\n\xb0\xa6\xb9\xe7\xdb\x8aF\xb2EU\xe8\x0c:N8\x17\xa10\t\xb1\x90\\\xe1\xe8\xcf\x81\xcfgM \xec\r\x0c\r\xdd\xb2g\xfbe#\x99\xfc\xaa\x9b\xa2_Cx$[\xbc\xc9\n\x85I\x8a\x05\xa8\x8b\xfce\xda\x99\x81\x19\xbf\xf4\xf9\xfe;\x00\x1c\x9b\x98\x9d\x99(\x02\x14\x017\xfa\x88s\xcc\xb8\x12n\xfb\xde\x82\x13\xb9\xb1\x1dK7Y\xb1\x90\x10\xdc70\xe3y\xfc\x11\x9d\x12\xa6\xb2\xa2I\xe4V\xce\xa5`W\xcb\x95\xa3\xb3J\xfa?\x87\xf0\xe2T\xe2dC>\x84\xc2\x14W6\x89\xe5\r\xddE%\x01\xf9\x1d\xb0z\xca\xc1R\x90/\xa10\xc5\x95M\xe2\xb5\x87+\x86\x8aJ\xccZr\xac\x98\xb2!\x9fB!O+\x9bDM\xd3;%Vb{AVN9\x98\xd0\x1b\x87\xa5\x1d\xad\xa1\xee<P\x03\xf2\xb4\xb2I\xb4m\x9d;`2\xedr\xe4\x00E\xfe\x91O\xa1\x90g\xb1\x00\xaeN\xf2\xd3\xee\x03@\xde\xc5:\x04\xfe\x7f\xc4\xc6M\xd6\xa2\xffC\xc3\xa4\x1eP\xb5\xf5g\xa6\x8f\x14\x0f_e\xac^\xa6\xca\xa5"T\x88p\xb1\xc2\xdfDyJ\xe1\x8fS%\xa6"\x07\xad\xc4\xd7;\xd6\xd9\x02\xfc\x0b\xb4K0]\xa2\xf6\xf8hi\xc1\x91\x8e\x96\xf2\xf3\xb9\xc6\xf4\xdc\xdc\x1a\x8f\xda\xfa\xa3\x05\xf1\xc2\xc2\xebT\x08\xa3\xb2\x04t\x11\x85\xb2\xd0\x8c]\xac2\xb6w8v\xce\xce\x1b\x83\xbay\xba\x90\xc5\x06\x0b\xc0\xd6\x8e\x1d\xa1(*B``\xd4V7G\x8f\x01\x87\x04\x0e\xa91\x07\xfb\xfaz\xdeH\xd7\tx?\x9e\xd7\xca\xd6n:Y\x1e\x8b\xc7o\x03\xf9,\xb0\x9cD\xed:\x1e\xe7\x80\xc3\x8a\x1e\x12\xe4\x88\xb5\xda\x19\xc0\xf9\xe7\xe8E#\x9d\x81\xa1\xc0\xe5X9<U\xa1*rp\x7f\xeb\x82U\xe1\xe6\xcey\x8e\x06\x17\x1a\x91J\xe0rU]\x8c\xe8\x12\x90\x85\x17N\xe0<\x86\x97Q^,p\xdc\x9dc;%\xe9\xc5\xaei\xee\xf9\x84E7\x08\\\x0f\x04\xc7\xf9Y\xe0eD\xf6Z\x95\x03\x9f,\x99\x7f\xa8\xa5\x05\xcf\xf5\xabi:q\x95\x15\xf3v\xbe\xc4\xa6\xb3\xd7n:Y>\x1a\xb3\xabEl5\xc8-\xc0\xacq\xe6a\xe07\x08\x8f\xb6\xb7\x86^O\x0e\x8a\xaa\xf2\x99o\x9c\xac\x8c\xbb\xeec\xc0\xda\x94\x98\xc3\xa8<fU\x9e8\xb0m~\x97\x1f\x92U\x8d\'\xaf\x14\xe3\x1e\xc9A\x97\'\xb2\x89\x1d\x8fp\xa4\xb308\x18\xbc\xd5*\xdf\x11\xa8\xbc0\x0c\xcf\xc6\xa0\xa9\xa35\xd4-\xab\x1bO\\-"\x1d@j\xff\xe6\x84\xe3\xe8\xa7\xf7m\xae8\x9a\x0b\xc9\x9a\xc6\xde\x8fZc\xff\x9a\xcb\x1c/\xe4"6\x89\xe5\r\xddE%Ay\x0e\xe5\x86\x14\xd3;\x88\t\x1b#\xf2#&\n\x05\xd5\x8d\xb9\n\x05\x889y\xac?s\xc4k\x0fW\x0cY\xd7\xdc\xe3a\x9a+\xd6\xfe\xd8(x7\x93Dr:\xabI\x04\xd4~\xa8E\x851n\xea\xad\x08\x80\n\x8b\x02(\xcf"\xdc\xe1a\xbf\xb3\xba):\'n\xf8j.5\xaaqP7\xd7\xad\xf1<\xa0\xb6\xfe\xcc\xf4x\xe1\xe0\xfd \x8d^v\x85\xe7\x03\xf1\xd2i\xf5\x81\xf3\xb1\x05\x88\xd6L\xf0\x10\xd6\x05\x94\x9b\xaa\x9b\xa3\xbfR1;\x1dk\xda\xdb\xb6\xce\x1d\xc8\x94\xd4\xc5Zp\xf2$!3\xae\xbd\xeb\xad\xe0\xec\xe9\xf3V\xba\xa2\xeb\xa4P\xbe\x04\xe2\xdd\x03Visp\xee\x15UE\x04\xa9n\x8e~\x11\xe5AM\xfc\xa5 \x1dF\x80\xdf\xa3\xf2\x86`\xdfpE\x0f\xcf\xee\xbc\xb83\xb9\x8b\x0fP\xb5):[\xe2|\x1f\x98\x03\xcc\x1e\xfb\x95\x023\xc9\xdc\xbe\x8c\x03g\x81~\x84\xb3(\x07\xdb\xb7\x84\x1a\xc6;\xacn\xe8\x0e9\x01\xe7cV\xed\xc7EX\n\xac\x042\xb5M\xbbThYY\x1cz\xba\xa5\x05{\xc1{vm\xa4\xb7xp\xd0\xde*\xca\xed$Z\x83~z\xab\xa3\xc01\x85\xa3\x06zT\xa5W\xc4F\x15\xfaP\xd3oT\xfa$\xe8\xf6\xbbX\x1bw\xed\xe0\xac@0\x16\x8f\xc5\x13m\xce\xd2i\xee\xd0p,\x00`\xdd\xe0L\xa3\xeet03\x10\x9d\xa1BHT\xe6+T\x08z)\xca\x15\x08\xa5\x99\x88\x8c!Y\x13<\x1d\x1c\x1a\xfc\xc5\xf8]\xcd\xb4\xb5\xf1\xea\xc6\xdeK\x8d\xb1\xb5(U\x08a.|i\xff\xaf\xe1]\x94\x971\xd2\x11Gw\xa7{\xc6\xf8\xfa\x10\xa8\xab\xc39[\x19]\xa4"KTu\xb1\xc0b`\x11\x89K\xf4\x83\xc6)\xe00\xc2\xdbj\xe5\xcf\x01G\xdf\\V\x14z;]E7\x1eS\xda\x96\xa9\xad?3}\xb4`\xb0R0\x0bEl%\xb0\x00a\xb6US\x860[T\xcb\x80b\x84"\x94B\x12\xb7E\xf2\xbf\x18q\x1256$\x9a_\xef\xa9rN\x84>\x943b\xb4O\xad9\x8d\xa1\xdbX\xba\\l\x978\xa3]\xed\x0f}\xa4\x7f\xb2|\xff\x03)\xcdoRp\x9c\xb9\xd0\x00\x00\x00\x00IEND\xaeB`\x82'


display.drawFill(0x000000)
display.drawPng(0, 0, blub)
display.flush()

class Pixels:
    def __init__(self):
        powerPin = Pin(19, Pin.OUT)
        dataPin = Pin(5, Pin.OUT)
        self.np = NeoPixel(dataPin, 5)
        powerPin.on()
        self.color = "white"

    def white(self):
        self.set_color((255, 255, 255))

    def red(self):
        self.set_color((255, 0, 0))

    def green(self):
        self.set_color((0, 255, 0))

    def orange(self):
        self.set_color((255, 165, 0))

    def blue(self):
        self.set_color((0, 0, 255))

    def black(self):
        self.set_color((0, 0, 0))
        
    def set_color(self, color):
        if self.color == color:
            return
        self.color = color
        self.np[0] = color
        self.np[1] = color
        self.np[2] = color
        self.np[3] = color
        self.np[4] = color
        self.np.write()

class Timer:
    def __init__(self):
        self.pixels = Pixels()
        self.paused = False
        self.going_up = True
        self.going_target = False
        self.mode = "up"
        self.direction = "up"
        self.target_time = 90000
        self.reset()

    def reset(self):
        self.current_time = 0
        self.prev_time = 0
        self.remaining_time = 0
        self.start()

    def start(self):
        self.start_time = time.ticks_ms()

    def pause(self):
        self.paused = True
        self.prev_time = self.current_time
        self.remaining_time = self.current_time
           
    def resume(self):
        self.paused = False
        self.start()

    def get_mode(self):
        return self.mode

    def set_mode(self, new_mode):
        self.mode = new_mode

    def increase_target_seconds(self):
        self.target_time = self.target_time + 1000

    def decrease_target_seconds(self):
        self.target_time = self.target_time - 1000
        if self.target_time < 1000:
            self.target_time = 1000

    def increase_minutes(self):
        self.remaining_time = self.remaining_time + 60000

    def decrease_minutes(self):
        self.remaining_time = self.remaining_time - 60000
        if self.remaining_time < 0:
            self.remaining_time = 0

    def decrease_seconds(self):
        self.remaining_time = self.remaining_time - 1000
        if self.remaining_time < 0:
            self.remaining_time = 0

    def count_up(self):
        self.pause()
        self.reset()
        self.going_up = True

    def count_down(self):
        self.pause()
        self.going_up = False

    def tick(self):
        if self.paused:
            offset = 0
        else:
            offset = time.ticks_diff(time.ticks_ms(), self.start_time)
        if self.going_up:
            self.current_time = self.prev_time + offset
        else:
            self.current_time = self.remaining_time - offset
        if self.going_target:
            changed = False
            if self.get_mode() == "target":
                target_offset = self.current_time % (self.target_time / 2)
                if target_offset < 15000:
                    self.pixels.green()
                    changed = True
                elif target_offset < 30000:
                    self.pixels.orange()
                    changed = True
                elif target_offset > (self.target_time - 3000):
                    self.pixels.green()
                    changed = True
                else:
                    self.pixels.red()
                    changed = True
            elif self.get_mode() == "target3":
                target1_offset = (self.current_time + 3000) % (self.target_time / 2)
                target2_offset = (self.current_time - 1000) % ((self.target_time + 10000) / 2)
                target3_offset = (self.current_time - 5000) % ((self.target_time + 20000) / 2)
                colors = []
                if target1_offset < 10000:
                    colors.append(self.pixels.green)
                if target2_offset < 10000:
                    colors.append(self.pixels.orange)
                if target3_offset < 10000:
                    colors.append(self.pixels.red)
                for index, c in enumerate(colors):
                    if int((self.current_time / 500) % len(colors)) == index:
                        c()
                        changed = True
            if not changed:
                self.pixels.black()
        else:
            if self.current_time <= 0:
                self.pixels.red()
            elif self.current_time < 20000:
                self.pixels.orange()
            elif self.current_time < 40000:
                self.pixels.green()
            elif self.current_time < 60000:
                self.pixels.blue()
            else:
                self.pixels.black()
    
    def get_current(self):
        return self.current_time
    
    def get_paused(self):
        return self.paused

    def get_count_up(self):
        return self.going_up

timer = Timer()

def reset_timer(pressed):
    if pressed:
        timer.reset()

def pause_timer(pressed):
    if pressed:
        if timer.get_paused():
            timer.resume()
        else:
            timer.pause()
    
def press_home(pressed):
    if pressed:
        if timer.get_mode() == "up":
            timer.set_mode("target")
            timer.going_target = True
            timer.count_up()
        elif timer.get_mode() == "target":
            timer.set_mode("target3")
            timer.going_target = True
            timer.count_up()
        elif timer.get_mode() == "target3":
            timer.set_mode("down")
            timer.going_target = False
            timer.count_down()
        else:
            timer.set_mode("up")
            timer.going_target = False
            timer.count_up()

def press_menu(pressed):
    if pressed:
        if timer.get_mode() in ["target", "target3"]:
            timer.increase_target_seconds()
        else:
            timer.increase_minutes()

def press_select(pressed):
    if pressed:
        if timer.get_mode() in ["target", "target3"]:
            timer.decrease_target_seconds()
        else:
            timer.decrease_minutes()
    
def press_start(pressed):
    if pressed:
        if timer.get_mode() in ["target", "target3"]:
            pass
        else:
            timer.decrease_seconds()

buttons.attach(buttons.BTN_A, reset_timer)
buttons.attach(buttons.BTN_B, pause_timer)
buttons.attach(buttons.BTN_HOME, press_home)
buttons.attach(buttons.BTN_MENU, press_menu)
buttons.attach(buttons.BTN_SELECT, press_select)
buttons.attach(buttons.BTN_START, press_start)

while True:
    time.sleep_ms(100)
    timer.tick()
    result = timer.get_current()
    if result < 0:
        text = "-"
        result = result * -1
    else:
        text = ""

    text = text + f"{int(result / 60000):02}:{int((result / 1000) % 60):02}"
    font = "ocra22"
    display.drawFill(0x000000)
    display.drawPng(0, 0, blub)
    width = display.getTextWidth(text, font) * 3
    height = display.getTextHeight(text, font) * 3
    display.drawText(int((320 - width) / 2), int((240 - height) / 2), text, 0xffffff, font, 3, 3)

    text = timer.get_mode()
    if timer.going_target:
        target = timer.target_time
        text =  text + f" {int(target / 60000):02}:{int((target/ 1000) % 60):02}"
    width = display.getTextWidth(text, font) 
    height = display.getTextHeight(text, font) 
    display.drawText(int((320 - width) / 2), 10, text, 0xffffff, font, 1, 1)

    display.flush()
