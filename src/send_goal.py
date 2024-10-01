#!/usr/bin/python3

import rospy
from geometry_msgs.msg import PoseStamped

class GoalSender(object):

    def __init__(self):
        self.goal_pub_ = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        self.points_ = rospy.get_param('/locations')

    def send_goal(self, name):
        if name in self.points_:
            x,y,z = self.points_[name]

            pose = PoseStamped()
            pose.header.frame_id = "map"
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.position.z = z
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = 0.0
            pose.pose.orientation.w = 1.0

            self.goal_pub_.publish(pose)
            rospy.loginfo("Sent  goal command for %s", name)

        else:
            rospy.logerr("Location not found")


def main():
    rospy.init_node('goal_sender')

    goal_sender = GoalSender()
    goal_location = input("Enter goal location:" )
    goal_sender.send_goal(goal_location)

if __name__ == "__main__":
    main()