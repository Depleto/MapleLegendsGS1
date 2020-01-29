import pyautogui
import time


# TODO:
    # Selling function 


def active_window():
    '''
    Make maplelegends the active window
    '''
    print("Finding MapleLegends Window...")

    try:
        maple_window = pyautogui.getWindowsWithTitle("MapleLegends")[0]
        print("MapleLegends Window Found...")
    except:
        print("Cannot Find MapleLegends Window... Program Terminating")
        exit(1)


    if maple_window.isActive == False:
        pyautogui.click("taskbaricon.PNG")

    pyautogui.click(maple_window.box)



    print("MapleLegends Window Activation Successful")

def get_window_coordinates():
    maple_window = pyautogui.getWindowsWithTitle("MapleLegends")[0]
    return maple_window.box

def refresh_buffs():
        #pyautogui.press("delete") # Magic guard
        #time.sleep(2)
        pyautogui.press("pagedown")
        time.sleep(2)
        pyautogui.press("end")

def player_teleport(direction):
    pyautogui.keyDown(direction)
    pyautogui.press("ctrl" , presses=2 , interval=.2)
    pyautogui.keyUp(direction)

def platform_loot(): # loots gs1 platform, must have pet out
    player_teleport("up")
    while not pyautogui.locateOnScreen("left_platform.PNG", region= maple_window_box):
        for i in range(2):
            player_teleport("left")
        pyautogui.press("w", pause=.5)

    print("Upper left found...")

    player_teleport("down")

    tries = 0
    while not pyautogui.locateOnScreen("bottom_left.PNG", region = maple_window_box): #failsafe 1
        pyautogui.keyDown("left")
        pyautogui.press("w", pause=1)
        tries +=1

        if tries > 10:
            player_teleport("down")
    pyautogui.keyUp("left")
    print("Bottom left found...")

    while not pyautogui.locateOnScreen("bottom_right.PNG", region=maple_window_box):
        if pyautogui.locateOnScreen("top_right.PNG", region = maple_window_box):
            player_teleport("down") #failsafe 2
        for i in range(2):
            player_teleport("right")
        pyautogui.press("w", pause=.5)
    print("Bottom right found...")

    tries = 0
    while not pyautogui.locateOnScreen("right_platform.PNG", region = maple_window_box): #move back and forth until under stairs and then tp up
        pyautogui.keyDown("left")
        pyautogui.keyUp("left")
        pyautogui.press("w")
        tries += 1

        if tries > 40:
            while not pyautogui.locateOnScreen("bottom_right.PNG", region = maple_window_box):
                player_teleport("right")
            tries = 0



    player_teleport("up")
    print("Teleported to stairs...")



def feed_pet():
    pyautogui.press(".",  pause=.5)







#############################################################
# end of functions

#############################################################

if __name__ == '__main__':
    active_window() # Activates MapleLegends window
    maple_window_box = get_window_coordinates()


    loops = 0

    refresh_buffs()
    start_time = time.time()
    while True: # Main loop
        if loops > 0:
            if loops % 5 == 0:
                refresh_buffs()

            elif loops % 20 == 0:
                feed_pet()


        timeout = time.time() + 10 # Kill monsters until anti-macro activates
        while True: # 60 seconds of killing
            if time.time() > timeout:
                break
            else:
                pyautogui.press("w" , pause = .5)

        platform_loot()
        loops += 1
        print(f"Loops completed: {loops}")



