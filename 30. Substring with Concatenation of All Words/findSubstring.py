class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        if len(words[0]) == 0:
            return []
        
        ans = []
        n = len(words)
        m = len(words[0])
        if len(words) == 1:
            for i in range(len(s) - len(words[0]) + 1):
                if s[i:i+len(words[0])] == words[0]:
                    ans.append(i)
            
            return ans
        
        dic = {}
        for v in words:
            if dic.__contains__(v):
                dic[v] += 1
            else:
                dic.update({v:1})

        for i in range(0, len(s) - (n * m) + 1, 1):
            tmp = dict(dic)
            k=n
            j=i
            while k > 0:
                if tmp.__contains__(s[j:j + m]) == False or tmp[s[j:j + m]] < 1:
                    break
                
                tmp[s[j:j + m]] -= 1
                k -= 1
                j += m
            
            if k == 0:
                ans.append(i)
                
        return ans