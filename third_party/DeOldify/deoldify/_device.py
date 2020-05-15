import os
from enum import Enum
from .device_id import DeviceId

# NOTE:  This must be called first before any torch imports in order to work properly!


class DeviceException(Exception):
    pass


class _Device:
    def __init__(self):
        self.set(DeviceId.GPU0)

    def is_gpu(self):
        """ Returns `True` if the current device is GPU, `False` otherwise. """
        return self.current() is not DeviceID.CPU

    def current(self):
        return self._current_device

    def set(self, device: DeviceId):
        if device == DeviceId.CPU:
            os.environ["CUDA_VISIBLE_DEVICES"] = ""
        else:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(device.value)
            import torch

            torch.backends.cudnn.benchmark = False

        os.environ["OMP_NUM_THREADS"] = "1"
        self._current_device = device
        return device
