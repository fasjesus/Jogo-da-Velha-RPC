# Flávia Alessandra Santos de Jesus.
import xmlrpc.server
from game import JogoDaVelha

servidor = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8080))
servidor.register_instance(JogoDaVelha())

print("Servidor do Jogo da Velha RPC rodando...")
servidor.serve_forever()
