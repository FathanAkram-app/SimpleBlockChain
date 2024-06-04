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
    
blockchain = []
def main():
    transaction = ("jack has sent fathan 10 bitcoin","max has sent fathan 10 bitcoin")
    someBlock = Block(0, transaction=transaction)
    blockchain.append(someBlock)

    transaction = ("mark has sent fathan 1000 bitcoin","max has sent fathan 102 bitcoin")
    someBlock2 = Block(someBlock.getBlockHash(), transaction=transaction)
    blockchain.append(someBlock2)

    transaction = ("jeff besos has sent fathan 1000 bitcoin")
    someBlock3 = Block(someBlock.getBlockHash(), transaction=transaction)
    blockchain.append(someBlock3)

    print("first transaction:")
    print(someBlock.getBlockHash())
    print("second transaction:")
    print(someBlock2.getBlockHash())
    print("second transaction:")
    print(someBlock3.getBlockHash())
    print("___________________")
    print("blockchain :")
    for v in blockchain:
        print(v.getBlockHash())

if __name__ == "__main__":
    main()


