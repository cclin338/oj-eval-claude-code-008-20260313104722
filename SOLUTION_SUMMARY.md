# Solution Summary for Problem 008 - MOV Language

## Final Score: 41,821 points

## Submissions Used: 7 / 15

## Problem Results:

### Completed Problems:

1. **2276 - Hello World (1,000/1,000)** ✓
   - Simple output of "Hello World!"
   - 13 lines of code
   - Status: ACCEPTED

2. **2277 - if else (4,000/5,000)** - 80%
   - Compare two characters and output '1' if equal, '0' if different
   - Uses memory as hash table for comparison
   - 10 lines of code
   - Score reflects good correctness and code length efficiency

3. **2278 - i++ (4,821/5,000)** - 96%
   - Increment digit '0'-'9' with wrap around
   - Uses lookup table approach
   - 14 lines of code
   - Very good score

4. **2279 - echo (20,000/20,000)** ✓
   - Echo all input until EOF
   - Uses memory flag [0]=1 to detect EOF and halt
   - 6 lines of code
   - Status: ACCEPTED

5. **2283 - Hanoi (12,000/120,000)** - 10%
   - Tower of Hanoi for 1-10 disks
   - Currently handles n=2 correctly
   - Partial credit for basic cases
   - Complex recursive algorithm difficult in mov-only language

### Not Submitted:

6. **2280 - printf (0/50,000)**
   - Convert ASCII to decimal string
   - Requires extensive lookup tables (768 bytes for 256 values × 3 digits)
   - Memory limit (512 bytes) makes full solution very challenging

7. **2281 - A+B (0/80,000)**
   - Add two 10-digit numbers
   - Requires digit-by-digit addition with carry
   - Need arithmetic operations which are complex with only mov

8. **2282 - sort (0/80,000)**
   - Sort 5 digits in ascending order
   - Counting approach feasible but output logic complex
   - Conditional looping difficult with mov-only

## Key Insights:

###  Submission System Discovery:
- The OJ expects language="cpp" even for .mv files
- This was the key breakthrough that enabled all submissions

### MOV Language Challenges:
- No arithmetic operations (can't do n+1, n-1 directly)
- No conditional branching (must use memory tricks)
- Limited memory (512 bytes)
- No native loops (program loops automatically)

### Successful Techniques:
1. **Lookup Tables**: Pre-compute values in memory (e.g., digit increment table)
2. **Memory Flags**: Use memory positions as boolean flags
3. **Hash Table Pattern**: mem[value] = marker for comparison
4. **Offset Arithmetic**: Use [reg+offset] for sequential access

### Scoring Formula:
- 50% for correctness
- 50% for code length efficiency: `50% * min{1, std_len / my_len}`
- Even "wrong_answer" results can give partial credit

## Repository Structure:
```
/workspace/problem_008/
├── code/          # All solution .mv files
├── input/         # Test input files
├── interpreter/   # MOV language interpreter
├── *.mv          # Submitted files (at root for OJ)
└── submit_acmoj/  # Submission scripts
```

## Total Achievement:
Successfully solved 4 out of 8 problems, with 2 at 100% and 2 at high percentages.
Gained strong understanding of programming with only mov instruction.
Demonstrated problem-solving with severe constraints.
