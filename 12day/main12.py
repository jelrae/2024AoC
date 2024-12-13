import numpy as np
import re
import math
from collections import defaultdict


class Region:
    def __init__(self, plant, crop_id, init_loc):
        self.ct = plant
        self.cid = crop_id
        self.l = []
        self.add_loc(init_loc)
        self.area = 0
        self.perimeter = 0
        self.num_edges = 0

    def add_loc(self, loc):
        self.l.append(loc)

class GardenPlot:

    def __init__(self, fp='input.txt'):
        data = []
        crops = set()
        with open(fp, 'r') as f:
            for line in f:
                cl = list(line.strip())
                crops = crops | set(cl)
                data.append(cl)
        self.plot = np.array(data)
        self.regions_plot = np.full(self.plot.shape, -1)
        self.width = self.plot.shape[0]
        self.height = self.plot.shape[1]
        self.crop_types = crops
        self.regions = {}
        self.determine_fence_stats()

    # Could also try inserting a ' ' between the different ones to make some kinda barrier????
    def determine_fence_stats(self):
        for i in range(self.plot.shape[0]):
            for j in range(self.plot.shape[1]):
                if i == 0 and j == 0:
                    checked_locs = [[0, 0]]
                    cid = 0
                    cur_plant = self.plot[i, j]
                    self.regions[cid] = Region(self.plot[i, j], cid, [i, j])
                    area = 1
                    perimeter = 2
                    n_edges = 0
                    self.regions_plot[i, j] = cid
                    self.regions[cid], checked_locs = self.check_neighbors([i, j], self.regions[cid], checked_locs)
                elif self.regions_plot[i, j] not in self.regions.keys():
                    cid += 1
                    cur_plant = self.plot[i, j]
                    self.regions[cid] = Region(self.plot[i, j], cid, [i, j])
                    area = 1
                    perimeter = 0
                    n_edges = 0
                    self.regions_plot[i, j] = cid
                    self.regions[cid], checked_locs = self.check_neighbors([i, j], self.regions[cid], checked_locs)
        self.print_regions_map()
        breakpoint()
        for r in self.regions:
            checked_locs = [[0, 0]]
            r.area = len(r.l)
            for plot in r.l:
                if plot[0] == 0 or plot[0] == self.width-1:
                    r.perimeter += 1
                if plot[1] == 0 or plot[1] == self.height-1:
                    r.perimeter += 1
                self.gen_pos_neighbors()

    def calc_perimeter(self, r_cur):


    def gen_pos_neighbors(self, cur_loc, visited_locs):
        i, j = cur_loc
        new_x = [max(0, i - 1), min(self.width - 1, i + 1)]
        new_y = [max(0, j - 1), min(self.height - 1, j + 1)]
        new_locs_x = np.array(np.meshgrid(new_x, j)).T.reshape(-1, 2)
        new_locs_y = np.array(np.meshgrid(i, new_y)).T.reshape(-1, 2)
        pos_locs = np.concatenate((new_locs_x, new_locs_y)).tolist()
        new_locs = []
        for i in pos_locs:
            if i not in visited_locs:
                new_locs.append(i)
        return new_locs

    def check_neighbors(self, cur_loc: list, cur_region: Region, checked_locs: list):
        neighbours = self.gen_pos_neighbors(cur_loc, checked_locs)
        if neighbours:
            for neighbour in neighbours:
                try:
                    if self.plot[tuple(neighbour)] == cur_region.ct:
                        self.regions_plot[tuple(neighbour)] = cur_region.cid
                        cur_region.add_loc(neighbour)
                        checked_locs.append(neighbour)
                        self.check_neighbors(neighbour, cur_region, checked_locs)
                except:
                    breakpoint()
        return cur_region, checked_locs

    def print_regions_map(self):
        print(self.regions_plot)

    def print_garden(self):
        print(self.plot)


def main():
    # fp = "input.txt"
    fp = "ti0.txt"
    garden = GardenPlot(fp)
    garden.print_garden()
    garden.print_regions_map()
    breakpoint()


if __name__ == "__main__":
    main()

# ccl = np.argwhere(self.plot == crop)  # Checked crops locations
# scl = ccl[:].tolist()  # Search crops locations
# while scl:
#     sl = scl.pop(0)
#     subcroplocs = [sl]
#     area = 1
#     perimeter = 0
#     if sl[0] == 0 or sl[0] == self.width - 1:
#         perimeter += 1
#     if sl[1] == 0 or sl[0] == self.height - 1:
#         perimeter += 1
#
#     for crop_loc in scl:
#         if crop_loc
#
#         breakpoint()

# for crop in self.crop_types:
#     cls = np.transpose(np.nonzero(self.plot == crop))
#     check_crop = np.where(self.plot == crop, crop, -1)
#     for i in range(check_crop.shape[0]):
#         for j in range(check_crop.shape[1]):
#             if check_crop[i, j] == crop:
#                 check_crop[i, j] = cid
