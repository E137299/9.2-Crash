# 9.2-Crash

## Objective:
For this assignment, you will program a game in which the player steers a car that must avoid oncoming traffic.

## Part One - Car Class:
![Cars](images/crash.png)

You will create a Car class, representing the vehicles that the player must avoid in the game. The Car class must include:

1. **Constructor**: The constructor method will initialize each car object. It will assign a car body to the object and determine its initial location with random x and y coordinates. All car objects must appear above the screen out of view of the player.

2. **Drive Method**: This method will be responsible for moving the car object down by ten pixels every time it is called. 

3. **Relocate Method**: When a car drops below the bottom of the screen, the relocate method will be invoked. This function will teleport the car object above the screen to a new random location (x, y coordinates) and assign it a new car body.

Once implemented, cars will continuously loop through the drive and relocate actions, simulating movement and providing a challenge for the player to avoid collisions.

## Part Two - Player Class:
You will create a Player class which must include:
1. **Constructor**: The constructor method initializes a player's car at the bottom of the window and assigns a car body to the player. Additionally, it binds the move_left() and move_right() methods to keys, enabling the player object to move left when one key is pressed and move right when another key is pressed. The constructor should initialize a instance variable, *alive*, to True
2. **move_left()**: This method will move the player left as long as the player is on the road.
3. **move_right()**: This method will move the player right as long as the player is on the road.

## Part Three - Collision:
Utilize the turtle method, .distance(), to determine whether the player object has collided with any of the car objects. If a collision is detected, the player's instance variable, *alive*, should be set to False, consequently halting the while loop and effectively terminating the game.
