# https://leetcode.com/problems/satisfiability-of-equality-equations/


import collections
import string
from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        uf = {a: a for a in string.lowercase}
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)

    def equationsPossible2(self, equations: 'List[str]') -> 'bool':
        graph = collections.defaultdict(set)
        notEquals = []

        def canMeet(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for v in graph[u]:
                if v in visited:
                    continue
                if canMeet(v, target, visited):
                    return True
            return False

        for eq in equations:
            if eq[1:3] == '!=':
                a, b = eq.split('!=')
                notEquals.append((a, b))
                continue
            u, v = eq.split('==')
            graph[u].add(v)
            graph[v].add(u)

        for u, v in notEquals:
            if canMeet(u, v, set()):
                return False
        return True
