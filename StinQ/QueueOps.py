
QueueSystem = []

class QueueOpsResponse:
    def __init__(self, isSuccess, data, errorList):
        self.isSuccess = isSuccess
        self.data = data
        self.errorList = errorList

class QueueMessage:
    def __init__(self, name):
        self.name = name
        self.messageList = []

def isQueueExists(queueName):
    for queue in QueueSystem:
        if (queue.name == queueName):
            return True
    return False

def getQueueByName(queueName):
    for queue in QueueSystem:
        if (queue.name == queueName):
            return queue
    return None

class StinQueue:
    def createQueue(self, queueName):
        if (isQueueExists(queueName)):
            return QueueOpsResponse(False, None, ["Queue Already Exists"])
        QueueSystem.append(QueueMessage(queueName))
        return QueueOpsResponse(True, len(QueueSystem), [])
    
    def pushToQueue(self, queueName, message):
        if (not isQueueExists(queueName)):
            self.createQueue(queueName)
        queueFromList = getQueueByName(queueName)
        if (queueFromList == None):
            return QueueOpsResponse(False, None, ["Queue doesn't exists and creation of new Queue failed"])
        if (queueFromList.messageList != None):
            queueFromList.messageList.append(message)
            return QueueOpsResponse(True, len(queueFromList.messageList), None)
        return QueueOpsResponse(False, None, ["Data String does not exists in Queue Object"])

    def getFromQueue(self, queueName):
        if (not isQueueExists(queueName)):
            return None
        queueFromList = getQueueByName(queueName)
        if (queueFromList == None):
            return QueueOpsResponse(False, None, ["Queue could not be fetched"])
        message = queueFromList.messageList.pop(0)
        return message

