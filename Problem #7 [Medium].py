"""Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed."""

#This problem was asked by Facebook.

def count_decodings(message):
    n = len(message)

    # Create a list to store the number of ways to decode the message up to each index
    dp = [0] * (n + 1)

    # There is one way to decode an empty message
    dp[0] = 1

    # If the first character of the message is '0', it cannot be decoded
    # So, there are zero ways to decode the message
    if message[0] == '0':
        return 0
 
    # There is one way to decode the first character
    dp[1] = 1

    # Iterate through the message starting from the second character
    for i in range(2, n + 1):
        # If the current character is not '0', we can decode it as a single digit
        if message[i - 1] != '0':
            dp[i] = dp[i] + dp[i - 1] #aka dp[i] += dp[i - 1]

        # If the current character and the previous character form a valid two-digit number
        two_digit = int(message[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    # Return the number of ways to decode the entire message
    return dp[n]

message = '11'
ways = count_decodings(message)
print(ways)  # Output: 3


#Sudo code
"""function countDecodings(message):
    n = length of message
    if n == 0:
        return 0
    dp = array of size n+1, initialized with 0s
    dp[0] = 1  # There is one way to decode an empty message
    dp[1] = 1  # There is one way to decode a single-character message
    
    for i = 2 to n:
        if message[i-1] is not '0':  # If the current character is not '0', it can be decoded individually
            dp[i] += dp[i-1]  # Add the count from one character back to the current count
        
        if message[i-2] is '1' or (message[i-2] is '2' and message[i-1] is between '0' and '6'):
            # If the current and previous characters form a valid two-digit encoding
            dp[i] += dp[i-2]  # Add the count from two characters back to the current count
    
    return dp[n]  # The count at index n represents the total number of possible decodings

message = "111"  # example input
ways = countDecodings(message)
print(ways)  # output: 3
"""