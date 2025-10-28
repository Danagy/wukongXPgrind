# Original Script By Jackhammer Development (u/PreppyToast)
# Upgraded by Gulredy

# In settings \ Gameplay -> Disable Camera Assist!
# Script must be started when standing in front of Pool of shattered Jade.
# While standing there the "E" activate must be highlighted to be hit.

import pydirectinput as controller
import time

time_to_wait = 10
print(f"You have {time_to_wait} seconds to switch to game")
iterations = 200

for i in range(time_to_wait, 0, -1):
    print(i)
    time.sleep(1)

# Start Menu Interaction 
# this resets the camera position
# Needed only once, if mouse\keyboard is not touched.
controller.press('e')
time.sleep(3.3)
controller.press('esc')
time.sleep(2) # 2.6


for i in range (iterations):
    print (f" Start Iteration {i+1}")
    
    # Engage running
    controller.keyDown('shift')
    
    # Start Walking To Target Position
    # Move back a bit
    controller.keyDown('s')
    time.sleep(0.4) # 1.8
    controller.keyUp('s')
    
    # Move to the right
    controller.keyDown('d')
    time.sleep(4) # 6.8 
    controller.keyUp('d')
    
    # Move up
    controller.keyDown("w")
    time.sleep(0.2) # 0.5
    controller.keyUp("w")

    # Move strafe up
    controller.keyDown("w")
    controller.keyDown('d')
    time.sleep(0.1) # 0.5
    controller.keyUp("w")
    controller.keyUp("d")
  
    # Activate cloud step
    controller.press('2')
    time.sleep(0.3)    

    # Move up
    controller.keyDown("w")
    time.sleep(1.2) # 2.8
    controller.keyUp("w")
    
    # Disengage runnig
    controller.keyUp('shift')
    
    # Initiate Attack
    controller.press("4")
    time.sleep(1.5) #3
    controller.press("4")
    time.sleep(4) #6

    #Reset
    controller.press('q')
    print (f" Completed Iteration {i+1} \n")
    time.sleep(15) # This value highly depends on your computer loading speed!
