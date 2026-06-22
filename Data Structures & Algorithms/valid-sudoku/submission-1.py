class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValid(board[i]):
                print(1)
                return False
        
        for j in range(9):
            col_list = [row[j] for row in board]
            if not self.isValid(col_list):
                return False
        
        for i in range(3):
            for j in range(3):
                sub_mat = [row[3*j:3*j+3] for row in board[3*i:3*i+3]]
                flat_mat = []
                for row in sub_mat:
                    for k in row:
                        flat_mat.append(k)
                if not self.isValid(flat_mat):
                    print(3)
                    return False


                
        return True
    
    def isValid(self, myList):
        counter = 0
        mySet = set()
        for j in myList:
            if j != ".":
                counter += 1
                mySet.add(j)
        return len(mySet) == counter



        