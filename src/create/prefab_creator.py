import pygame
import esper
from src.ecs.components.r_surface import RSurface
from src.ecs.components.r_transform import RTransform
from src.ecs.components.r_velocity import RVelocity

def crear_rectangulo(ecs_world:esper.World, size:pygame.Vector2, pos:pygame.Vector2, vel:pygame.Vector2, col:pygame.Color):
        rect_entity = ecs_world.create_entity()
        ecs_world.add_component(rect_entity, 
                                     RSurface(size, col))
        ecs_world.add_component(rect_entity, 
                                     RTransform(pos))
        ecs_world.add_component(rect_entity,
                                     RVelocity(vel))