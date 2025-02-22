import rclpy
import time
import numpy as np
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity, DeleteEntity

class MovingObject(Node):
    def __init__(self):
        super().__init__('moving_object_client')
        
        # Create clients for spawning and deleting entities
        self.spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        self.delete_client = self.create_client(DeleteEntity, '/delete_entity')

        # Wait for services
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn_entity service...')
        while not self.delete_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /delete_entity service...')

        # Define waypoints
        waypoints1 = [(x, 3.5, 0.5) for x in np.linspace(1, 8, 8)]
        waypoints2 = [(x, 3.5, 0.5) for x in np.linspace(8, 1, 8)]
        # waypoints1 = [(x, 2, 0.5) for x in np.linspace(-2, 3, 5)]
        # waypoints2 = [(x, 2, 0.5) for x in np.linspace(2, 3, 5)]
        self.waypoints = waypoints1 + waypoints2

        
        # Start movement
        self.move_object()

    def spawn_object(self, x, y, z):
        """ Spawn a dynamic object at given coordinates """
        request = SpawnEntity.Request()
        request.name = "my_box"
        request.xml = """<sdf version='1.6'>
                          <model name='box'>
                            <link name='link'>
                                <inertial>
                                <mass>1</mass>
                                <inertia>
                                    <ixx>0.166667</ixx>
                                    <ixy>0</ixy>
                                    <ixz>0</ixz>
                                    <iyy>0.166667</iyy>
                                    <iyz>0</iyz>
                                    <izz>0.166667</izz>
                                </inertia>
                                <pose>0 0 0 0 -0 0</pose>
                                </inertial>
                                <collision name='collision'>
                                <geometry>
                                    <box>
                                    <size>1 1 1</size>
                                    </box>
                                </geometry>
                                <max_contacts>10</max_contacts>
                                <surface>
                                    <contact>
                                    <ode/>
                                    </contact>
                                    <bounce/>
                                    <friction>
                                    <torsional>
                                        <ode/>
                                    </torsional>
                                    <ode/>
                                    </friction>
                                </surface>
                                </collision>
                                <visual name='visual'>
                                <geometry>
                                    <box>
                                    <size>1 1 1</size>
                                    </box>
                                </geometry>
                                <material>
                                    <script>
                                    <name>Gazebo/Grey</name>
                                    <uri>file://media/materials/scripts/gazebo.material</uri>
                                    </script>
                                </material>
                                </visual>
                                <self_collide>0</self_collide>
                                <enable_wind>0</enable_wind>
                                <kinematic>0</kinematic>
                            </link>
                            </model>
                        </sdf>"""
        request.robot_namespace = ""
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = z

        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result():
            self.get_logger().info(f"Spawned object at ({x}, {y}, {z})")
        else:
            self.get_logger().error("Failed to spawn object")

    def delete_object(self):
        """ Delete the object from the simulation """
        request = DeleteEntity.Request()
        request.name = "my_box"
        future = self.delete_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result():
            self.get_logger().info("Deleted object")
        else:
            self.get_logger().error("Failed to delete object")

    def move_object(self):
        """ Move the object across defined waypoints """
        
        while rclpy.ok():
            for x, y, z in self.waypoints:
                self.spawn_object(float(x), y, z)
                time.sleep(5)  # Pause for visibility
                self.delete_object()

def main():
    rclpy.init()
    moving_object = MovingObject()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

