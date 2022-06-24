def count_bits(x):
    """
    Count the number of bits set to 1 in an integer.
    """
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

print(5)
print(count_bits(5))