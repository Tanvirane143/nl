c. Accept the input string with Regular expression of FA: (a+b)*bba.

code allows you to accept input strings that follow the regular expression pattern (a+b)*bba.

The regular expression (a+b)*bba can be broken down as follows:
(a+b)*: Zero or more occurrences of either 'a' or 'b'.
bba: The string must end with the sequence 'bba'.

Code :
def FA(s):
    size = 0
    # Scan the complete string and make sure that it contains only 'a' & 'b'
    for i in s:
        if i == 'a' or i == 'b':
            size += 1
        else:
            return "Rejected"

    # After checking that it contains only 'a' & 'b'
    # Check its length, it should be at least 3
    if size >= 3:
        # Check the last 3 elements
        if s[size-3] == 'b':
            if s[size-2] == 'b':
                if s[size-1] == 'a':
                    return "Accepted" # If all 4 conditions are true
                return "Rejected" # Else of 4th if
            return "Rejected" # Else of 3rd if
        return "Rejected" # Else of 2nd if
    return "Rejected" # Else of 1st if

# List of input strings to test
inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', '']

# Iterate over the input strings and print the result of FA for each
for i in inputs:
    print(f"Input: {i} - {FA(i)}")
