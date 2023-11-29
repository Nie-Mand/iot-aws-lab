from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def get_on_connection_interrupted(self):
        pass

    @abstractmethod
    def get_on_connection_resumed(self):
        pass

    @abstractmethod
    def get_on_connection_success(self):
        pass

    @abstractmethod
    def get_on_connection_failure(self):
        pass

    @abstractmethod
    def get_on_connection_closed(self):
        pass

    @abstractmethod
    def get_on_message_received(self):
        pass
