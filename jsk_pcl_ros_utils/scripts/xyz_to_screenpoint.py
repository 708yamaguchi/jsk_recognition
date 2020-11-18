#!/usr/bin/env python

import rospy

from sensor_msgs.msg import CameraInfo
from geometry_msgs.msg import PointStamped

from image_geometry import PinholeCameraModel

class XYZToScreenPoint(object):
    def __init__(self):
        self.cameramodels = PinholeCameraModel()
        self.is_camera_arrived = False
        self.header = None

        # publish info
        self.pub = rospy.Publisher("~output", PointStamped, queue_size=1)

        rospy.Subscriber('~input/camera_info', CameraInfo, self.camera_info_cb)
        rospy.Subscriber('~input', PointStamped, self.point_stamped_cb)

    def camera_info_cb(self, msg):
        self.cameramodels.fromCameraInfo(msg)
        self.is_camera_arrived = True
        self.frame_id = msg.header.frame_id

    def point_stamped_cb(self, msg):
        if not self.is_camera_arrived:
            return
        point = (msg.point.x, msg.point.y, msg.point.z)
        u, v = self.cameramodels.project3dToPixel(point)
        rospy.logdebug("u, v : {}, {}".format(u, v))
        pub_msg = PointStamped()
        pub_msg.header = self.header
        pub_msg.point.x = u
        pub_msg.point.y = v
        pub_msg.point.z = 0
        self.pub.publish(pub_msg)

    # def subscribeCameraInfo(self):
        

if __name__ == '__main__':
    rospy.init_node("xyz_to_screenpoint")
    xyz_to_screenpoint = XYZToScreenPoint()
    # xyz_to_screenpoint.subscribeCameraInfo()
    rospy.spin()
