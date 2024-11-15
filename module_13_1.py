import asyncio


async def start_srongman(name, power):
    print(f"Силач {name} начал соревнования")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования")


async def start_tournament():
    task1 = asyncio.create_task(start_srongman('Pasha', 3))
    task2 = asyncio.create_task(start_srongman('Denis', 4))
    task3 = asyncio.create_task(start_srongman('Apollon', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())