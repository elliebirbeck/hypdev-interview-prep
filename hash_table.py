class HashTable:
	
	def __init__(self, size=64):
		self.size = size
		self.slots = [[] for _ in range(self.size)]

	def hash(self, hash_input):
		hash_output = sum(ord(i) for i in str(hash_input))
		return hash_output

	def set(self, key, value):

		index = self.hash(key) % self.size

		# slot is empty, so we can use it
		if self.slots[index]==[]:
			self.slots[index].append((key, value))
			return

		# slot is taken, let's look inside contents
		else:
			for i, (k, v) in enumerate(self.slots[index]):
				# slot is taken by our own key, so update value
				if k==key:
					self.slots[index][i] = (key, value)
					return

			# slot is taken by other keys (hash collision), so append new kv pair to slot
			self.slots[index].append((key, value))
			return


	def get(self, key):

		index = self.hash(key) % self.size

		# look for key within slots
		for i, (k, v) in enumerate(self.slots[index]):
			if k==key:
				return v

		# key not in list, no value to be found
		return None


	# provides use of [] for easier index access
	def __getitem__(self,key):
		return self.get(key)
	def __setitem__(self, key, value):
		self.set(key, value)



if __name__ == '__main__':

	#### TESTS ####

	ht = HashTable() # default size 64

	# populate hash table
	ht.set('Ellie', '0161-822-400')
	ht.set('Joey', '0208-949-123')
	ht.set('Chandler', '0117-111-386')
	print("Hash Table:", ht.slots, sep='\n')

	# replace a key value
	ht.set('Ellie', 'ellie@email.com')
	print("Key 'Ellie' has value '", ht.get('Ellie'), "'", sep='')

	# hash collision
	ht.set('Dolly','dolly@email.com')
	ht.set('Lloyd','lloyd@email.com')
	print("Hash Table:", ht.slots, sep='\n')

	print("Key 'Ellie' has value '", ht.get('Ellie'), "'", sep='') # get a replaced value
	print("Key 'Lloyd' has value '", ht.get('Lloyd'), "'", sep='') # get a collision value
	print("Key 'Phoebe' has value '", ht.get('Phoebe'), "'", sep='') # get a non-existent value

