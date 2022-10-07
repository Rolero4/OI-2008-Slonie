import sys

from typing import List


class Elephants:
    def __init__(self, file: List[str]):
        self.elephant_count = int(file[0])
        self.weights = [int(element) for element in file[1].split()]
        self.start_order = [int(element) for element in file[2].split()]
        self.end_order = [int(element) for element in file[3].split()]
        self.permutation = []
        self.permutation = Elephants.permutation_construction(self)

    # function which make permutation list for each elephant
    def permutation_construction(self) -> List[int]:
        perm = self.elephant_count * [0]
        for i in range(0, self.elephant_count):
            perm[self.end_order[i] - 1] = self.start_order[i]
        return perm

    # function which make one cycle from the start to the end
    def make_one_cycle(self, start_point: int) -> List[int]:
        current_cycle = []
        next_point = self.permutation[start_point] - 1
        current_cycle.append(next_point)  # adding first element of cycle
        # as long as it's not the end of cycle we are adding another one point to the cycle
        while start_point != next_point:
            next_point = self.permutation[next_point] - 1
            current_cycle.append(next_point)

        return current_cycle

    # final calculation of weight
    def calculate(self) -> int:
        total_weight = 0
        elephant_indexes = list(range(self.elephant_count))
        total_min = min(self.weights)
        while len(elephant_indexes) > 0:
            current_cycle = Elephants.make_one_cycle(self, elephant_indexes[0])
            current_cycle_parameters = Elephants.method_parameters(self, current_cycle)
            total_weight += min(Elephants.method_first(current_cycle_parameters[0], current_cycle_parameters[1],
                                                       current_cycle_parameters[2]),
                                Elephants.method_second(current_cycle_parameters[0], current_cycle_parameters[1],
                                                        current_cycle_parameters[2], total_min))
            for elephant in current_cycle:  # removing variables from a list
                elephant_indexes.remove(elephant)

        return total_weight

    # method which gives basic info about cycle
    def method_parameters(self, cycle: List[int]) -> tuple:
        weight_of_cycle = 0
        min_in_cycle = self.weights[cycle[0]]
        for i in cycle:
            weight_of_cycle += self.weights[i]
            if self.weights[i] < min_in_cycle:
                min_in_cycle = self.weights[i]
        return weight_of_cycle, min_in_cycle, len(cycle)

    # first method to calculate weight of elephants in cycle
    @staticmethod
    def method_first(weight_of_cycle: int, min_in_cycle, cycle_length: int) -> int:
        return weight_of_cycle + (cycle_length - 2) * min_in_cycle

    # second method to calculate weight of elephants in cycle
    @staticmethod
    def method_second(weight_of_cycle: int, min_in_cycle, cycle_length: int, total_min: int) -> int:
        return weight_of_cycle + min_in_cycle + (cycle_length + 1) * total_min


if __name__ == '__main__':
    problem = Elephants(sys.stdin.readlines())
    print(problem.calculate())
