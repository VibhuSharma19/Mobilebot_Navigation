#!/usr/bin/python3

import rospy
from visualization_msgs.msg import Marker

class MarkerPublisher(object):

    def __init__(self):
        self.marker_pub_ = rospy.Publisher('/visualization_marker',Marker,queue_size=10)

        self.points_ = {
            'CenterTable':(0.0, 0.0, 0.0),
            'SofaLeft':(-3.53, 0.667, 0.0),
            'SofaRight':(-3.55, -0.966, 0.0),
            'Lamp':(-4.39, -3.45, 0.0),
            'CoffeeTable': (-3.7, 3.5, 0.0),
            'Door': (0.0, 4.1, 0.0),
            'Dustbin': (4.06, 4.3, 0.0),
            'BookShelf':(3.96, -4.03, 0.0),
            'BlackShelf_1':(3.87, 0.54, 0.0),
            'BlackShelf_2': (0.68, -3.71, 0.0),
            'Desk_1': (1.5, 3.7, 0.0),
            'Desk_2': (3.8, 3.0, 0.0),
            'Desk_3': (3.75, -0.98, 0.0),
            'Desk_4': (2.94, -3.71, 0.0),
            'Desk_5': (-1.07, -3.71, 0.0),
        }

        rospy.set_param('/locations', self.points_)

    def publish_markers(self):
        mId = 0
        for name, (x,y,z) in self.points_.items():
            marker = Marker()
            marker.header.frame_id = "map"
            marker.ns = "locations"
            marker.id = mId
            marker.type = Marker.TEXT_VIEW_FACING
            marker.action = Marker.ADD
            marker.pose.position.x = x
            marker.pose.position.y = y
            marker.pose.position.z = z
            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0
            marker.text = name
            marker.scale.x = 0.3
            marker.scale.y = 0.3
            marker.scale.z = 0.3
            marker.color.r = 0.0
            marker.color.g = 0.0
            marker.color.b = 1.0
            marker.color.a = 1.0

            self.marker_pub_.publish(marker)
            mId +=1

def main():
    rospy.init_node('Marker_Publisher')
    rate = rospy.Rate(10)

    marker_pub = MarkerPublisher()
    while not rospy.is_shutdown():
        marker_pub.publish_markers()
        rate.sleep()


if __name__ == '__main__':
    main()