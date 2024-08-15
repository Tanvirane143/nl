b. Accept the input string with Regular expression of FA: 101+

allows you to accept input strings that follow the regular expression pattern 101+

Code : 
def FA(s):
    # if the length is less than 3 then it can't be accepted, Therefore end the process.
    if len(s) < 3:
        return "Rejected"

    # first three characters are fixed. Therefore checking them using index
    if s[0] == '1':  # Check if the first character is '1'
        if s[1] == '0':  # Check if the second character is '0'
            if s[2] == '1':  # Check if the third character is '1'

                # After index 2 only "1" can appear. Therefore break the process if any other character is detected
                for i in range(3, len(s)):  # Loop through the remaining characters
                    if s[i] != '1':  # If any character is not '1'
                        return "Rejected"  # Reject the string
                return "Accepted"  # If all characters after the first three are '1', accept the string

    # If any of the conditions fail, return "Rejected"
    return "Rejected"

inputs=['1','10101','101','10111','01010','100','','10111101','1011111']

# Loop through each input string and print whether it is accepted or rejected
#for i in inputs:
#  print(FA(i))

for i in inputs:
    print(f"Input: {i} - {FA(i)}")
