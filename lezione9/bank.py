"""
Classe del Account:
    Attributi:
        account_id: str - identificatore univoco per l'account.
        balance: float - il saldo attuale del conto.
    Metodi:
        deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
        get_balance(): restituisce il saldo corrente del conto.
"""
class Account:
    def __init__(self, account_id: str, balance: float = 0):
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
"""
Classe Bank:
    Attributi:
        accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
    Metodi:
        create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
        deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
        get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
"""
class Bank:
    def __init__(self):
        self.accounts: dict[str, Account] = dict()
    
    def create_account(self, account_id):
        account = Account(account_id)
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")
        self.accounts[account_id] = account
        return account
    
    def deposit(self, account_id, amount):
        self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id].get_balance()