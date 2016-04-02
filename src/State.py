# class nay dung de luu ve trang thai hien tai cua bai toan
# jug1, jug2 la cai to dung de giai bai toan water-jug


class State:
    def __init__(self, mapp):
        self.mapp = mapp
        self.parent = None
        self.height = 0

    def setParent(self, parent):
        self.parent = parent
        self.height = self.parent.height + 1

    def __eq__(self, other):
        return self.mapp == other.mapp

    def __hash__(self):
        return hash(str(self.mapp))