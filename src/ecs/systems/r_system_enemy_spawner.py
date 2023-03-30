

import esper


def crear_rectangulo(ecs_world:esper.World, runtime: int):
        rect_entity = ecs_world.create_entity()
        ecs_world.add_component(rect_entity, 
                                     RSurface(size, col))
        ecs_world.add_component(rect_entity, 
                                     RTransform(pos))
        ecs_world.add_component(rect_entity,
                                     RVelocity(vel))