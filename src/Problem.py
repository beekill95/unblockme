# class nay de mo ta bai toan minh can giai
# cac du lieu chua trong class nay se duoc aiplayer doc ra va chua vao class nay
# class co ham isGoalState de kiem tra xem trang thai hein tai la trang thai de chien thang hay khong
# class co ham generateNextStates de sinh ra tat ca cac trang thai co the co tu trang thai hien tai
from State import State


class Problem:
    def __init__(self, startState):
        self.startState = startState

    def copyArray(self, cpArray):
        result = [["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
        for i in range(0, 6):
            for j in range(0, 6):
                result[i][j] = cpArray[i][j]
        return result

    def isGoalState(self, state):
        for i in range(0, 6):
            for j in range(0, 6):
                if state.mapp[i][j] == '8':
                    if j == 4:
                        return True
                    for k in range(j+2, 6):
                        if state.mapp[i][k] != '0':
                            return False
                    return True

    def generateNextStates(self, state):
        states = []
        for i in range(0, 6):
            for j in range(0, 6):
                if state.mapp[i][j] == '0':
                    if j <= 3:
                        mapp2 = self.copyArray(state.mapp)
                        if mapp2[i][j+1] == '1' or mapp2[i][j+1] == '8':
                            if mapp2[i][j+1] == '8':
                                mapp2[i][j] = '8'
                                mapp2[i][j+1] = '9'
                                mapp2[i][j+2] = '0'
                            elif mapp2[i][j+2] == '2':
                                mapp2[i][j] = '1'
                                mapp2[i][j+1] = '2'
                                mapp2[i][j+2] = '0'
                            else:
                                mapp2[i][j] = '1'
                                mapp2[i][j+1] = '3'
                                mapp2[i][j+2] = '2'
                                mapp2[i][j+3] = '0'
                            states.append(State(mapp2))
                    if i <= 3:
                        mapp2 = self.copyArray(state.mapp)
                        if mapp2[i+1][j] == '4':
                            if mapp2[i+2][j] == '5':
                                mapp2[i][j] = '4'
                                mapp2[i+1][j] = '5'
                                mapp2[i+2][j] = '0'
                            else:
                                mapp2[i][j] = '4'
                                mapp2[i+1][j] = '6'
                                mapp2[i+2][j] = '5'
                                mapp2[i+3][j] = '0'
                            states.append(State(mapp2))
                    if j >= 2 :
                        mapp2 = self.copyArray(state.mapp)
                        if mapp2[i][j-1] == '2' or mapp2[i][j-1] == '9':
                            if mapp2[i][j-1] == '9':
                                mapp2[i][j] = '9'
                                mapp2[i][j-1] = '8'
                                mapp2[i][j-2] = '0'
                            elif mapp2[i][j-2] == '1':
                                mapp2[i][j] = '2'
                                mapp2[i][j-1] = '1'
                                mapp2[i][j-2] = '0'
                            else:
                                mapp2[i][j] = '2'
                                mapp2[i][j-1] = '3'
                                mapp2[i][j-2] = '1'
                                mapp2[i][j-3] = '0'
                            states.append(State(mapp2))
                    if i >= 2 :
                        mapp2 = self.copyArray(state.mapp)
                        if mapp2[i-1][j] == '5':
                            if mapp2[i-2][j] == '4':
                                mapp2[i][j] = '5'
                                mapp2[i-1][j] = '4'
                                mapp2[i-2][j] = '0'
                            else:
                                mapp2[i][j] = '5'
                                mapp2[i-1][j] = '6'
                                mapp2[i-2][j] = '4'
                                mapp2[i-3][j] = '0'
                            states.append(State(mapp2))
        return states