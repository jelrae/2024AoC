import numpy as np
import re
import math
from collections import defaultdict


# To make a propper network should have probably created something with up down left and right to be able to just
# keep track of who is where and when


class Region:
    def __init__(self, plant, crop_id, init_loc):
        self.ct = plant
        self.cid = crop_id
        self.l = []
        self.add_loc(init_loc)
        self.area = 0
        self.perimeter = 0
        self.num_edges = 0
        self.num_corners = 0
        self.edges = []

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
                    n_edges = 0
                    self.regions_plot[i, j] = cid
                    self.regions[cid], checked_locs = self.check_neighbors([i, j], self.regions[cid], checked_locs)
                elif self.regions_plot[i, j] not in self.regions.keys():
                    cid += 1
                    cur_plant = self.plot[i, j]
                    self.regions[cid] = Region(self.plot[i, j], cid, [i, j])
                    n_edges = 0
                    self.regions_plot[i, j] = cid
                    self.regions[cid], checked_locs = self.check_neighbors([i, j], self.regions[cid], checked_locs)
        # self.print_regions_map()
        for reg_id, reg in self.regions.items():
            checked_locs = []
            reg.area = len(reg.l)
            reg.num_corners = 0
            for plot in reg.l:
                if plot[0] == 0 or plot[0] == self.width-1:
                    reg.perimeter += 1
                if plot[1] == 0 or plot[1] == self.height-1:
                    reg.perimeter += 1
                checked_locs.append([plot])
                ns = self.gen_pos_neighbors(plot, checked_locs)
                for n in ns:
                    if n not in reg.l:
                        reg.perimeter += 1
                    else:
                        checked_locs.append(n)
                i,j = plot
                up = [i, j-1]
                down = [i, j+1]
                left = [i-1, j]
                right = [i+1, j]
                d0 = [right[0], up[1]]
                d1 = [left[0], up[1]]
                d2 = [left[0], down[1]]
                d3 = [right[0], down[1]]
                q0 = [up, right, d0]
                q1 = [up, left, d1]
                q2 = [down, left, d2]
                q3 = [down, right, d3]

                # check for q0 corner
                if up in reg.l and right in reg.l and d0 not in reg.l:
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, up, right, d0]))
                # check for q1 corner
                if up in reg.l and left in reg.l and d1 not in reg.l:
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, up, left, d1]))
                # check for q2 corner
                if down in reg.l and left in reg.l and d2 not in reg.l:
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, down, left, d2]))
                # check for q3 corner
                if down in reg.l and right in reg.l and d3 not in reg.l:
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, down, right, d3]))
                # Check for basic corner 0
                if not(up in reg.l or right in reg.l):
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, up, right, d0]))
                # Check for basic corner 1
                if not (up in reg.l or left in reg.l):
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, up, left, d1]))
                # Check for basic corner 2
                if not (down in reg.l or left in reg.l):
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, down, left, d2]))
                # Check for basic corner 3
                if not (down in reg.l or right in reg.l):
                    reg.num_corners += 1
                    reg.edges.append(tuple([plot, down, right, d3]))


            if reg.ct == 'B':
                for edge in reg.edges:
                    print("Corner found at location {0}, corner: {1}".format(edge[0], edge[1:]))
                print(reg.num_edges)


    def gen_pos_neighbors(self, cur_loc, visited_locs):
        i, j = cur_loc
        new_x = [max(0, i - 1), min(self.width - 1, i + 1)]
        new_y = [max(0, j - 1), min(self.height - 1, j + 1)]
        new_locs_x = np.array(np.meshgrid(new_x, j)).T.reshape(-1, 2)
        new_locs_y = np.array(np.meshgrid(i, new_y)).T.reshape(-1, 2)
        pos_locs = np.concatenate((new_locs_x, new_locs_y)).tolist()
        new_locs = []
        for i in pos_locs:
            if i not in visited_locs and i != cur_loc:
                new_locs.append(i)
        return new_locs

    def check_neighbors(self, cur_loc: list, cur_region: Region, checked_locs: list):
        checked_locs.append(cur_loc)
        neighbours = self.gen_pos_neighbors(cur_loc, checked_locs)
        if neighbours:
            for neighbour in neighbours:
                try:
                    if self.plot[tuple(neighbour)] == cur_region.ct and neighbour not in checked_locs:
                        self.regions_plot[tuple(neighbour)] = cur_region.cid
                        cur_region.add_loc(neighbour)
                        # print(cur_region.l)
                        # This is pointless since we do this later with a sum (we are being inefficient atm but thats ok)
                        cur_region.area += 1
                        self.check_neighbors(neighbour, cur_region, checked_locs)
                except:
                    breakpoint()
        return cur_region, checked_locs

    def print_regions_map(self):
        print(self.regions_plot)

    def print_garden(self):
        print(self.plot)

    def print_regions_sizes(self, check_regions = False):
        cost_full = 0
        cost_discount = 0
        if check_regions:
            for reg_id, reg in self.regions.items():
                print("For Region {0} we have an area of {1}, a perimeter of {2}, and a number of corners of {3}".format(reg_id, reg.area, reg.perimeter, reg.num_corners))
                cost_full += np.sum(reg.area * reg.perimeter)
                cost_discount += np.sum(reg.area * reg.num_corners)
        else:
            costs_full = [np.sum(reg.area * reg.perimeter) for _, reg in self.regions.items()]
            cost_full = np.sum(costs_full)

            costs_discount = [np.sum(reg.area * reg.num_corners) for _, reg in self.regions.items()]
            cost_discount = np.sum(costs_discount)
        print("The full cost found for this plot is: {0}".format(cost_full))
        print("The discounted cost found for this plot is: {0}".format(cost_discount))


def main():
    fp = "input.txt"
    # fp = "ti4.txt"
    garden = GardenPlot(fp)
    garden.print_garden()
    garden.print_regions_map()
    garden.print_regions_sizes(False)


if __name__ == "__main__":
    main()

