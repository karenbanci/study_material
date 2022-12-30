"""
1. Setting Up Our Robot
Let’s begin by creating the class for our robot. We will begin by setting up the instance variables to keep track of important data related to the robot. Here are the steps we need to do:

Create a new class called DriveBot
Set up a basic constructor (no parameters needed)
Initialize three instance variables within our constructor which all default to 0: motor_speed, direction, and sensor_range
"""

class DriveBot:
  def __init__(self):
    self.motor_speed = 0
    self.direction = 0
    self.sensor_range = 0

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

"""
2. Adding Methods
Now we want to add some logic to our robot. It would be very useful to be able to control our robot, so we are going to create a control_bot method which changes the speed and direction. We are also going to create a method called adjust_sensor. This method is used to change the range of our robot’s sensors which are used to detect obstacles. Here are the steps:

Define a function within the DriveBot class which accepts two additional parameters: one for a new speed and one for a new direction
Replace the instance variables for speed and direction with the input parameters
Define another function called adjust_sensor which accepts one additional parameter
Replace the instance variable sensor_range with the input parameter
"""
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

"""
3. Enhanced Constructor
It can be tedious manually setting the values for each instance variable after we have created an object from the DriveBot class. We can enhance our constructor to automatically assign the values we provide to the instance variables. Instead of taking zero parameters, we are going to make the constructor take three parameters. Here is what we need to do:

Modify the constructor to take three parameters (in addition to self): one for motor_speed, one for direction, and one for sensor_range
For the first parameter, make the default value 0
For the second parameter, make the default value 180
For the third parameter, make the default value 10
Within the constructor, replace the instance variables with the variables from the input parameters
"""
class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed = 0, direction = 180,sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

"""
4. Controlling Them All
We want to add a new feature which allows the use to control multiple robots at once. The robots should be able to all have the same latitude and longitude GPS destination coordinates as well as a setting for disabling them all called all_disabled. We can accomplish this using class variables. Here is how we can do it:

Create a new class variable within the DriveBot class called all_disabled and set it equal to False
Create a new class variable within the DriveBot class called latitude and set it equal to -999999
Create a new class variable within the DriveBot class called longitude and set it equal to -999999
Outside of the class, test the class variables by setting the longitude of all robots to 50.0, the latitude to -50.0 and all_disabled to True
"""
class DriveBot:
  # Create the class variables!
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!

DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

"""
5. Identifying Robots
In order to keep track of the robots we are creating, we want to be able to assign an ID value to each robot when it is created. If we create five robots in a row, we want the IDs of each robot to be 1, 2, 3, 4, and 5 respectively. This can be accomplished by using a class variable counter which increments and is assigned to an instance variable for the ID whenever the constructor is called. Here are the steps:

Create a new class variable in the DriveBot class called robot_count
In the constructor, increment the robot_count by 1
After incrementing the value, assign the value of robot_count to a new instance variable called id.
"""
class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)


