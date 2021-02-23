def process_scores(f):
    scores = [float(score) for score in f.readline().split(" ")]

    return (sum(scores), sum(scores)/len(scores))