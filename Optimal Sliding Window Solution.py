'''
In HashMap, we keep each character as a key and frequency of the characters as a value.

Every time we find a character, add 1 frequency to HashMap. 
Since this question requires us to find the longest substring without repeating characters, so if we have more than 2 frequency of the current character, 
we add -1 to HashMap until we have 1 frequency of the current character and move left pointer to the next at the same time.
Now just compare max length using,

max_length = max(max_length, right - left + 1)

Try to do manual calculations and dry run the code for the testcases.

'''
def lengthOfLongestSubstring(s):
        max_length = left = 0
        count = {}

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
        
            max_length = max(max_length, right - left + 1)

        return max_length
