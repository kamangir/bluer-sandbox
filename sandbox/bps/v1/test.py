#!/usr/bin/env python3
import asyncio
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, method
from dbus_next import BusType


class Hello(ServiceInterface):
    def __init__(self):
        super().__init__("org.example.Hello")

    @method()
    def Ping(self) -> "s":
        print("[Python] Ping() called by busctl")
        return "Pong"


async def main():
    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()

    # 🔹 print our unique connection name (:1.<N>)
    print(f"[Python] Connected to system bus with unique name: {bus.unique_name}")

    obj_path = "/org/example/Hello"
    bus.export(obj_path, Hello())

    print(f"exported org.example.Hello at {obj_path}")
    print(f'run in another terminal: "source bps.sh introspect,N={bus.unique_name}"')

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
