class Hashmap :
  def __init__(self,size):
    self.size = size
    self.check = False
    self.buckets = []
    for i in range(size):
      self.buckets.append([])

  def set(self, key, value):
    Hashed_key = hash(key)
    indice = Hashed_key % self.size

    bucket = self.buckets[indice]

    for i in range(len(bucket)) :
      if bucket[i][0] == key:
        del bucket[i]

    self.buckets[indice].append((key,value))

  def get(self, key):
    hashed_key = hash(key)
    index = hashed_key % self.size
    for a,b in self.buckets[index]:
      if a == hashed_key:
        return a,b
    return "La clée n'est pas la bonne"
  
  def load(self, bucket):
    self.buckets = bucket

  def clear(self):
    self.buckets = []

  def check_if_empty(self):
    for i in range(len(self.buckets)):
      if self.buckets[i] != []: 
        self.buckets = True