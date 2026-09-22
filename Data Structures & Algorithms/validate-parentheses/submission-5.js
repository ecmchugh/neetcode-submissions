class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const seen = new Set();
        ['(', '{', '['].forEach(x => seen.add(x));
        const stack = [];
        for (const letter of s) { 
            if (seen.has(letter)) { 
                stack.push(letter);
            } else { 
                if (stack[stack.length-1] === '(' && letter === ')') { 
                    stack.pop()
                } else if (stack[stack.length-1] === '{' && letter === '}') {
                    stack.pop()
                } else if (stack[stack.length-1] === '[' && letter === ']') { 
                    stack.pop()
                } else {
                    return false;
                }
            }
        }
        return stack.length === 0;
    }
}
