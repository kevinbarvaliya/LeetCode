class Solution:
    
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minn = []
        maxx = []

        for i in matrix:
            minn.append(min(i))
        

        for i in range(len(matrix[0])):
            mx = matrix[0][i]
            for j in range(len(matrix)):
                if mx < matrix[j][i]:
                    mx = matrix[j][i]
                
            maxx.append(mx)
        
        for i in minn:
            if i in maxx:
                return [i]
            
           
