class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0;
        let profit = 0;
        for (let r = 0; r < prices.length; r++) { 
            if (prices[r] > prices[l]) { 
                profit = Math.max(profit, (prices[r] - prices[l]));
            } else { 
                l = r;
            }
        }
        return profit;
    }
}
