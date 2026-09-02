class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phonebook = {2 : ["a", "b", "c"], 3 : ["d", "e", "f"], 4 : ["g", "h", "i"], 5:["j", "k", "l"], 6:["m", "n", "o"], 7:["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
        ans = []
        self.helper(0, phonebook, ans, "", digits)
        return ans
    def helper(self, start, phonebook, ans, path, digits):
        if len(digits) == 0:
            return []
        if len(path) == len(digits):
            ans.append(path)
            return
        
        
        number = phonebook[int(digits[start])]
        for j in range(len(number)):
            path = path + number[j]
            print(path)
            self.helper(start + 1, phonebook, ans, path, digits)
            path = path[:-1]