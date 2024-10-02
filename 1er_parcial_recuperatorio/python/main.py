from modelos.Bicicleta import Bicicleta
from modelos.Furgoneta import Furgoneta
from modelos.GestorEnvios import GestorEnvios
from modelos.Paquete import Paquete

gestor_envios = GestorEnvios()

paquete_liviano = Paquete(10, 20)
paquete_pesado = Paquete(400, 400)

print(paquete_liviano)
print(paquete_pesado)

transportes = [Bicicleta("Bicicleta"), Furgoneta("Furgoneta")]

gestor_envios.gestionar_envio(transportes, paquete_liviano, 20)
gestor_envios.gestionar_envio(transportes, paquete_pesado, 2000)