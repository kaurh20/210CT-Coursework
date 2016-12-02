def longestIncreasingSubsequence(n):

    
    longestSequence= []
    for i in range(len(n)):
        longestSequence.append(max([longestSequence[j] for j in range(i) if longestSequence[j][-1] < n[i]] or [[]], key=len) 
                  + [n[i]])
    return max(longestSequence, key=len)
 
if __name__ == '__main__':
    for n in [[4,5,9,8,7,11,16,17]]:

        print('longest sub sequence of %s is %s' % (n, longestIncreasingSubsequence(n)))



