import time

sec = 64852
type_result = time.gmtime(sec)
result = time.strftime("%H:%M:%S",type_result)
print(result)
