import numpy as np
import itertools


def load_data(fp):
    data = []
    with open(fp, 'r') as f:
        for line in f:
            cl = line.strip().split(',')
            cl = [int(i) for i in reversed(cl)]
            data.append(cl)

    return data


class GridSpace:
    def __init__(self, size, db):
        self.start = tuple([0, 0])
        self.end = tuple([size, size])
        self.safe_grid = np.ones([size + 1, size + 1])
        # self.unsafe_grid = np.zeros([size+1, size+1])
        self.dropped_bits = db
        self.tiles = {}
        self.init_tiles()

    def init_tiles(self):
        for i in range(self.end[0] + 1):
            for j in range(self.end[0] + 1):
                self.tiles[tuple([i, j])] = Tile([i, j], self.end[0] + 1)

    def knockout_panel(self, step):
        panel = tuple(self.dropped_bits[step])
        self.safe_grid[panel] = 0
        ns = self.tiles[tuple(panel)].neighbours
        for n in ns:
            self.tiles[tuple(n)].remove_neighbour(panel)
        del self.tiles[tuple(panel)]

    def jump_to_state(self, end_step):
        if end_step == -1:
            end_step = len(self.dropped_bits)
        for i in range(0, end_step):
            self.knockout_panel(i)
        print(self.safe_grid)
        print(1 - self.safe_grid)

    def find_shortest_path(self):

        perm_set = itertools.permutations(self.safe_grid)


class Tile:
    def __init__(self, pos, max_grid):
        self.pos = pos
        self.max = max_grid
        self.neighbours = self.determine_neighbours()

    def determine_neighbours(self):
        i, j = self.pos
        new_x = [max(0, i - 1), min(self.max - 1, i + 1)]
        new_y = [max(0, j - 1), min(self.max - 1, j + 1)]
        nx = np.array(np.meshgrid(new_x, j)).T.reshape(-1, 2)
        ny = np.array(np.meshgrid(i, new_y)).T.reshape(-1, 2)
        pos_locs = np.concatenate((nx, ny)).tolist()
        n = []
        for i in pos_locs:
            if i != self.pos:
                n.append(i)
        return n

    def remove_neighbour(self, n):
        if n in self.neighbours:
            self.neighbours.remove(n)


def main():
    # fp = 'input.txt'
    gs = 70
    fp = 'ti0.txt'
    gs = 6
    data = load_data(fp)
    grid = GridSpace(gs, data)
    grid.jump_to_state(12)
    breakpoint()


if __name__ == '__main__':
    main()
