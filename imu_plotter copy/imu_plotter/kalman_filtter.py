import rclpy
from rclpy.node import Node
from  myimu.msg import Calculation, ImuSensor


class Kalmanfiltter(Node):
    def __init__(self):
        super().__init__('kalman_filtter')
        self.imu_sub = self.create_subscription(Calculation, '/calculation/accel', self.imu_callback, 10)
        self.kalman_pub = self.create_publisher(Calculation, '/calculation/final', 10)

    def imu_callback(self, accel_msg):
        kalman_msg = Calculation()
        kalman_msg.final.roll = accel_msg.accel.roll
        kalman_msg.final.pitch = accel_msg.accel.pitch
        kalman_msg.final.yaw = accel_msg.accel.yaw

        self.kalman_pub.publish(kalman_msg)  # ✅ 올바른 변수명 사용

def main():
    rclpy.init()
    node = Kalmanfiltter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
