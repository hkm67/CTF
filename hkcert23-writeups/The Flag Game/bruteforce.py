import hashlib

def generate_hash(base_string, char_list, hash_prefix, depth, hash_algo):
    
    if depth == 0:
        # Hash the base string
        hash_object = hashlib.new(hash_algo, base_string.encode())

        hash_hex = hash_object.hexdigest()

        # Check if the hash starts with the specified prefix
        if hash_hex.startswith(hash_prefix):
            yield base_string, hash_hex
    else:
        for i, char in enumerate(char_list):
            # Generate combinations with the remaining characters
            new_base = base_string + char
            new_char_list = char_list[:i] + char_list[i+1:]
            yield from generate_hash(new_base, new_char_list, hash_prefix, depth - 1)

# Base string
base = str(input("Enter the base string: "))

# No. of characters missing
depth = int(input("Enter the no. of characters missing: "))

# Hashing algorithm
    # Possible values: "sha224" or "sha256"
hash_algo = str(input("Enter the hashing algorithm (sha224 or sha256): "))

# List of Characters to choose from
    # Possible range: REGEX [a-z0-9_]
    # Also, characters in the word "fail" are not included
chars = "1234567890bcdeghjkmnopqrstuvwxyz_"

# First 6 characters of the hash
hash_prefix = str(input("Enter the hash prefix to check: "))

# Generate and print matching hashes
for string, hash_val in generate_hash(base, chars, hash_prefix, depth, hash_algo):
    print(f"Matching string: {string} -> Hash: {hash_val}")
