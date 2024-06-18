from typing import List
import csv
class Client:

    def __init__(self,dni,name,last_name):
        self.dni = dni
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"({self.dni}) {self.name} {self.last_name}"

class Clients:
    list: List[Client] = []
    with open('clients.csv',newline='\n') as f:
        reader = csv.reader(f, delimiter= ';')
        for dni,name,last_name in reader:
            client = Client(dni,name,last_name)
            list.append(client)

    @staticmethod
    def search(dni):
        for client in Clients.list:
            if client.dni == dni:
                return client

    @staticmethod
    def create(dni,name,last_name):
        client = Client(dni,name,last_name)
        Clients.list.append(client)
        Clients.save()
        return client

    @staticmethod
    def modify(dni,name,last_name):
        for index,client in enumerate(Clients.list):
            if client.dni == dni:
                Clients.list[index].name = name
                Clients.list[index].last_name = last_name
                Clients.save()
                return Clients.list[index]

    @staticmethod
    def delete(dni):
        for index,client in enumerate(Clients.list):
            if client.dni == dni:
                Clients.save()
                return Clients.list.pop(index)


    @staticmethod
    def save():
        with open('clients.csv', 'w', newline='\n') as f:
            writer = csv.writer(f, delimiter=';')
            for client in Clients.list:
                writer.writerow(( client.dni,client.name,client.last_name ))
