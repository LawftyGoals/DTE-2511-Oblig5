import asyncio
import time
import random

class Counter():
    # Counter klassen holder styr på antall execute_io som er satt opp. Dette er gjort ved at hver
    # execute_io() kaller increment() som plusser på et i variabelen number. get() returnerer number
    # str er streng versjonen av self så den kan printes for seg selv.
    def __init__(self):
        self.number = 0

    def increment(self):
        self.number += 1

    def get(self):
        return self.number

    def __str__(self):
        return f'{self.number}'


async def execute_io(number: int, counter: Counter) -> int:
    counter.increment()
    
    await asyncio.sleep(random.uniform(0,2))
    
    return tverrsummen(number)

def tverrsummen(number):
    final = 0
    
    for x in str(number):
        final += int(x)
    
    return final



async def main():
    task_list = []
    max = 10000

    tverrsum = 0

    counter = Counter()

    for i in range(0, max):
        task_list.append(asyncio.create_task(execute_io(i, counter)))

    for y in await asyncio.gather(*task_list):
        tverrsum += y
    
    print(f'Finished processing, result {tverrsum}, got counter: {counter}')


asyncio.run(main())