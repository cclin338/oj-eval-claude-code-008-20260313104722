#!/usr/bin/env python3

print("# printf - ASCII to decimal")
print("# Minimal solution with direct output")
print()
print("# Read input")
print("A<I")
print()

# For each ASCII value, create a small dispatch table
# We'll use memory 0-255 to store an action code
# Then based on that, output the appropriate digits

# Actually, simplest approach: pre-compute all and store as 3 bytes
# mem[0-2]: for value 0 (stores '0', 0, 0)
# mem[3-5]: for value 1 (stores '1', 0, 0)
# ...

# This uses 768 bytes, too much!

# Better: Compute on the fly using range checks
# Build tables for digit extraction

# Create hundreds digit table (0-255)
for i in range(256):
    h = i // 100
    if h > 0:
        print(f"[{i}]<{48 + h}")  # Store ASCII digit
    else:
        print(f"[{i}]<0")  # Mark as no hundreds

print()
print("# Get hundreds digit indicator")
print("B<[A]")
print()

# Only output if non-zero
# But we need conditional output...
# Skip hundreds for now, compute tens

# For tens: need (A % 100) / 10
# Create a lookup table: mem[256+V] = (V % 100)
print("# Store V % 100 lookup")
for i in range(256):
    print(f"[{256+i}]<{i % 100}")

print()
print("# Get A mod 100")
print("C<A")
print("C<[256+C]")
print()

# Now we have V%100 in C
# Get tens digit: C / 10
# Need another lookup...

print("# This is getting too large, switching approach")
print("Z<1")
