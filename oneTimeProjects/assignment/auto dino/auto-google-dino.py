from PIL import ImageGrab
import pyautogui

while True:
    screen = ImageGrab.grab()
    # screen.show()
    color_count = {}
    # width, height = screen.size
    rgb_image = screen.convert("RGB")
    for x in range(300, 500):
        for y in range(275, 350):
            rgb = rgb_image.getpixel((x, y))
            if rgb in color_count:
                color_count[rgb] += 1
            else:
                color_count[rgb] = 1
    if color_count[(83, 83, 83)] > 930:
        pyautogui.press('space')
