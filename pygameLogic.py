class Pygame :
    def __init__(self, pygameModule) -> None:
        self.screen = pygameModule.display.set_mode([700, 700])
        self.ennemySurface = pygameModule.Surface((500, 700))




