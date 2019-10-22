class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        bordery = len(grid)
        borderx = len(grid[0])
        islandscount = 0
        x, y = 0, 0
        while 0 <= y < bordery:
            island = False
            while 0 <= x < borderx:
                if grid[y][x] == "1":
                    islandscount += 1
                    grid = self.wipeIsland([y, x], grid)
                x += 1
            y += 1
            x = 0
        return islandscount

    def wipeIsland(self, coordenate: list[int], grid: list[list[str]]) -> list:
        y, x = coordenate[0], coordenate[1]
        bordery = len(grid)
        borderx = len(grid[0])
        grid[y][x] = "0"

        if x + 1 < borderx and grid[y][x + 1] == "1":
            self.wipeIsland([y, x + 1], grid)
        if x - 1 >= 0 and grid[y][x - 1] == "1":
            self.wipeIsland([y, x - 1], grid)
        if y + 1 < bordery and grid[y + 1][x] == "1":
            self.wipeIsland([y + 1, x], grid)
        if y - 1 >= 0 and grid[y - 1][x] == "1":
            self.wipeIsland([y - 1, x], grid)

        return grid
