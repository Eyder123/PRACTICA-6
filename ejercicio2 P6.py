import numpy as np

class Vector:
    def __init__(self, coordenadas):
        self.coordenadas = np.array(coordenadas, dtype=float)
    
    def __add__(self, otro):
        return Vector(self.coordenadas + otro.coordenadas)
    
    def __sub__(self, otro):
        return Vector(self.coordenadas - otro.coordenadas)
    
    def __mul__(self, escalar):
        return Vector(self.coordenadas * escalar)
    
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    
    def __truediv__(self, escalar):
        return Vector(self.coordenadas / escalar)
    
    def __repr__(self):
        return f"Vector({self.coordenadas.tolist()})"
    
    def producto_escalar(self, otro):
        return np.dot(self.coordenadas, otro.coordenadas)
    
    def producto_cruzado(self, otro):
        return np.cross(self.coordenadas, otro.coordenadas)
    
    def es_perpendicular_a(self, otro):
        return np.isclose(np.dot(self.coordenadas, otro.coordenadas), 0)
    
    def es_paralelo_a(self, otro):
        return np.isclose(np.cross(self.coordenadas, otro.coordenadas), 0).all()
    
    def proyeccion_sobre(self, otro):
        norma_otro_cuadrado = np.dot(otro.coordenadas, otro.coordenadas)
        if np.isclose(norma_otro_cuadrado, 0):
            raise ValueError("No se puede proyectar sobre el vector cero.")
        return (np.dot(self.coordenadas, otro.coordenadas) / norma_otro_cuadrado) * otro.coordenadas
    
    def componente_en(self, otro):
        norma_otro = np.linalg.norm(otro.coordenadas)
        if np.isclose(norma_otro, 0):
            raise ValueError("No se puede calcular el componente en el vector cero.")
        return (np.dot(self.coordenadas, otro.coordenadas) / norma_otro)

# Ejemplo de uso
a = Vector([2, 5])
b = Vector([4, 10])

print("Producto escalar:", a.producto_escalar(b))
print("Producto cruzado:", a.producto_cruzado(b))
print("¿Son perpendiculares?:", a.es_perpendicular_a(b))
print("¿Son paralelos?:", a.es_paralelo_a(b))
print("Proyección de a sobre b:", a.proyeccion_sobre(b))
print("Componente de a en b:", a.componente_en(b))
