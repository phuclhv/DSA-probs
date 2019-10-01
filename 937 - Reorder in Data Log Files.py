class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        idx = 0
        for log in logs:
            firstBlankPos = log.find(' ')
            if log[firstBlankPos + 1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append([log[firstBlankPos:], log[0:firstBlankPos], idx])
            idx += 1

        letterLogs.sort(key = operator.itemgetter(0, 1))

        finalLogs = []
        for log in letterLogs:
            finalLogs.append(logs[log[2]])
        for log in digitLogs:
            finalLogs.append(log)

        return finalLogs