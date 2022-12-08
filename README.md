## bouncy-window
It's not a ghost, it's gravity

This program can simulate the effects of gravity on a window
- Watch a [DEMO VIDEO](https://youtu.be/naj3HBQeBLY) of this project

## info
use the class `Gravity` to add gravity effect to any Tk window (like this: `Gravity(root)`) more info below:
the class Gravity takes 1 to 3 arguments
```
Gravity(master, gravity, bounce_factor)
```
default values for gravity and bounce_factor, if they're not passed as arguments are 3 and 0.6 respectively

- master: pass a tkinter window of type `Tk` here

- gravity: integer value for the magnitude of gravity acted on the window 
  - ranges from 0 to 100
  - 0 means the window is free to move anywhere
  - any other value (let's say N) means the window will move an additional "N" number of pixels every 10 ms (basically acceleration is N px/10 ms^2)

- bounce_factor: (float) fraction of the previous height the window will reach upto after every bounce
  - ranges from 0.0 to 1.0
  - 0 means the window will not bounce at all (0 times the previous height), therefore will just stick to the ground like a magnet
  - 1 means the window will bounce till the same height every time, therefore bouncing forever
  - any other float value (lets say N) means the window will bounce upto "N" times the previous height, ultimately settling on the ground

## usage
run the file to get an error box with the gravity effect

or

To add the effect to your custom tkinter window

- import class `Gravity` from the file `bounce.py` to the python file you want
- in case you don't already have your desired tkinter window, make a tkinter window of the type `Tk` (suppose it's named `root`) and customise it as you wish (don't execute `root.mainloop()`, Gravity class will handle that)
- then use:
```
Gravity(root)
```
to get a gravity effect on the window with default values `gravity=3, bounce_factor=0.7`

```
Gravity(root, 7, 0.8)
```
to get a gravity effect on `root` with suppose values `gravity=7, bounce_factor=0.8`
