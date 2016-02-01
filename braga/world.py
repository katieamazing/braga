from braga.entity import Entity


class World(object):

    def __init__(self):
        self.entities = set()

    def entities_with_aspect(self, aspect):
        return set([entity for entity in self.entities if entity in aspect])

    def make_entity(self, assemblage=None, **kwargs):
        if not assemblage:
            new_entity = Entity()
        else:
            new_entity = assemblage.make(**kwargs)

        self.entities.add(new_entity)
        return new_entity
