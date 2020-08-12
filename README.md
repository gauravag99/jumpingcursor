# Jumpingcursor
This is a simulator for the twitter post [here](https://twitter.com/Arnaldo_AGITF/status/1292527434353577985?s=20)

The twitter post basically wants us to calculate the average steps taken by the jumping dot to reach 6, given initial starting position  as 1.
![](https://github.com/sciencyboi/jumpingcursor/blob/master/vid.gif)

The code simulates 100000 iterations, and an average of 19 is reached around 60000 iterations.
The probabilities (serving the  purpose of gates) are hard coded, and similarly the structure of possible jumps is also hardcodeed in two dictionaries.
YOu can change these (essentially changing the structure of the above image), the iterations, can use multiprocessing to make it faster, since each cursor can be treated as a different object.


