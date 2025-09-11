from flask import Flask, render_template_string
import random
import math

app = Flask(__name__)

# === Driver, Rider, and Dispatch Logic ===

class Driver:
    def __init__(self, driver_id, location):
        self.id = driver_id
        self.location = location
        self.available = True

    def assign_rider(self, rider):
        self.available = False
        self.location = rider.destination
        return f"Driver {self.id} assigned to Rider {rider.id} from {rider.origin} to {rider.destination}"


class Rider:
    def __init__(self, rider_id, origin, destination):
        self.id = rider_id
        self.origin = origin
        self.destination = destination


class DispatchSystem:
    def __init__(self, drivers):
        self.drivers = drivers

    def dispatch(self, rider):
        available_drivers = [d for d in self.drivers if d.available]
        if not available_drivers:
            return f"No available drivers for Rider {rider.id}"
        
        # Find nearest driver
        nearest_driver = min(available_drivers, key=lambda d: self.distance(d.location, rider.origin))
        return nearest_driver.assign_rider(rider)

    @staticmethod
    def distance(loc1, loc2):
        return math.hypot(loc1[0] - loc2[0], loc1[1] - loc2[1])


# === Flask Route ===

@app.route('/')
def simulate_dispatch():
    # Create 5 drivers
    drivers = [Driver(i, (random.randint(0, 20), random.randint(0, 20))) for i in range(5)]

    # Create a rider
