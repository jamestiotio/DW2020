def split_sentences(f):
    sentences = []
    lines = f.readlines()
    titles = ["Mr", "Mrs", "Ms", "Dr", "Sr", "Jr"]
    for line in lines:
        i = 0
        for idx, char in enumerate(line):

            if char == "?" or char == "!":
                sentences.append(line[i:idx+1])
                i = idx + 1

            elif char == ".":
                if line[idx+1] == " " and line[idx+2].islower():
                    continue
                if line[idx+1].isdigit():
                    continue
                if line[idx+1] == " " and line[idx+2].isupper() and (line[idx-2:idx] in titles or line[idx-3:idx] in titles):
                    continue
                if line[idx-1].isalpha() and line[idx+1].isalpha():
                    continue
                if line[idx+1] == "," or line[idx+1:idx+3] == ".." or (line[idx-1] == "." and line[idx+1] == "."):
                    continue

                sentences.append(line[i:idx+1])
                i = idx + 1

    return sentences