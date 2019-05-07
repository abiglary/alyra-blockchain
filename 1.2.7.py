hash_table = [[] for _ in range(8)]

ville_ip = [
    ("Amsterdam", "153.8.223.72"),
    ("Chennai", "169.38.84.49"),
    ("Dallas", "169.46.49.112"),
    ("Dallas, TX, USA", "184.173.213.155"),
    ("Frankfurt", "159.122.100.41"),
    ("Hong Kong", "119.81.134.212"),
    ("London", "5.10.5.200"),
    ("London", "158.176.81.249"),
    ("Melbourne", "168.1.168.251"),
    ("Mexico City", "169.57.7.230"),
    ("Milan", "159.122.142.111"),
    ("Paris", "159.8.78.42"),
    ("San Jose", "192.155.217.197"),
    ("São Paulo", "169.57.163.228"),
    ("Toronto", "169.56.184.72"),
    ("Washington DC", "50.87.60.166")
]

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

for kv in ville_ip:
    k,v = kv
    insert(hash_table, k, v)

print(hash_table)

def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

# print(search(hash_table, "Amsterdam"))

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print('Key {} deleted'.format(key))
    else:
        print('Key {} not found'.format(key))

# delete(hash_table, "Paris")
# print(hash_table)