import pygame
import esper
import json
from src.create.prefab_creator import crear_rectangulo
from src.ecs.systems.r_movement import system_movement
from src.ecs.systems.r_rendering import system_rendering
from src.ecs.systems.r_screen_bounce import system_screen_bounce

class GameEngine:
    
    
    def __init__(self) -> None:
        pygame.init()
        wf = open('assets/cfg/window.json')
        ef = open('assets/cfg/enemies.json')
        lf = open('assets/cfg/level_01.json')
        self.wData = json.load(wf)
        self.eData = json.load(ef)
        self.lData = json.load(lf)
        self.rList = self.lData["enemy_spawn_events"]
        wsize = self.wData["size"]
        self.title = self.wData["title"]
        self.screen = pygame.display.set_mode((wsize["w"],wsize["h"]), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
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
        crear_rectangulo(self.ecs_world,
                         pygame.Vector2(50, 30),
                         pygame.Vector2(100, 100),
                         pygame.Vector2(100, 100),
                         pygame.Color(255, 100, 100))

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0
        self.runtime = pygame.time.get_ticks()

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.K_MINUS:
                self.rList.pop(0)

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)
        if self.rList:
            pass

    def _draw(self):
        rgb = self.wData["bg_color"]
        self.screen.fill((rgb["r"], rgb["g"], rgb["b"]))
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
