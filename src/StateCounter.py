# to count number of state per loop


class StateCounter:
    def __init__(self):
        self.data = []
        self.loopCount = 0

    def record(self, stateContainer):
        self.data.append((self.loopCount, len(stateContainer)))
        self.loopCount += 1

    def report(self):
        step = 0
        if len(self.data) < 100:
            step = 10
        elif len(self.data) < 1000:
            step = 100
        else:
            step = 1000

        dataReport = []
        for i in range(0, len(self.data), step):
            dataReport.append(self.data[i])

        # append the last record if necessary
        if not (dataReport[len(dataReport)-1][0] == self.data[len(self.data)-1][0]):
            dataReport.append(self.data[len(self.data)-1])

        return dataReport