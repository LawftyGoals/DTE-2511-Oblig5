import asyncio
import time
import random

class Counter():
    # Counter klassen holder styr på antall execute_io som er satt opp. Dette er gjort ved at hver
    # execute_io() kaller increment() som plusser på et i variabelen number. get() returnerer number
    # str er streng versjonen av nummeret så den kan printes for seg selv.
    def __init__(self):
        self.number = 0

    def increment(self):
        self.number += 1

    def get(self):
        return self.number

    def __str__(self):
        return f'{self.number}'


async def execute_io(number: int, counter: Counter) -> int:
    # denne funksjonen startes og avventer mellom 0 og 2 sekunder før den returnerer tversummen
    # av nummeret som den får som argument. -> int tegnet i betegnelsen peker på at retur verdien
    # skal være av typen int.

    # kaller increment i counter klassen for å øke antallet med 1.
    counter.increment()

    # her sover funksjonen mellom 0 og 2 sekunder.
    await asyncio.sleep(random.uniform(0,2))
    
    return tverrsummen(number)

def tverrsummen(number):
    # denne funksjonen endrer tallene til strenger før den da plusser dem på og returnerer tverrsummen.

    final = 0
    
    for x in str(number):
        final += int(x)
    
    return final



async def main():

    task_list = []
    max = 10000
    tverrsum = 0
    counter = Counter()

    # her skapes alle instanser av execute_io i create_task gjennom asyncio. De blir da puttet inn
    # i task_list listen som holder alle sammen gående. for rangen forsikrer at hver funksjon har
    # en unik nummer tildelt.
    for i in range(0, max):
        task_list.append(asyncio.create_task(execute_io(i, counter)))

    # her utløses alle taskene gjennom gather funksjonen til asyncio, returverdiene blir da dyttet
    # inn i tverrsum variabelen for å summere alle slutt talene.
    for y in await asyncio.gather(*task_list):
        tverrsum += y
    
    print(f'Finished processing, result {tverrsum}, got counter: {counter}')


asyncio.run(main())