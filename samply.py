def shortestDistance( s, word1, word2):
    # code here
    min_dist = len(s)
    cur_one = -1
    cur_two = -1
    for index in range(len(s)):
        if(s[index] == word1):
            cur_one = index
            if(cur_two!=-1 and abs(cur_two-cur_one)<min_dist):
                min_dist = abs(cur_two-cur_one)
        if(s[index] == word2):
            cur_two = index
            if(cur_one!=-1 and cur_two-cur_one<min_dist):
                min_dist = cur_two-cur_one
    return min_dist

s = ["geeks", "for", "geeks", "contribute", 
     "practice"]

w1 = "contribute"
w2 = "geeks"
result = shortestDistance(s,w1,w2)
print(f"result: {result}")
