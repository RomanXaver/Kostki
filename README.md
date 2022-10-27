# Kostki

Python Version = 3.9

Welcome to the game "Kostki"!
The way you play the game is pretty simple:

In the beginning you roll your dice and try to collect points.

The points are counted as following:
Only 1 and 5 can be picked up separately. 1 = 100 points and 5 = 50 points
3x 2 = 200 points (3x 3 = 300 and so forth) except for 3x 1 which is 1000
6x 2 = 2000 points (3x 3 = 300 and so forth) except for 6x 1 which is 10000

Phase 1:
In the first phase every player first needs to reach at least 1050 points or more, in order to reach the phase two

Phase 2:
In the second phase of the game every player can write down any points number if its at least 350 points.

Phase 3:
As soon as the first player hits 10050 points, every player coming after him still gets one try. So if your turn was
before the players who hit 10050, that is bad luck. This is also the reason why you always want to be the last person to
throw your dice. In the end the player wins who has the most points.


## Discalimer

This is not the final version of the game yet!

## Next Steps:

1. Add validation for point input. So to check wether or not the input is valid according to the rules
2. Check if the point input is an integer
3. Build a Web UI for easy usage

### Vision:

Create an App to use on Android and IOS
