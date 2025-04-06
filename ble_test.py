import asyncio
from bleak import BleakClient, BleakScanner

# LEGO Hub Bluetooth Service UUID
UART_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
UART_CHAR_UUID = "00001623-1212-efde-1623-785feabcd123"  # TX

async def main():
    print("Keresés LEGO Hub-ra...")
    devices = await BleakScanner.discover()

    for d in devices:
        print(f"TALÁLT ESZKÖZ: {d.name} ({d.address})")
        if "LEGO" in d.name or "Technic" in d.name:
            address = d.address
            break
    else:
        print("Nem találtam LEGO Hub-ot. Kapcsold be párosítási módba!")
        return

    print(f"Kapcsolódás a {address} címhez...")

    async with BleakClient(address) as client:
        print("Kapcsolódva!")

        # Küldjünk egy egyszerű parancsot - pl. LED világítson zölden
        commands = [
            "from pybricks.hubs import TechnicHub\n",
            "hub = TechnicHub()\n",
            "hub.light.on((0, 255, 0))\n"
        ]

        for cmd in commands:
            await client.write_gatt_char(UART_CHAR_UUID, cmd.encode())
            await asyncio.sleep(0.2)

        await asyncio.sleep(3)

        await client.write_gatt_char(UART_CHAR_UUID, "hub.light.off()\n".encode())

        print("Parancsok elküldve, kapcsolat lezárva.")

asyncio.run(main())

