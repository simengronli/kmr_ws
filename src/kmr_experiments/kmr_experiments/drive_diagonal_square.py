import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


VELOCITY = 0.5

class DriveDiagonalSquare(Node):

    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 10  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0
        msg.linear.z = 0.0

        if self.i%5 == 0:
            msg.linear.x = VELOCITY
            msg.linear.y = VELOCITY
        if self.i%5 == 1:
            msg.linear.x = -VELOCITY
            msg.linear.y = VELOCITY
        if self.i%5 == 2:
            msg.linear.x = -VELOCITY
            msg.linear.y = -VELOCITY
        if self.i%5 == 3:
            msg.linear.x = VELOCITY
            msg.linear.y = -VELOCITY
        if self.i%5 == 4:
            msg.linear.x = 0.0
            msg.linear.y = 0.0

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg}')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    cmd_vel_publisher = DriveDiagonalSquare()

    rclpy.spin(cmd_vel_publisher)

    cmd_vel_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()