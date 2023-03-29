import esper
import pygame
from src.ecs.components.r_surface import RSurface
from src.ecs.components.r_transform import RTransform

def system_rendering(world:esper.World, screen:pygame.Surface):
    components = world.get_components(RTransform, RSurface)
    
    r_t:RTransform
    r_s:RSurface
    for entity, (r_t, r_s) in components:
        screen.blit(r_s.surf, r_t.pos)