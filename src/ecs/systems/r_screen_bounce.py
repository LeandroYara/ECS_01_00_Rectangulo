import pygame
import esper
from src.ecs.components.r_surface import RSurface
from src.ecs.components.r_transform import RTransform
from src.ecs.components.r_velocity import RVelocity


def system_screen_bounce(world:esper.World, screen:pygame.Surface):
    
    screen_rect = screen.get_rect()
    components = world.get_components(RTransform, RVelocity, RSurface)
    
    r_t:RTransform
    r_v:RVelocity
    r_s:RSurface
    for entity, (r_t, r_v, r_s) in components:
        cuad_rect = r_s.surf.get_rect(topleft=r_t.pos)
        
        if cuad_rect.left <= 0 or cuad_rect.right >= screen_rect.width:
            r_v.vel.x *= -1
            cuad_rect.clamp_ip(screen_rect)
            r_t.pos.x = cuad_rect.x
        if cuad_rect.top <= 0 or cuad_rect.bottom >= screen_rect.height:
            r_v.vel.y *= -1
            cuad_rect.clamp_ip(screen_rect)
            r_t.pos.y = cuad_rect.y