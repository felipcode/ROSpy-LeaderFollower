#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/src/turtlebot3/turtlebot3_example"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/install/lib/python3/dist-packages:/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/build" \
    "/usr/bin/python3" \
    "/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/src/turtlebot3/turtlebot3_example/setup.py" \
     \
    build --build-base "/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/build/turtlebot3/turtlebot3_example" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/install" --install-scripts="/home/lip/robotics/ROS/atividades/desafio1/follow_me_ws/install/bin"
