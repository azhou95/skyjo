from utils import f, sum_freq, sum_by_freq


def calc_expectation(threshold: int):
    total_cards = sum(f.values())
    e = (sum_freq(-2, threshold) / total_cards) * (sum_by_freq(-2, threshold) / sum_freq(-2, threshold)) + \
        (sum_freq(threshold, 12) / total_cards) * (sum_by_freq(-2, 12) / sum_freq(-2, 12))
    return e


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    thresholds = range(min(f), max(f) + 1)
    vals = [calc_expectation(t) for t in thresholds]

    plt.plot(thresholds, vals)
    plt.show()
