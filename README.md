## Clone it
`git clone https://github.com/felipcode/ROSpy-LeaderFollower.git` 

## In the WorsSpace folder:
`cd ~catkin_ws`

 `source devel/setup.bash`


## To test it i opened 3 diferent terminals:
### One to run the .launch file ->
`cd ~catkin_ws`

 `roslaunch /src/follow_/src/launch/two_tb3.launch`

### Another to run leader-follower file ->
`cd ~catkin_ws`

`rosrun follow_ turtlebot3_teleop_key.py`

### And a third to run the teleop of leader robot ->
`cd ~catkin_ws`

`rosrun follow_ turtlebot3_teleop_key.py`
