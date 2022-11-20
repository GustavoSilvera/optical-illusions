# 85-211 EAC (Extension Application Creative) project
## Gustavo Silvera
### CMU Psychology F22

# Optical Illusions Minigame

Welcome to Gustavo's 85-211 E/A/C Fall 2022 project: Optical Illusions Minigame
- This optical illusion minigame has you play through a game for catching (clicking) circles of various colours. However, all the circles are actually the same colour! There is an illusion based off which rows (red/green/blue) are rendered over each circle which skew our perception of colour (especially in motion!) and make it seem like the circles are coloured differently. 

This effect is strongest with the thinnest (and most frequent) rows, you can change this parameter (resolution) at runtime to see this effect for yourself!

Also pay attention to the messages (both on screen and in the terminal) for further instructions!

# Installation
**NOTE** You can actually demo this game entirely in your browser here

The only dependency for this application is `python3` ([https://www.python.org/downloads/](https://www.python.org/downloads/)) and `pygame` ([https://www.pygame.org](https://www.pygame.org)).

Once `python3` is installed, you can install `pygame` with:
```bash
pip install pygame
```

# Running the game
```bash
python3 illusion.py
```

![screenshot.jpg](screenshot.jpg)

You'll get the following output from the terminal where you launch the game and play through it.
```txt
Welcome to v1.0 of Gustavo's illusion game!

Controls:
 -- Click on a circle to reveal its true colours!
 -- Up/Down arrows to change the "resolution"
 -- Press 'R' to reset the reveal status
 -- Press SPACE to pause/unpause the game
 -- Press ESC to quit the game

INSTRUCTIONS:
1. Reveal (click) all the RED circles
2. Reveal (click) all the GREEN circles
3. Reveal (click) all the BLUE circles

Have fun!
Revealed a "GREEN" circle to be "BROWN" -- (Done 1/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 2/20)
Revealed a "GREEN" circle to be "BROWN" -- (Done 3/20)
Revealed a "GREEN" circle to be "BROWN" -- (Done 4/20)
Revealed a "GREEN" circle to be "BROWN" -- (Done 5/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 6/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 7/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 8/20)
Revealed a "GREEN" circle to be "BROWN" -- (Done 9/20)
Revealed a "GREEN" circle to be "BROWN" -- (Done 10/20)
Revealed a "GREEN" circle to be "BROWN" -- (Done 11/20)
Revealed a "RED" circle to be "BROWN" -- (Done 12/20)
Revealed a "RED" circle to be "BROWN" -- (Done 13/20)
Revealed a "RED" circle to be "BROWN" -- (Done 14/20)
Revealed a "RED" circle to be "BROWN" -- (Done 15/20)
Revealed a "RED" circle to be "BROWN" -- (Done 16/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 17/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 18/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 19/20)
Revealed a "BLUE" circle to be "BROWN" -- (Done 20/20)

Congratulations you found all the secrets!
As it turns out... All of these circles are actually the same colour!
This is simply an optical illusion to for perceiving colours on circles
similar to how we perceive colours on a pixel-based screen!
Illusions are fun!

Press 'R' to restart the game
```