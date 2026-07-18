import asyncio

async def make_food():
    print("making food...")
    await asyncio.sleep(2)    # wait but in non blocking fashion
    print("food is ready")

asyncio.run(make_food())    