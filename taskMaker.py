def taskMaker(sourceCopy, challengeId):
    source = sourceCopy
    i = 0
    previousLine = 0
    while i < len(source):
        if "/" in source[i] and str(challengeId) in source[i]:
            source[previousLine] = source[i].split("//")[-1]
        if "/" not in source[i]:
            previousLine = i
        i += 1

    i = 0
    while i < len(source):
        if "//DB" in source[i]:
            del source[i]
            i -= 1
        i += 1

    return source

if __name__ == "__main__":
    source = ["ans = 0",
          "for i in range(n):",
          "    for j in range(n):",
          "    //DB 3//for j in range(1, n):",
          "    //DB 2//for j in range(n + 1):",
          "        ans += 1",
          "return ans"]
    print(taskMaker(source, 3))

            
            
            
