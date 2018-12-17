class Cell:
    def __init__(self, x, y, Index, IsWall):
        self.x = x
        self.y = y
        self.Index = Index
        self.IsWall = IsWall
        self.IsStart = False
        self.IsEnd = False
        self.IsPath = False