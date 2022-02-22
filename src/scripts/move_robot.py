#! /usr/bin/env python


""" TODO:
-   Write a node that subscribes to the laser topic data and publishes into the topic `/robot/cmd_vel`.

-   Start by publishing a linear velocity of 0.1 m/s to the robot.

-   When the laser detects an obstacle 30 cm in front of the robot, stop it and turn 90 degrees to the right.

-   Publish a linear velocity of 0.1 m/s until the robot reaches the next obstacle (table), and then stop it (inside the loading cart).

-   Create a launch file named **goto_loading_pos.launch** that starts your program. """