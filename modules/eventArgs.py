class EventArgs:
    'Event arguments object for passing'
    def __init__(self, eventName, eventData):
        self.__EventName = eventName
        self.__EventData = eventData

    @property
    def EventName(self):
        return self.__EventName
    
    @property 
    def EventData(self):
        return self.__EventData

    @EventName.setter
    def EventName(self, eventName):
        self.__EventName = eventName

    @EventData.setter
    def EventData(self, eventData):
        self.__EventData = eventData

