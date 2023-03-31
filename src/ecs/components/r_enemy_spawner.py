import pygame

class REnemySpawner:
    def __init__(self, timestamp:float, tipo:str) -> None:
        self.timestamp = timestamp
        self.tipo = tipo