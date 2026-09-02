class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = {}
        for i in range(len(s)):
            end[s[i]] = i
        ans = []
        box = []
        size = 0
        for i in range(len(s)):
            size += 1
            if s[i] not in box:
                box.append(s[i])
            if s[i] in box and i == end[s[i]]:
                box.remove(s[i])
            if len(box) == 0:
                ans.append(size)
                size = 0
        return ans

            
            
            

            
