class HashTable:
    def __init__(self, size):
        self.lst = [None for i in range(0, size)]
        self.size = size

    def hashFunction(self, string):
        hashValue = 0
        for char in string:
            hashValue += ord(char)
            hashValue = (hashValue * ord(char)) % self.size
        return hashValue

    def insertEntry(self, string):
        if string is not None:
            hashedString = self.hashFunction(string)
            self.lst[hashedString] = string
            return True
        return False

    def printHashTable(self):
        for i in range(0, len(self.lst)):
            print(f"{i} - {self.lst[i]}")

    def findEntry(self, string):
        hashedString = self.hashFunction(string)
        if self.lst[hashedString] is not None:
            return True
        else:
            return False

    def deleteEntry(self, string):
        hashedString = self.hashFunction(string)
        if self.lst[hashedString] is not None:
            self.lst[hashedString] = None
            return True
        else:
            return False


if __name__ == "__main__":
    hashtable = HashTable(10)
    hashtable.insertEntry("Leonardo")
    hashtable.insertEntry("John")
    hashtable.printHashTable()
    print(hashtable.findEntry("Leonardo"))
    print(hashtable.findEntry("Doe"))
    print(hashtable.deleteEntry("John"))
    hashtable.printHashTable()

