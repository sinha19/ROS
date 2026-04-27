import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

class ArrowMarkerPublisher(Node):
    def __init__(self):
        super().__init__('arrow_marker_publisher')
        self.publisher_ = self.create_publisher(Marker, 'visualization_marker', 10)
        self.timer = self.create_timer(0.1, self.publish_marker)

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = 'turtle1'
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = 'arrow'
        marker.id = 0
        marker.type = Marker.ARROW
        marker.action = Marker.ADD

        start = Point()
        start.x = 0.0
        start.y = 0.0
        start.z = 0.0

        end = Point()
        end.x = 1.0
        end.y = 0.0
        end.z = 0.0

        marker.points = [start, end]
        marker.scale.x = 0.1
        marker.scale.y = 0.2
        marker.scale.z = 0.2

        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        self.publisher_.publish(marker)

def main(args=None):
    rclpy.init(args=args)
    node = ArrowMarkerPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

