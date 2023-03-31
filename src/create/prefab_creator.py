import pygame
import esper
from src.ecs.components.r_enemy_spawner import REnemySpawner
from src.ecs.components.r_surface import RSurface
from src.ecs.components.r_transform import RTransform
from src.ecs.components.r_velocity import RVelocity

def generar_enemigo(ecs_world:esper.World, rect_entity:int, size:pygame.Vector2, vel:pygame.Vector2, col:pygame.Color):
        ecs_world.add_component(rect_entity, 
                                     RSurface(size, col))
        ecs_world.add_component(rect_entity,
                                     RVelocity(vel))
        
def crear_enemigo(ecs_world:esper.World, timestamp:float, tipo:str, pos:pygame.Vector2):
        rect_entity = ecs_world.create_entity()
        ecs_world.add_component(rect_entity, 
                                REnemySpawner(timestamp, tipo))
        ecs_world.add_component(rect_entity, 
                                RTransform(pos))