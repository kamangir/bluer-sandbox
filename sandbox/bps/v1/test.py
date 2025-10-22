#!/usr/bin/env python3
import asyncio
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, method
from dbus_next import BusType


# A simple D-Bus service with one Ping() method.
class Hello(ServiceInterface):
    def __init__(self):
        super().__init__("org.example.Hello")

    @method()
    def Ping(self) -> "s":
        print("[Python] Ping() called by busctl")
        return "Pong"


async def main():
    # Connect explicitly to the SYSTEM bus (the one BlueZ uses)
    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()

    # Export our Hello interface on the object path below
    obj_path = "/org/example/Hello"
    bus.export(obj_path, Hello())

    print(f"[Python] Exported org.example.Hello at {obj_path}")
    print("[Python] Keep this running and use another terminal to introspect:")
    print("    sudo busctl --system list")
    print("    sudo busctl --system introspect :1.<N> /org/example/Hello")
    print(
        "    sudo busctl --system call :1.<N> /org/example/Hello org.example.Hello Ping"
    )
    print("---------------------------------------------------------")

    # Keep process alive forever
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
