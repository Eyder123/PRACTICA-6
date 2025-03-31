import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sumar(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def restar(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    
    def multiplicar_por_escalar(self, escalar):
        return Vector(self.x * escalar, self.y * escalar, self.z * escalar)
    
    def dividir_por_escalar(self, escalar):
        return Vector(self.x / escalar, self.y / escalar, self.z / escalar)
    
    def es_igual(self, otro):
        return self.x == otro.x and self.y == otro.y and self.z == otro.z
    
    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def producto_vectorial(self, otro):
        return Vector(self.y * otro.z - self.z * otro.y,
                      self.z * otro.x - self.x * otro.z,
                      self.x * otro.y - self.y * otro.x)
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalizar(self):
        mag = self.magnitud()
        return self.dividir_por_escalar(mag) if mag != 0 else None
    
    def es_perpendicular(self, otro):
        return self.producto_escalar(otro) == 0
    
    def es_paralelo(self, otro):
        return self.producto_vectorial(otro) == Vector(0, 0, 0)
    
    def proyeccion_sobre(self, otro):
        return otro.multiplicar_por_escalar(self.producto_escalar(otro) / otro.producto_escalar(otro))
    
    def componente_en_direccion(self, otro):
        return (self.producto_escalar(otro) / otro.magnitud())
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Ejemplo de uso:
a = Vector(3, 4, 0)
b = Vector(6, 8, 0)

print("Suma de vectores:", a.sumar(b))
print("Resta de vectores:", a.restar(b))
print("Producto escalar:", a.producto_escalar(b))
print("Producto vectorial:", a.producto_vectorial(b))
print("¿Son perpendiculares?", a.es_perpendicular(b))
print("¿Son paralelos?", a.es_paralelo(b))
print("Proyección de a sobre b:", a.proyeccion_sobre(b))
print("Componente de a en la dirección de b:", a.componente_en_direccion(b))