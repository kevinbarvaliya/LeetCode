class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0]*len(colSum) for i in range(len(rowSum))]
        
        i = 0
        j = 0
        print(ans)
        while(j< len(colSum) and i < len(rowSum)):
            
            x = min(rowSum[i],colSum[j])
            ans[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
            if rowSum[i] == 0: i += 1
            if colSum[j] == 0: j += 1
            
        return ans
