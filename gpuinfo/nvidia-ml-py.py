from pynvml import *
N.nvmlInit()

deviceCount = N.nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = N.nvmlDeviceGetHandleByIndex(i)
    util = N.nvmlDeviceGetUtilizationRates(handle)
print "Device", i, ":", N.nvmlDeviceGetName(handle)
print "GPU Utilization", i, ":", N.nvmlDeviceGetUtilizationRates(handle)

deviceCount = N.nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = N.nvmlDeviceGetHandleByIndex(i)
    util = str(N.nvmlDeviceGetUtilizationRates(handle))
gpu_util = util[util.index('gpu: ')+4:util.index(' %')+2]
print (gpu_util)

N.nvmlShutdown()