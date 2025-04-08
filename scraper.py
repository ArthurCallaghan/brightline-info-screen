import requests
from bs4 import BeautifulSoup
import json

def obtener_salidas_brightline():
    url = 'https://www.gobrightline.com/train-departures'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    trenes = []

    salidas = soup.find_all('div', class_='departure-card')

    for salida in salidas[:4]:
        destino = salida.find('div', class_='departure-destination')
        hora = salida.find('div', class_='departure-time')
        estado = salida.find('div', class_='departure-status')

        if destino and hora:
            trenes.append({
                'destino': destino.text.strip(),
                'hora': hora.text.strip(),
                'estado': estado.text.strip() if estado else 'Unknown'
            })

    with open('trenes.json', 'w') as f:
        json.dump(trenes, f, indent=2)

    print("✅ Horarios guardados en trenes.json")

if __name__ == '__main__':
    obtener_salidas_brightline()
