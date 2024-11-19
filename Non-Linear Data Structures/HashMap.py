# HashMap (dict) example
hash_map = {'a': 1, 'b': 2, 'c': 3, 'e': 5}
print(hash_map.keys())          # Output: dict_keys(['a', 'b', 'c'])
print(hash_map.get('b'))        # Output: 2
hash_map.update({'d': 4})       # Add a new key-value pair
print(hash_map)                 # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
