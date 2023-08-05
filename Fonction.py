class Menu:
    def __init__(self):
        self.x = 0
        self.y = 0

    def Import(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def Export(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def Comparaison(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy