import math
class Color_Process:
    _THRES = 48.6199958864663
    def rgb2hex(self, rgb):
        r = rgb[0] >> 16;
        g = rgb[1] >> 8 & 255;
        b = rgb[2] & 255;

        hsp = math.sqrt(0.299 * (r * r) +0.587 * (g * g) +0.114 * (b * b))

        return hsp

    def dark_or_what(self, rgb):
        hsp = self.rgb2hex(rgb)

        # print(hsp)
        if hsp > self._THRES: return False
        else: return True
