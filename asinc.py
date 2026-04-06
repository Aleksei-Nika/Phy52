import asyncio
import time

def make_coffee():
    print('Начинаю делать кофе')
    time.sleep(2)
    print('кофе готов!')

def make_tost():
    print('Начинаю делать тосты')
    time.sleep(2)
    print('тост готов!')

start_time = time.time()
make_coffee()
make_tost()
print(time.time() - start_time)

async def as_make_coffee():
    print('Начинаю делать кофе')
    await asyncio.sleep(5)
    print('кофе готов!')

async def as_make_tost():
    print('Начинаю делать тосты')
    await asyncio.sleep(2)
    print('тост готов!')


async def main():
    start_time = time.time()
    await asyncio.gather(as_make_coffee(), as_make_tost())
    print(time.time() - start_time)

asyncio.run(main())