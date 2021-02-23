def interlock(word1, word2, word3):
    if (not word1) or (not word2) or (not word3):
        return False

    interlocked = ""

    for i in range(len(min([word1, word2], key=len))):
        interlocked += (word1[i] + word2[i])

    if word3 == (interlocked + max([word1, word2], key=len)[len(min([word1, word2], key=len)):]):
        return True

    return False