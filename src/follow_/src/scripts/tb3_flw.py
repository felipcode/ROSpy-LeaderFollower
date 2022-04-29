import rospy
import numpy as np
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion as qt2e

class rob:
    def __init__(self, name):
        self.name = name
        self.max_lin = 0.22
        self.max_ang = 2.84
        self.pose = Pose()
        self.cmd_vel = Twist()
        self.rate = rospy.Rate(1)
        self.pub = rospy.Publisher(self.name + "/cmd_vel", Twist, queue_size=1)
        rospy.Subscriber(self.name + "/odom", Odometry, self.track)   
        
    def track(self, msg):
        orientation = msg.pose.pose.orientation
        (_, _, yaw) = qt2e([orientation.x, orientation.y, orientation.z, orientation.w])
        self.pose.x = msg.pose.pose.position.x
        self.pose.y = msg.pose.pose.position.y
        self.pose.theta =  yaw
    
    # se movimenta conforme o comando
    def move(self, msg):
        self.cmd_vel = msg
        self.pub.publish(self.cmd_vel)
    # fica em standby
    def run(self):
        rospy.spin()


class leader_flwr:
    def __init__(self, leader, follower):
        rospy.init_node("ldr_flwr", anonymous=False)
        self.folwr = rob(follower)
        self.leader = rob(leader)
        self.machinist = rospy.Rate(10)
        self.min_radius = 0.5
        rospy.Subscriber("/cmd_vel", Twist, self.teleop)

    # intercepta o comando de teleop e move o líder
    def teleop(self, msg):
        self.leader.move(msg)
    # obtém o vetor de posição do vagão em relação ao líder
    def relPos(self, leader, follower):
        ref = leader.pose
        flw = follower.pose
        module = np.sqrt((ref.x - flw.x)**2 + (ref.y - flw.y)**2)
        angle = np.arctan2(ref.y - flw.y,  ref.x - flw.x) - flw.theta
        return (module, angle)
    
    # ação de controle baseada no vetor de posição relativa
    def control(self, rel_pos, kp=(1.5, 6)):
        ctrl_vel = Twist()
        stop = (rel_pos[0] > self.min_radius)
        # ação de controle linear
        ctrl_vel.linear.x  = kp[0] * rel_pos[0] * stop
        ctrl_vel.linear.y = 0
        ctrl_vel.linear.z = 0
        # ação de controle angular
        ctrl_vel.angular.z = kp[1] * rel_pos[1] * stop
        ctrl_vel.angular.x = 0
        ctrl_vel.angular.y = 0

        #SATURACAO
        # velocidade linear máxima
        if abs(ctrl_vel.linear.x) > self.folwr.max_lin:
            ctrl_vel.linear.x = self.folwr.max_lin * np.sign(ctrl_vel.linear.x)
        # velocidade angular máxima
        if abs(ctrl_vel.angular.z) > self.folwr.max_ang:
            ctrl_vel.angular.z = self.folwr.max_ang * np.sign(ctrl_vel.angular.z)
        return ctrl_vel

    def run(self):
        while not rospy.is_shutdown():
            (d, ang) = self.relPos(self.leader, self.folwr)

            cmd = self.control((d, ang))
            self.folwr.move(cmd)
        
        self.machinist.sleep()


if __name__ == "__main__":
    try:
        maluk = leader_flwr('tb3_0', 'tb3_1')
        maluk.run()

    except rospy.ROSInterruptException:
        pass