from utils import f, sum_freq, sum_by_freq


def calc_expectation(threshold: int, seen_card: int):
    total_cards = sum(f.values())
    if seen_card <= threshold:
        return seen_card

    e = ((sum_by_freq(-2, 12) - seen_card) / sum_freq(-2, 12) - 1)
    return e


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    thresholds = range(min(f), max(f) + 1)
    vals = [calc_expectation(t, 12) for t in thresholds]

    plt.plot(thresholds, vals)
    plt.show()
