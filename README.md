## Clone it 😎
`$ git clone https://github.com/felipcode/ROSpy-LeaderFollower.git` 

## In the WorkSpace folder:
`$ cd ~catkin_ws`

 `$ source devel/setup.bash`
 
### Build project
 
 `$ catkin_make`


## To test it i opened 3 diferent terminals:
### One to run the .launch file ->
`$ cd ~catkin_ws`

`$ roslaunch /src/follow_/src/launch/two_tb3.launch`

### Another to run leader-follower file ->
`$ cd ~catkin_ws`

`$ rosrun follow_ turtlebot3_teleop_key.py`

### And a third to run the teleop of leader robot ->
`$ cd ~catkin_ws`

`$ rosrun follow_ turtlebot3_teleop_key.py`


## After the teleop file is running this should happen
![brave_Ze6L2SXyBH](https://user-images.githubusercontent.com/42594579/166072254-384654ec-189e-4fe0-81f2-402173851bfd.gif)



Inspired by the work of: https://github.com/lcaldeira/Rosject2_Turtlebot
