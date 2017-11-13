
"""projectile.py
Provides a simple class for modeling the 
flight of projectiles."""

import math

class Projectile:
    
    """Simulates the flight of simple projectiles near the earth's 
    surface, ignoring wind resistance. Tracking is done in two 
    dimensions, height (y) and distance (x)."""
    
    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity, and height"""
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)
        
    def getX(self):
        "Returns the x position (distance) of this projectile"
        return self.xpos
    
    def getY(self):
        "Returns the y position (height) of this projectile"
        return self.ypos
    
    def update(self, time):
        """Update the state of this projectile to move it time seconds 
        farther into its flight."""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2
        self.yvel = yvel1

def getCballInputs():
    """Get inputs for simulation interactively from user: 
    angle, velocity, initial height, time-step"""
    angle = float(input("Enter the launch angle (in degreeds): "))
    velocity = float(input("Enter the initial velocity (in meters per second): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    return angle, velocity, h0, time

        
def main():
    """Run interactive projectile simulation with a single projectile"""
    angle, vel, h0, time = getCballInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("Distance traveled: {0:0.1f} meters.".format(cball.getX()))
    
if __name__ == "__main__":
    main()