import sys

DATABASE_PATH = 'clients.csv'

if 'test' in sys.argv[0]:
    print('loading test database')
    DATABASE_PATH = 'tests/clients_test.csv'
