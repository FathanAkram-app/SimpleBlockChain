class Block:

    def __init__(self, previousHash, transaction):
        self.previousHash = previousHash
        self.transaction = transaction

        contents = {hash(transaction), previousHash}
        self.blockhash = hash(frozenset(contents))
        
    def getPreviousHash(self):
        return self.previousHash
    
    def getTransaction(self):
            return self.transaction
    
    def getBlockHash(self):
            return self.blockhash
    
blockchain = frozenset()
def main():
    transaction = ("jack has sent fathan 10 bitcoin","max has sent fathan 10 bitcoin")
    someBlock = Block(0, transaction=transaction)

    print(someBlock.getBlockHash())

if __name__ == "__main__":
    main()


