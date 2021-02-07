from Queue import *

stinQueue = StinQueue()

queueObject = stinQueue.createQueue("TestQueue1")
print(queueObject.isSuccess)
print(queueObject.data)

queueObject = stinQueue.createQueue("TestQueue2")
print(queueObject.data)

queueObejct = stinQueue.pushToQueue("TestQueue2", "Test Data String")
print(queueObejct.isSuccess)
print(str(queueObejct.errorList))

dataFromQueue = stinQueue.getFromQueue("TestQueue2")
print(dataFromQueue)