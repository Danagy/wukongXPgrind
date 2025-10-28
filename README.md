#### How to set up the script:

### Download python
https://www.python.org/downloads/

### Install python (Windows)
1. In the installer click on "customize installation"
2. Make sure pip is installed. 
3. Make sure "add it to the path" option is selected.


### Install required lib
1. Start a new CMD session
2. type: pip install pydirectinput

### Prepare the game to execute the script:
!!!! This is really important step, skipping it will make the script execution faulty !!!!
When you start the game, go to the settings \ Gameplay and disable "Camera assisst".
This makes the camera to be static and not trying to follow the back of your character.
Otherwise the camera would turn when you move and the direction of the move would change.

### How to run the script
1. git clone or download the "BlackMythWukongFarm.py" file and place it on your pc, where it does not require admin rights to execute.
2. In the CMD window navigate to the path where the py script file is.
4. Start the game and travel to "Pool of shattered Jade" which is in Chapter 4.
5. Make sure that you stand at the Incense shrine in a way that it shows you the "E offer incense" option.
6. Alt+Tab to the CMD, and type "BlackMythWukongFarm.py"
7. It will count down from 10, and you will need to Alt+Tab back to the game making sure that step 4 is still valid!
8. The script will run. Don't touch the keyboard or the mouse at all.

### How to stop the script during execution?
The best option for this is to wait until the game starts to load. 
Quickly Alt+Tab to the CMD and hit CTRL+C to break the execution.

### How to set up the iterations?
In the script you can find at line 13:
iterations = 200
Modify this number to an integer value will represent how many times the xp farming will be executed. (sets the loop counter)
