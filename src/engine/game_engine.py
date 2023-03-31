import pygame
import esper
import json
from src.create.prefab_creator import crear_enemigo
from src.ecs.systems.r_movement import system_movement
from src.ecs.systems.r_rendering import system_rendering
from src.ecs.systems.r_screen_bounce import system_screen_bounce
from src.ecs.systems.r_system_enemy_spawner import system_enemy_spawner

class GameEngine:
    
    
    def __init__(self) -> None:
        pygame.init()
        wf = open('assets/cfg/window.json')
        self.wData = json.load(wf)
        lf = open('assets/cfg/level_01.json')
        lData = json.load(lf)
        events = lData['enemy_spawn_events']
        self.lTime = []
        for event in events:
            self.lTime.append(event['time'])
        wsize = self.wData["size"]
        self.title = self.wData["title"]
        self.screen = pygame.display.set_mode((wsize["w"],wsize["h"]), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        if self.wData["framerate"] == 0:
            self.framerate = 60
        else:
            self.framerate = self.wData["framerate"]
        self.delta_time = 0
        self.ecs_world = esper.World()

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        lf = open('assets/cfg/level_01.json')
        lData = json.load(lf)
        if lData:
            eList = lData['enemy_spawn_events']
            for enemy in eList:
                positions = enemy['position']
                time = enemy['time']
                tipo = enemy['enemy_type']
                pos = pygame.Vector2(positions['x'], positions['y'])
                crear_enemigo(self.ecs_world, time, tipo, pos)

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0
        self.runtime = pygame.time.get_ticks()

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)
        if self.lTime:
            if (min(self.lTime) <= self.runtime/1000):
                system_enemy_spawner(self.ecs_world, self.runtime)
                self.lTime = [x for x in self.lTime if x > self.runtime/1000]

    def _draw(self):
        rgb = self.wData["bg_color"]
        self.screen.fill((rgb["r"], rgb["g"], rgb["b"]))
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
