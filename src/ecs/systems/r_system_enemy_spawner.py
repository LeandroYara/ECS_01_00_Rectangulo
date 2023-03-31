import json
import pygame
import esper
import random
from src.create.prefab_creator import generar_enemigo
from src.ecs.components.r_enemy_spawner import REnemySpawner

ef = open('assets/cfg/enemies.json')
eData = json.load(ef)

def system_enemy_spawner(world:esper.World, runtime:int):
        components = world.get_component(REnemySpawner)
        r_l:REnemySpawner
                
        for (entity, r_l) in components:
                if r_l.timestamp <= runtime/1000 and r_l.generado == False:
                        tamano = eData[r_l.tipo]['size']
                        rgb = eData[r_l.tipo]['color']
                        vel_min = eData[r_l.tipo]['velocity_min']
                        vel_max = eData[r_l.tipo]['velocity_max']
                        vel_ran = random.randint(vel_min, vel_max)
                        size = pygame.Vector2(tamano['x'], tamano['y'])
                        vel = pygame.Vector2(vel_ran, vel_ran)
                        color = pygame.Color(rgb['r'], rgb['g'], rgb['b'])
                        generar_enemigo(world, entity, size, vel, color)
                        r_l.generado = True