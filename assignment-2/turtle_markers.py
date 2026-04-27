import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point
import math

class TurtleMarker(Node):
    def __init__(self):
        super().__init__('turtle_marker')
        self.pub = self.create_publisher(MarkerArray, '/turtle_markers', 10)
        self.timer = self.create_timer(0.1, self.publish_markers)

    def publish_markers(self):
        ma = MarkerArray()
        now = self.get_clock().now().to_msg()

        # --- SHELL LAYER 1 (bottom, biggest) ---
        s1 = Marker()
        s1.header.frame_id = 'turtle1'
        s1.header.stamp = now
        s1.ns = 'turtle'
        s1.id = 0
        s1.type = Marker.CYLINDER
        s1.action = Marker.ADD
        s1.pose.position.x = 0.0
        s1.pose.position.y = 0.0
        s1.pose.position.z = 0.02
        s1.scale.x = 0.40
        s1.scale.y = 0.28
        s1.scale.z = 0.03
        s1.color = ColorRGBA(r=0.0, g=0.6, b=0.2, a=1.0)

        # --- SHELL LAYER 2 ---
        s2 = Marker()
        s2.header.frame_id = 'turtle1'
        s2.header.stamp = now
        s2.ns = 'turtle'
        s2.id = 1
        s2.type = Marker.CYLINDER
        s2.action = Marker.ADD
        s2.pose.position.x = 0.0
        s2.pose.position.y = 0.0
        s2.pose.position.z = 0.07
        s2.scale.x = 0.32
        s2.scale.y = 0.22
        s2.scale.z = 0.03
        s2.color = ColorRGBA(r=0.0, g=0.55, b=0.18, a=1.0)

        # --- SHELL LAYER 3 ---
        s3 = Marker()
        s3.header.frame_id = 'turtle1'
        s3.header.stamp = now
        s3.ns = 'turtle'
        s3.id = 2
        s3.type = Marker.CYLINDER
        s3.action = Marker.ADD
        s3.pose.position.x = 0.0
        s3.pose.position.y = 0.0
        s3.pose.position.z = 0.12
        s3.scale.x = 0.22
        s3.scale.y = 0.15
        s3.scale.z = 0.03
        s3.color = ColorRGBA(r=0.0, g=0.50, b=0.15, a=1.0)

        # --- SHELL LAYER 4 (top, smallest) ---
        s4 = Marker()
        s4.header.frame_id = 'turtle1'
        s4.header.stamp = now
        s4.ns = 'turtle'
        s4.id = 3
        s4.type = Marker.SPHERE
        s4.action = Marker.ADD
        s4.pose.position.x = 0.0
        s4.pose.position.y = 0.0
        s4.pose.position.z = 0.17
        s4.scale.x = 0.14
        s4.scale.y = 0.10
        s4.scale.z = 0.06
        s4.color = ColorRGBA(r=0.0, g=0.45, b=0.12, a=1.0)

        ma.markers = [s1, s2, s3, s4]
        self.pub.publish(ma)

def main():
    rclpy.init()
    node = TurtleMarker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
