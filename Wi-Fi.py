import network
import urequests
from time import sleep

wlan = network.WLAN(network.STA_IF)

if not wlan.active():
  wlan.active(True)

while not wlan.isconnected():
  wlan.connect('Gabriel','gabbog98')
  print('Tentando se conectar a rede...')
  sleep(1)
  print('Codigo de estado de conexao '+str(wlan.status()))
 
print('Conectado')
print('Dados da interface de rede '+str(wlan.ifconfig()))
print('Realizando uma consulta na API de adviceslip')

response = urequests.get('https://api.adviceslip.com/advice')
objeto_json = response.json()

print('Conselho:'+objeto_json['slip']['advice'])


