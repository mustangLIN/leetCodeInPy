class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        i = 0
        j = 0
        ans = 0
        # sliding window [i,j]
        for c in s:
            # if new char duplicate
            if c in dic:
                #update i to old char next index, str"abba", len(abb)==len(bba)
                i = max(dic[c] + 1, i)
            # (length record, sliding window length calculate)
            ans = max(ans, j - i + 1)
            #  storage char max index
            dic[c] = j
            j = j + 1
        return ans