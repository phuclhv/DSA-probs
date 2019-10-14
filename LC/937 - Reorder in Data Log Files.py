import operator

def reorderLogFiles(logs):
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


print(reorderLogFiles(["wda dfu too eow", "kkj dfu too eow", "fqo fiw pok sip", "fvg 231 431 837", "ios 433 347 009"]))
print(reorderLogFiles(['aaa 999 999 999',
  'aaf zzz zzz zzz',
  'aac aaa aaa aaa',
  'dsd 000 111 222',
  'aab aaa aaa aaa',
  'aaa bbb bbb ccc',
  'ddd 123 123 123',
  'aaa ccc bbb bbb']))
print(reorderLogFiles([
   'waa ofu aab aaa',
  'wda ofu aab aaa',
  'wda dfu too aaa',
  'kkj dfu too eow',
  'fvg 231 431 837',
  'fqo fiw pok sip',
  'ios 433 347 009',
  'oip 000 000 000',
  'err 123 aaa 444',
  'aaa aaa aaa aaz',
  'zzz zzz zzz zza']))