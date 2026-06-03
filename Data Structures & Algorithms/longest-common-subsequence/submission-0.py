class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) , len(text2) 
        word_matrix = [[0 for j in range(cols +1)] for i in range(rows +1)]

        for i in range(rows -1,  -1, -1):
            for j in range(cols-1, -1, -1):
                if text1[i] == text2[j]:
                    #its the sum of 1 + its diagonal
                    word_matrix[i][j] = 1 + word_matrix[i+1][j+1]

                else:
                    #we take the max of right and bottom
                    word_matrix[i][j] = max(word_matrix[i+1][j],word_matrix[i][j+1])

        return word_matrix[0][0]

