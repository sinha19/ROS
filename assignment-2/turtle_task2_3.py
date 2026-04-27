import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA

class Turtle(Node):

    def __init__(self, name, id_seed):
        super().__init__(name)
        self.name = name
        self.id_seed = id_seed
        self.pub = self.create_publisher(MarkerArray, '/turtle_markers', 10)
        self.timer = self.create_timer(0.1, self.publish_turtle)

    def publish_turtle(self):
        ma = MarkerArray()
        now = self.get_clock().now().to_msg()
        frame = self.name  # 'turtle1' or 'turtle2'

        # --- FLOOR 1 (bottom, biggest) ---
        f1 = Marker()
        f1.header.frame_id = frame
        f1.header.stamp = now
        f1.ns = self.name
        f1.id = self.id_seed + 0
        f1.type = Marker.CYLINDER
        f1.action = Marker.ADD
        f1.pose.position.x = 0.0
        f1.pose.position.y = 0.0
        f1.pose.position.z = 0.04
        f1.scale.x = 0.38
        f1.scale.y = 0.28
        f1.scale.z = 0.04
        f1.color = ColorRGBA(r=0.0, g=0.6, b=0.2, a=1.0)

        # --- FLOOR 2 (middle) ---
        f2 = Marker()
        f2.header.frame_id = frame
        f2.header.stamp = now
        f2.ns = self.name
        f2.id = self.id_seed + 1
        f2.type = Marker.CYLINDER
        f2.action = Marker.ADD
        f2.pose.position.x = 0.0
        f2.pose.position.y = 0.0
        f2.pose.position.z = 0.18
        f2.scale.x = 0.30
        f2.scale.y = 0.22
        f2.scale.z = 0.04
        f2.color = ColorRGBA(r=0.0, g=0.55, b=0.18, a=1.0)

        # --- PILLAR front-right ---
        p1 = Marker()
        p1.header.frame_id = frame
        p1.header.stamp = now
        p1.ns = self.name
        p1.id = self.id_seed + 2
        p1.type = Marker.CYLINDER
        p1.action = Marker.ADD
        p1.pose.position.x =  0.10
        p1.pose.position.y =  0.07
        p1.pose.position.z =  0.11
        p1.scale.x = 0.04
        p1.scale.y = 0.04
        p1.scale.z = 0.14
        p1.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        # --- PILLAR front-left ---
        p2 = Marker()
        p2.header.frame_id = frame
        p2.header.stamp = now
        p2.ns = self.name
        p2.id = self.id_seed + 3
        p2.type = Marker.CYLINDER
        p2.action = Marker.ADD
        p2.pose.position.x = -0.10
        p2.pose.position.y =  0.07
        p2.pose.position.z =  0.11
        p2.scale.x = 0.04
        p2.scale.y = 0.04
        p2.scale.z = 0.14
        p2.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        # --- PILLAR rear-right ---
        p3 = Marker()
        p3.header.frame_id = frame
        p3.header.stamp = now
        p3.ns = self.name
        p3.id = self.id_seed + 4
        p3.type = Marker.CYLINDER
        p3.action = Marker.ADD
        p3.pose.position.x =  0.10
        p3.pose.position.y = -0.07
        p3.pose.position.z =  0.11
        p3.scale.x = 0.04
        p3.scale.y = 0.04
        p3.scale.z = 0.14
        p3.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        # --- PILLAR rear-left ---
        p4 = Marker()
        p4.header.frame_id = frame
        p4.header.stamp = now
        p4.ns = self.name
        p4.id = self.id_seed + 5
        p4.type = Marker.CYLINDER
        p4.action = Marker.ADD
        p4.pose.position.x = -0.10
        p4.pose.position.y = -0.07
        p4.pose.position.z =  0.11
        p4.scale.x = 0.04
        p4.scale.y = 0.04
        p4.scale.z = 0.14
        p4.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        # --- WHEEL front-right ---
        w1 = Marker()
        w1.header.frame_id = frame
        w1.header.stamp = now
        w1.ns = self.name
        w1.id = self.id_seed + 6
        w1.type = Marker.CYLINDER
        w1.action = Marker.ADD
        w1.pose.position.x =  0.14
        w1.pose.position.y =  0.15
        w1.pose.position.z =  0.04
        w1.pose.orientation.x = 1.0
        w1.pose.orientation.y = 0.0
        w1.pose.orientation.z = 0.0
        w1.pose.orientation.w = 0.0
        w1.scale.x = 0.10
        w1.scale.y = 0.10
        w1.scale.z = 0.05
        w1.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        # --- WHEEL front-left ---
        w2 = Marker()
        w2.header.frame_id = frame
        w2.header.stamp = now
        w2.ns = self.name
        w2.id = self.id_seed + 7
        w2.type = Marker.CYLINDER
        w2.action = Marker.ADD
        w2.pose.position.x = -0.14
        w2.pose.position.y =  0.15
        w2.pose.position.z =  0.04
        w2.pose.orientation.x = 1.0
        w2.pose.orientation.y = 0.0
        w2.pose.orientation.z = 0.0
        w2.pose.orientation.w = 0.0
        w2.scale.x = 0.10
        w2.scale.y = 0.10
        w2.scale.z = 0.05
        w2.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        # --- WHEEL rear-right ---
        w3 = Marker()
        w3.header.frame_id = frame
        w3.header.stamp = now
        w3.ns = self.name
        w3.id = self.id_seed + 8
        w3.type = Marker.CYLINDER
        w3.action = Marker.ADD
        w3.pose.position.x =  0.14
        w3.pose.position.y = -0.15
        w3.pose.position.z =  0.04
        w3.pose.orientation.x = 1.0
        w3.pose.orientation.y = 0.0
        w3.pose.orientation.z = 0.0
        w3.pose.orientation.w = 0.0
        w3.scale.x = 0.10
        w3.scale.y = 0.10
        w3.scale.z = 0.05
        w3.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        # --- WHEEL rear-left ---
        w4 = Marker()
        w4.header.frame_id = frame
        w4.header.stamp = now
        w4.ns = self.name
        w4.id = self.id_seed + 9
        w4.type = Marker.CYLINDER
        w4.action = Marker.ADD
        w4.pose.position.x = -0.14
        w4.pose.position.y = -0.15
        w4.pose.position.z =  0.04
        w4.pose.orientation.x = 1.0
        w4.pose.orientation.y = 0.0
        w4.pose.orientation.z = 0.0
        w4.pose.orientation.w = 0.0
        w4.scale.x = 0.10
        w4.scale.y = 0.10
        w4.scale.z = 0.05
        w4.color = ColorRGBA(r=0.3, g=0.3, b=0.3, a=1.0)

        ma.markers = [f1, f2, p1, p2, p3, p4, w1, w2, w3, w4]
        self.pub.publish(ma)


def main():
    rclpy.init()

    turtle1 = Turtle("turtle1", 100)
    turtle2 = Turtle("turtle2", 200)

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(turtle1)
    executor.add_node(turtle2)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__ == '__main__':
    main()
