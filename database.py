from typing import List
class Client:

    def __init__(self,dni,name,last_name):
        self.dni = dni
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"({self.dni}) {self.name} {self.last_name}"

class Clients:
    list: List[Client] = []

    @staticmethod
    def search(dni):
        for client in Clients.list:
            if client.dni == dni:
                return client

    @staticmethod
    def create(dni,name,last_name):
        client = Client(dni,name,last_name)
        Clients.list.append(client)
        return client

    @staticmethod
    def modify(dni,name,last_name):
        for index,client in enumerate(Clients.list):
            if client.dni == dni:
                Clients.list[index].name = name
                Clients.list[index].last_name = last_name
                return Clients.list[index]

    @staticmethod
    def delete(dni):
        for index,client in enumerate(Clients.list):
            if client.dni == dni:
                return Clients.list.pop(index)


