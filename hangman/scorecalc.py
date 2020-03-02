def scorecalc(fguess,ftable):
    letters = len(set(ftable))
    score =  fguess * letters
    return score
