import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class FaceVertexMesh:
    def __init__(self):
        self.vertices = []  # Lista de vértices
        self.faces = []     # Lista de faces

    def read_off(self, file_path):
        """Lê um arquivo OFF e armazena os vértices e faces na estrutura."""
        with open(file_path, 'r') as f:
            lines = f.readlines()

        assert lines[0].strip() == "OFF", "O arquivo não está no formato OFF."

        # Lendo número de vértices e faces
        num_vertices, num_faces, _ = map(int, lines[1].split())

        # Lendo vértices
        for i in range(2, 2 + num_vertices):
            self.vertices.append(tuple(map(float, lines[i].split())))

        # Lendo faces
        for i in range(2 + num_vertices, 2 + num_vertices + num_faces):
            parts = list(map(int, lines[i].split()))
            self.faces.append(parts[1:])  # Armazena apenas os índices dos vértices

    def __repr__(self):
        return f"FaceVertexMesh(Vértices={len(self.vertices)}, Faces={len(self.faces)})"

    def plot(self, title="Malha 3D"):
        """Plota a malha 3D utilizando matplotlib."""
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')

        verts = np.array(self.vertices)
        mesh_faces = [[verts[idx] for idx in face] for face in self.faces]

        ax.add_collection3d(Poly3DCollection(mesh_faces, facecolors='cyan', linewidths=0.5, edgecolors='k', alpha=0.5))

        ax.scatter(verts[:, 0], verts[:, 1], verts[:, 2], s=1, color='red')  # Plota os vértices
        ax.set_title(title)

        plt.show()

# Teste com os arquivos fornecidos
mesh1 = FaceVertexMesh()
mesh1.read_off('/mnt/data/hand-hybrid.off')
print(mesh1)
mesh1.plot(title="Malha - Hand Hybrid")

mesh2 = FaceVertexMesh()
mesh2.read_off('/mnt/data/triangles.off')
print(mesh2)
mesh2.plot(title="Malha - Triangles")