#!/usr/bin/env python3
# Generate lookup table for printf problem

print("# printf - ASCII to decimal conversion")
print("# Read character and output its ASCII code")
print()
print("# Read input")
print("A<I")
print()

# We'll create a lookup table structure
# For each ASCII value, we need to store where its decimal string starts
# Strategy: Use memory 300+ for strings, 0-255 for pointers

# Build the decimal strings in memory starting at position 300
pos = 300
pointer_map = {}

for ascii_val in range(256):
    decimal_str = str(ascii_val)
    pointer_map[ascii_val] = pos
    
    # Store each digit at consecutive positions
    for digit_char in decimal_str:
        print(f"[{pos}]<{ord(digit_char)}")
        pos += 1
    # Store a 0 terminator
    print(f"[{pos}]<0")
    pos += 1

print()
print("# Store pointers for each ASCII value")
for ascii_val in range(256):
    print(f"[{ascii_val}]<{pointer_map[ascii_val]}")

print()
print("# Now use A as index to get pointer")
print("B<[A]")
print()
print("# Output characters from position B until we hit 0")
print("# Use C as the character to output")
print("C<[B]")
print("O<C")
print("# Increment B and continue if C != 0")
print("# But we need to check...")
print("# Initialize halt lookup: mem[256] = 0, others = something else")
print("# Actually, let me simplify...")
print()
print("Z<1  # Halt after outputting")

