# -*- coding: utf-8 -*-
"""
__init__.py

Created on 2017-11-19 by hbldh <henrik.blidh@nedomkull.com>

"""

# Use PyObjC and PyObjC Core Bluetooth bindings for Bleak!
import asyncio
import objc

from PyObjCTools import AppHelper

from Foundation import CBCentralManager

from bleak.backends.client import BaseBleakClient

CBCentralManagerDelegate = objc.protocolNamed('CBCentralManagerDelegate')


class BleakClientCoreBluetooth(BaseBleakClient):
    def __init__(self, address, hci_device="hci0", **kwargs):
        super().__init__(address, **kwargs)
        raise NotImplementedError("BleakClientCoreBluetooth not implemented yet.")

    async def connect(self) -> bool:
        pass


class ManagerDelegate():
    def centralManagerDidUpdateState_(self, manager):
        self.manager = manager
        manager.scanForPeripheralsWithServices_options_(None, None)

    def centralManager_didDiscoverPeripheral_advertisementData_RSSI_(self, manager, peripheral, data, rssi):
        print(str(peripheral.UUID), data, rssi)

    def didDiscoverPeripheral(self, *args, **kwargs):
        print(args, kwargs)

    def didDiscover(self, *args, **kwargs):
        print(args, kwargs)


async def discover(timeout=5.0, loop=None, **kwargs):
    device = kwargs.get("device", "hci0")
    loop = loop if loop else asyncio.get_event_loop()
    delegate = ManagerDelegate()

    manager = CBCentralManager.alloc().initWithDelegate_queue_options_(delegate, None, None)

    cached_devices = {}
    devices = {}
    AppHelper.runConsoleEventLoop()

#    while True:
#        manager.scanForPeripheralsWithServices_options_([], None)


if __name__ == '__main__':
    asyncio.run(discover())
