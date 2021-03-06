import wpilib

from Devices.General import Potentiometer, LimitSwitch
from Devices.Joysticks.Logitech.Attack3 import LogitechAttack3
from Devices.Maxbotix.MB10x0 import MB10x0_Digital
from Devices.RevRobotics.AnalogPressureSensor import AnalogPressureSensor
from Devices.GarnetSquadron.GarnetControls import GarnetControls
from Subsystems.subsystem_Arm import Arm
from Subsystems.subsystem_DriveBase import DriveBase
from Subsystems.subsystem_DriverStation import DriverStation
from Subsystems.subsystem_EndEffector import EndEffector
from Subsystems.subsystem_Pneumatics import Pneumatics


class InitRobot:
    def __init__(self):
        self.devices = Devices()
        self.subsystems = Subsystems(self.devices)


class Devices:
    """
    This class initializes the hardware devices on the robot.
    """
    def __init__(self):
        self.motors = self.InitMotors()
        self.sensors = self.InitSensors()
        self.pneumatics = self.InitPneumatics()
        self.driver_station = self.InitDriverStation()

    class InitMotors:
        def __init__(self):
            # PWM Outputs
            self.left_drive = wpilib.Spark(channel=0)
            self.right_drive = wpilib.Spark(channel=1)
            self.grip = wpilib.VictorSP(channel=2)

            # CAN Outputs
            self.arm = wpilib.CANTalon(deviceNumber=2)

    class InitSensors:
        def __init__(self):
            # Digital Inputs
            self.left_drive_encoder = wpilib.Encoder(aChannel=0, bChannel=1)
            self.right_drive_encoder = wpilib.Encoder(aChannel=2, bChannel=3)
            self.lock_disengaged_switch = LimitSwitch(channel=4)
            self.ultrasonic_distance = MB10x0_Digital(channel=5)

            # Analog Inputs
            self.pressure_sensor = AnalogPressureSensor(channel=0)
            self.arm_angle_sensor = Potentiometer(channel=1)

            # XDP sensor
            # self.imu = ADIS16488() - TODO: Finish implementing this class

    class InitPneumatics:
        def __init__(self):
          pass

    class InitDriverStation:
        def __init__(self):
            self.left_joystick = LogitechAttack3(0)
            self.right_joystick = LogitechAttack3(1)
            self.control_board = GarnetControls()


class Subsystems:
    def __init__(self, devices):
        """

        :param devices: Devices
        """

        self.arm = Arm()
        self.drive_base = DriveBase()
        self.driver_station = DriverStation()
        self.end_effector = EndEffector()
        self.pneumatics = Pneumatics()

        self.arm.setRunWhenDisabled(True)
        self.drive_base.setRunWhenDisabled(True)
        self.driver_station.setRunWhenDisabled(True)
        self.end_effector.setRunWhenDisabled(True)
        self.pneumatics.setRunWhenDisabled(True)

        self.arm.start(devices)
        self.drive_base.start(devices)
        self.driver_station.start(devices)
        self.end_effector.start(devices)
        self.pneumatics.start(devices)
