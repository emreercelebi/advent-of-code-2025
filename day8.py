from __future__ import annotations
from readfile import read_file
from math import sqrt
from typing import List, Tuple

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class Circuit:
    def __init__(self):
        self.points = set()
    
    def add_point(self, p: Point):
        self.points.add(p)

    def add_points(self, ps: List[Point]):
        self.points.update(ps)

    def contains_point(self, p: Point) -> bool:
        return p in self.points
    
    def merge_circuit(self, c: Circuit):
        self.points.update(c.points)
    
    def size(self) -> int:
        return len(self.points)

def distance(p1: Point, p2: Point) -> float:
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)

file_name = "inputs/day8/input.txt"
num_connections = 10 if file_name == "inputs/day8/test.txt" else 1000
lines = read_file(file_name)

def build_points_list() -> List[Point]:
    points = []
    for line in lines:
        coords = [int(val) for val in line.split(",")]
        points.append(Point(coords[0], coords[1], coords[2]))
    
    return points

def build_points_distances_list(points: List[Point]) -> List[Tuple[float, Point, Point]]:
    point_distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point_distances.append((distance(points[i], points[j]), points[i], points[j]))
    
    return sorted(point_distances)

def part1():
    points = build_points_list()
    point_distances = build_points_distances_list(points)
    
    circuit_map = {}
    connections_made = 0
    for pd in point_distances:
        if connections_made == num_connections:
            break
        
        connections_made += 1
        p1, p2 = pd[1], pd[2]
        if p1 in circuit_map and p2 in circuit_map:
            # both in existing circuits
            if circuit_map[p1] == circuit_map[p2]:
                # same circuit, do nothing
                continue
            # otherwise, merge
            p1_circuit = circuit_map[p1]
            p1_circuit.merge_circuit(circuit_map[p2])
            circuit_map[p2] = p1_circuit
        elif p1 in circuit_map:
            # only p1 in existing circuit, add p2
            p1_circuit = circuit_map[p1]
            p1_circuit.add_point(p2)
            circuit_map[p2] = p1_circuit
        elif p2 in circuit_map:
            # only p1 in existing circuit, add p1
            p2_circuit = circuit_map[p2]
            p2_circuit.add_point(p1)
            circuit_map[p1] = p2_circuit
        else:
            # neither in existing circuit, create new one
            new_circuit = Circuit()
            new_circuit.add_points([p1, p2])
            circuit_map[p1] = new_circuit
            circuit_map[p2] = new_circuit

        for p in circuit_map[p1].points:
            circuit_map[p] = circuit_map[p1]
        
    sorted_circuit_sizes = sorted([c.size() for c in set(circuit_map.values())], reverse=True)
    
    return sorted_circuit_sizes[0] * sorted_circuit_sizes[1] * sorted_circuit_sizes[2]

def part2():
    points = build_points_list()
    point_distances = build_points_distances_list(points)
    
    circuit_map = {}
    for pd in point_distances:
        
        p1, p2 = pd[1], pd[2]
        if p1 in circuit_map and p2 in circuit_map:
            # both in existing circuits
            if circuit_map[p1] == circuit_map[p2]:
                # same circuit, do nothing
                continue
            # otherwise, merge
            p1_circuit = circuit_map[p1]
            p1_circuit.merge_circuit(circuit_map[p2])
            circuit_map[p2] = p1_circuit
        elif p1 in circuit_map:
            # only p1 in existing circuit, add p2
            p1_circuit = circuit_map[p1]
            p1_circuit.add_point(p2)
            circuit_map[p2] = p1_circuit
        elif p2 in circuit_map:
            # only p1 in existing circuit, add p1
            p2_circuit = circuit_map[p2]
            p2_circuit.add_point(p1)
            circuit_map[p1] = p2_circuit
        else:
            # neither in existing circuit, create new one
            new_circuit = Circuit()
            new_circuit.add_points([p1, p2])
            circuit_map[p1] = new_circuit
            circuit_map[p2] = new_circuit

        if circuit_map[p1].size() == len(points):
            return p1.x * p2.x

        for p in circuit_map[p1].points:
            circuit_map[p] = circuit_map[p1]
        

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
