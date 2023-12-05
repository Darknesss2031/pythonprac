import asyncio
from time import strftime
#
# async def late(delay, msg):
#     print(f"Start task ({msg}) at {strftime('%X')}")
#     await asyncio.sleep(delay)
#     print(msg)
#     return delay
#
# # async def main():
# #     print(f"> {strftime('%X')}")
# #     await late(1, "One")
# #     print(f"> {strftime('%X')}")
# #     await late(2, "Two")
# #     print(f"> {strftime('%X')}")
# #
# #     # task3 = asyncio.create_task(late(3, "Three"))
# #     # task4 = asyncio.create_task(late(4, "Four"))
# #     await(late(3, "Three"))
# #     await(late(4, "Four"))
# #     print(f"> {strftime('%X')}")
# #     print(f"> {strftime('%X')}")
# #
# # asyncio.run(main())
#
# async def main():
#     res = await asyncio.gather(late(3, "Three"), late(1, "One"), late(2, "Two"))
#     print(res)
#
# asyncio.run(main())

# async def squarer(num):
#     return num**2
#
# async def doubler(num):
#     return num*2
#
# async def main():
#     x, y = list(map(int, input().split()))
#     res1 = await asyncio.gather(squarer(x), squarer(y))
#     res2 = await asyncio.gather(doubler(res1[0]), doubler(res1[1]))
#     print(res2)
#
# asyncio.run(main())

async def snd(evsnd):
    evsnd.set()
    print("> snd generated evsnd")

async def mid1(evsnd, evmid1):
    await evsnd.wait()
    print("< mid1 received evsnd")
    evmid1.set()
    print("> mid1 generated evmid1")

# async def mid2(evsnd, evmid2):
#     await evsnd.wait()
#     print("< mid2 received evsnd")
#     evmid2.set()
#     print("> mid2 generated evmid1")
#
# async def rcv(evmid1, evmid2):
#     await asyncio.gather(evmid1.wait(), evmid2.wait())
#     #await evmid1.wait()
#     print("< rcv received evmid1")
#     #await evmid2.wait()
#     print("< rcv received evmid2")
#
# async def main():
#     evsnd = asyncio.Event()
#     evmid1 = asyncio.Event()
#     evmid2 = asyncio.Event()
#     res = await asyncio.gather(mid2(evsnd, evmid2), rcv(evmid1, evmid2), snd(evsnd), mid1(evsnd, evmid1))
#
# asyncio.run(main())

