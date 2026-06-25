class HashTable:
    def __init__(self):
        self.collection = {}

  
    def hash(self, key: str) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total

    
    def add(self, key, value):
        index = self.hash(key)

       
        if index not in self.collection:
            self.collection[index] = {}

       
        self.collection[index][key] = value

    
    def remove(self, key):
        index = self.hash(key)

        
        if index in self.collection and key in self.collection[index]:
            del self.collection[index][key]

            
            if not self.collection[index]:
                del self.collection[index]

   
    def lookup(self, key):
        index = self.hash(key)

        if index in self.collection and key in self.collection[index]:
            return self.collection[index][key]

        return None
