import  Transaction

class TransactionData(Transaction):
    def __init__(self, data):
        super().__init__()
        self.data = data
        max = 64
        if len(data) > 64:
            self.data = data[:max]

def validateDataInTransaction(transaction):
    if isinstance(transaction, TransactionData):
        if len(transaction.data) > 64:
            return "Invalido"
        else:
            return "Valido"
    return "Essa transacao nao eh do tipo TransactionData"