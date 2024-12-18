import numpy as np
import itertools
from heapq import heapify, heappop, heappush

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
        self.gridsize = size + 1
        self.start = tuple([0, 0])
        self.end = tuple([size, size])
        self.safe_grid = np.ones([self.gridsize, self.gridsize])
        self.dropped_bits = db
        self.tiles = {}
        self.loc_to_id = {}
        self.id_to_loc = {}
        self.init_tiles()
        self.cur_time = 0

    def init_tiles(self):
        id = 0
        for i in range(self.end[0] + 1):
            for j in range(self.end[0] + 1):
                self.tiles[tuple([i, j])] = Tile(id,[i, j], self.end[0] + 1)
                self.loc_to_id[tuple([i, j])] = id
                self.id_to_loc[id] = tuple([i, j])
                id += 1

    def knockout_panel(self):
        panel = tuple(self.dropped_bits[self.cur_time])
        self.safe_grid[panel] = 0
        ns = self.tiles[tuple(panel)].neighbours
        for n in ns:
            self.tiles[tuple(n)].remove_neighbour(panel)
        del self.tiles[tuple(panel)]
        self.cur_time += 1

    def jump_to_state(self, end_step):
        if end_step == -1:
            end_step = len(self.dropped_bits)
        for i in range(0, end_step):
            self.knockout_panel()
        # print(self.safe_grid)
        # print(1 - self.safe_grid)

    def find_shortest_path(self):
        self.distance = {p: np.inf for p in self.tiles.keys()}
        self.paths = {p: [] for p in self.tiles.keys()}
        ten_dist = 0
        visited_locs = set()
        self.distance[self.start] = 0
        clc = self.loc_to_id[self.start]
        pos_locs = [(0, clc)]
        heapify(pos_locs)
        while pos_locs:
            cd, clc = heappop(pos_locs)
            if clc in visited_locs:
                continue
            visited_locs.add(clc)
            try:
                for neigh in self.tiles[self.id_to_loc[clc]].neighbours:
                    ten_dist = cd + 1
                    if ten_dist < self.distance[neigh]:
                        self.distance[neigh] = ten_dist
                        heappush(pos_locs, (ten_dist, self.loc_to_id[neigh]))
            except:
                breakpoint()

    def find_first_blockage(self):
        can_escape = True
        while can_escape:
            self.knockout_panel()
            self.find_shortest_path()
            if self.distance[tuple(self.end)] == np.inf:
                can_escape = False
        print("The panel which causes us to be unable to escape is {}".format(self.dropped_bits[self.cur_time-1]))
class Tile:
    def __init__(self, id, pos, max_grid):
        self.id = id
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
                n.append(tuple(i))
        return n

    def remove_neighbour(self, n):
        if n in self.neighbours:
            self.neighbours.remove(n)


def main():
    fp = 'input.txt'
    gs = 70
    es = 1024
    # fp = 'ti0.txt'
    # gs = 6
    # es = 12
    data = load_data(fp)
    grid = GridSpace(gs, data)
    grid.jump_to_state(es)
    grid.find_shortest_path()
    print("The shortest path to {0} was {1}".format(grid.end, grid.distance[tuple(grid.end)]))
    grid.find_first_blockage()


if __name__ == '__main__':
    main()
