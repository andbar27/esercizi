class DatabaseConnection:

    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.connection = None

    def connect(self):
        print(f"Connetting to database: {self.db_name}")
        self.connection = f"Connection to {self.db_name}"

    def disconnect(self):
        print(f"Disconnect")
        self.connection = None

    def rollback(self):
        print("Rollback")

    
    def exec_query(self, query):
        print("exec query", query)
        return f"Result {query}"

    def commit(self):
        print("commit")


class DataBaseContextManager:
    #   Eseguite subito dopo il with
    def __init__(self, db_name) -> None:
        self.db = DatabaseConnection(db_name)


    def __enter__(self):
        self.db.connect()

    #   Eseguita subito prima della fine del with
    def __exit__(self, exception_type, exception_value, traceback):
         
        if exception_type is not None:
            self.db.rollback()
            print("Fail")
        
        else:
            self.db.commit()

        self.db.disconnect()

        return False
    


db_name = "miodb"
query = "select *"

try:
    with DataBaseContextManager(db_name) as db:
        results = db.exec_query()
        print("results: ", results)
        
except Exception as e:
    print("exception: ", e)







def generatore():

    yield "a"
    yield "b"
    yield "c"


prova_generatore = generatore()
prova_generatore2 = generatore()

print(next(prova_generatore))   # cambia lo stato  
print(next(generatore()))       
print(next(generatore()))       # non cambia lo stato ma riparte dal primo
print(next(prova_generatore2))
print(next(prova_generatore2))  # è un'istanza diversa con il suo stato
print(next(prova_generatore))


#   NON FUNGE, ERRORE NELLE SLIDE (?) ########################################
from contextlib import contextmanager

@contextmanager
def timer(*args):
    
    import time

    start_time = time.time()    # Prima di yield esegue __enter__

    yield

    end_time = time.time()      # Dopo di yield esegue __exit__
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time}")

@timer
def prova1(a,b,c):
    return a + b + c


prova1(1,2,3)
#############################################################################