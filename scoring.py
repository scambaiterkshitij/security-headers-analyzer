def calculate_score(header_results):
    total = len(header_results)
    present = sum(header_results.values())

    score = int((present / total) * 100)
    return score
