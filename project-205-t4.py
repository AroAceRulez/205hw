import glob
import os
import sys
import argparse
import random
import time
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
actor_list=[]
def main(arg):
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)
    world = client.get_world()

    try:

        get_blueprint_of_world = world.get_blueprint_library()
        car_model = get_blueprint_of_world.filter('model3')[0]
        spawn_point = random.choice(world.get_map(),get_spawn_points())
        dropped_vehicle = world.spawn_actor(car_model, spawn_point)

        

        vehicle = world.spawn_actor(vehicle_bp, vehicle_transform)
        vehicle.set_autopilot(True)

        spectator_transform = carla.Transform(vehicle_transform.location, vehicle_transform.rotation)
        spectator_transform.location += vehicle_transform.get_forward_vector() * 20
        spectator_transform.rotation.yaw += 180
        spectator = world.get_spectator()
        spectator.set_transform(spectator_transform)
        vehicle.set_transform(vehicle_transform)
        actor_list.append(dropped_vehicle)

        time.sleep(1000)


    finally:
        print('destroying actors')
        for actor in actor_list:
            actor.destroy()
        print('done.')


