# Matrix calculator logic
import numpy as np

class MatrixEngine:
    @staticmethod
    def parse(text):
        # Expects "1,2;3,4" format
        rows = text.split(';')
        mat = []
        for r in rows:
            mat.append([float(x.strip()) for x in r.split(',')])
        return np.array(mat)

    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def sub(a, b): return a - b
    @staticmethod
    def mul(a, b): return np.dot(a, b)
    @staticmethod
    def det(a): return np.linalg.det(a)
    @staticmethod
    def inv(a): return np.linalg.inv(a)
    @staticmethod
    def trans(a): return a.T