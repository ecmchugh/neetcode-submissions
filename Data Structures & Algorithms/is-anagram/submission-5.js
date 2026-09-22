class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let sMap = new Map();

        for (const letter of s) { 
            sMap.set(letter, (sMap.get(letter) || 0) + 1);
        }

        for (const letter of t) { 
            sMap.set(letter, (sMap.get(letter) || 0) - 1);
        }

        for (const count of sMap.values()) { 
            if (count != 0) { 
                return false;
            }
        }
        return true;
    }
}
