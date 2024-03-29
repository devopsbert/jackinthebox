#Fixture module for defining the various fixture types
from abc import ABC, abstractmethod
from modules.eventArgs import EventArgs as Event  

class Fixture(ABC):
    'Fixtures for the habitat'
    def __init__(self, params):
        #initize the private __state
        self.__state = 0

        #load values from params
        try:
           self.Id = params['id']
           self.Name = params['name'] 
           self.state = params['state']
        except Exception as exception:
            if exception.args[0] == 'state':
                self.state = 0
            else:
                print(f"error occured: {exception}")

    @property
    def state(self):
        return(self.__state)

    @state.setter 
    def state(self, value):
        if self.__state != value:
            self.__state = 'on' if value == 1 else 'off' 
            self.state_changed(Event('Set_State',value))
            print(f'Your turned me {self.__state}!')

    def state_changed(self, eventArgs):
        self.before_state_change(eventArgs)
        print(f'State change: {eventArgs.EventName}')
        self.on_state_changed(eventArgs)
    
    def before_state_change(self, eventArgs):
        print('Migght wanna check something here')
      
    def on_state_changed(self, eventArgs):
        print(f'Object has changed, event called was: {eventArgs.EventName}')


class SimpleFixture(Fixture):
    'Simple light fixture'

    def on_state_changed(self, eventArgs):
        super().on_state_changed(eventArgs)
        print('some additional stuff')



