def count_substring(string, sub_string):
    result = 0
    ofset = -1
    while True:
     ofset = string.find(sub_string, ofset + 1)
     if ofset >= 0:
         result += 1
     else:
         break
    return result

