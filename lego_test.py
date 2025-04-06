import asyncio
from pybricksdev.connections import BluetoothConnection

async def run():
    # Cseréld ki a nevet vagy a címkét ha kell!
    conn = BluetoothConnection("LEGO Technic Large Hub")

    print("Kapcsolódás folyamatban...")
    await conn.connect()
    print("Sikeres kapcsolat!")

    # LED bekapcsolása például zöld színnel
    await conn.write("from pybricks.hubs import TechnicHub\n")
    await conn.write("hub = TechnicHub()\n")
    await conn.write("hub.light.on((0, 255, 0))\n")

    await asyncio.sleep(3)

    # LED kikapcsolása
    await conn.write("hub.light.off()\n")

    await conn.disconnect()
    print("Kapcsolat bontva.")

asyncio.run(run())
