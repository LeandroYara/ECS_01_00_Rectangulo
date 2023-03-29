import pygame
import esper
from src.ecs.components.r_transform import RTransform
from src.ecs.components.r_velocity import RVelocity

def system_movement(world: esper.World, delta_time:float):
    
    components = world.get_components(RTransform, RVelocity)
    
    r_t:RTransform
    r_v:RVelocity
    for entity, (r_t, r_v) in components:
        r_t.pos.x += r_v.vel.x * delta_time
        r_t.pos.y += r_v.vel.y * delta_time