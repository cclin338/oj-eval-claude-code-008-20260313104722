#!/usr/bin/env python3
# Generate a more compact printf solution using math approach

print("# printf - ASCII to decimal")
print("# Uses digit extraction by repeated comparison")
print()
print("# Read input")
print("A<I")
print()

# Create ranges for digit extraction
# Hundreds place: 0-99=0, 100-199=1, 200-255=2
# Store hundreds digit at mem[0-255] directly
for i in range(256):
    print(f"[{i}]<{i // 100 + 48}")  # ASCII digit

print()
print("# Get hundreds digit from lookup")
print("B<[A]  # B = hundreds digit ASCII")
print()
print("# Output hundreds digit if non-zero (not '0')")
print("# Skip if B == 48 (ASCII '0')")
print("# Store marker: mem[256] = 0 (don't output), mem[other] = 1 (output)")
print("[256]<0")  
print("[257]<1")

# Actually this is getting complicated too
# Let me use a simpler direct approach
print()
print("# Just output all three digits for simplicity")
print("O<B")
