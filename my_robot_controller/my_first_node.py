#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Node class
class MyNode(Node):

    def __init__(self):
        # Name of the node -> initialise node
        super().__init__("first_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    
    # Install ROS2 communication
    rclpy.init(args=args)

    # Create node out of the MyNode calss
    node = MyNode()

    # Make the node to run continuously until it is stopped
    rclpy.spin(node)

    # Shutdown ROS2 communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()
