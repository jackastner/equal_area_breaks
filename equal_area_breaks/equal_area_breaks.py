import numpy as np
import mapclassify.classifiers as mc

class Equal_Area_Greedy(mc.MapClassifier):
    # y must be a list with elements of type {'area': a, 'value': v}
    def __init__(self, y, area=None, k=mc.K):
        if area is None:
            raise ValueError("area kwarg must be supplied")

        self.k = k
        self.area = area
        super().__init__(y)
        self.name = 'Equal Area Greedy'

    def _set_bins(self):
        # sort values and area array using value as key
        sort_order = np.argsort(self.y)
        ordered_area = np.asarray(self.area)[sort_order]#self.area.values[sort_order]
        ordered_values = self.y[sort_order]

        # compute goal chunk size
        average_chunk = sum(self.area) / self.k

        # take chunks from ordered arrays such that the sum
        # of areas in the chunk is at least the goal size
        bins = []
        chunk_area = 0
        for area, value in zip(ordered_area, ordered_values):
            chunk_area += area
            if chunk_area >= average_chunk:
                bins.append(value)
                chunk_area = 0

        bins.append(ordered_values[-1])

        self.bins = np.array(bins)

setattr(mc, Equal_Area_Greedy.__name__, Equal_Area_Greedy)
mc.CLASSIFIERS = mc.CLASSIFIERS + (Equal_Area_Greedy.__name__,)

class Equal_Area_Greedy2(mc.MapClassifier):
    # y must be a list with elements of type {'area': a, 'value': v}
    def __init__(self, y, area=None, k=mc.K):
        if area is None:
            raise ValueError("area kwarg must be supplied")

        self.k = k
        self.area = area
        super().__init__(y)
        self.name = 'Equal Area Greedy 2'

    def _set_bins(self):
        # sort values and area array using value as key
        sort_order = np.argsort(self.y)
        ordered_area = np.asarray(self.area)[sort_order]#self.area.values[sort_order]
        ordered_values = self.y[sort_order]

        # compute goal chunk size
        average_chunk = sum(self.area) / self.k

        bins = []
        total_area = 0
        for area, value in zip(ordered_area, ordered_values):
            total_area += area
            if total_area >= average_chunk * (len(bins) + 1):
                bins.append(value)

        bins.append(ordered_values[-1])

        self.bins = np.array(bins)

setattr(mc, Equal_Area_Greedy2.__name__, Equal_Area_Greedy2)
mc.CLASSIFIERS = mc.CLASSIFIERS + (Equal_Area_Greedy2.__name__,)

# Super class for defining other classifiers that function by computing index of breaks
# Rather than constructing bins directly
class Break_Idx_Classifier(mc.MapClassifier):


class Equal_Area_DP(mc.MapClassifier):
    def __init__(self, y, area=None, k=mc.K):
        if area is None:
            raise ValueError("area kwarg must be supplied")

        self.k = k
        self.area = area
        super().__init__(y)
        self.name = 'Equal Area Dynamic Programming'

    def _resolve_break_links(self, breaks, links):
        self.bins = []
        r, c = breaks.shape 
        r -= 1
        c -= 1
        while r > 0 and c > 0:
            self.bins.insert(0, breaks[r, c])
            r, c = links[r, c]
            r = int(r)
            c = int(c)

        self.bins = np.array(self.bins)

    def _set_bins(self):
        # sort values and area array using value as key
        sort_order = np.argsort(self.y)
        ordered_area = np.asarray(self.area)[sort_order]#self.area.values[sort_order]
        ordered_values = self.y[sort_order]

        break_idxs = dpOptimalEqualAreaBreaks(ordered_area.tolist(), self.k)
        break_idxs = list(map(lambda i : i - 1, break_idxs))
        self.bins = np.append(ordered_values[break_idxs], [ordered_values[-1]])

setattr(mc, Equal_Area_DP.__name__, Equal_Area_DP)
mc.CLASSIFIERS = mc.CLASSIFIERS + (Equal_Area_DP.__name__,)

class Equal_Area_Weighted_DP(mc.MapClassifier):
    def __init__(self, y, area=None, w=0.5, k=mc.K):
        if area is None:
            raise ValueError("area kwarg must be supplied")

        self.k = k
        self.area = area
        self.w = w
        super().__init__(y)
        self.name = 'Equal Area Weighted Dynamic Programming (W = ' + str(w) + ')'

    def _resolve_break_links(self, breaks, links):
        self.bins = []
        r, c = breaks.shape 
        r -= 1
        c -= 1
        while r > 0 and c > 0:
            self.bins.insert(0, breaks[r, c])
            r, c = links[r, c]
            r = int(r)
            c = int(c)

        self.bins = np.array(self.bins)

    def _set_bins(self):
        # sort values and area array using value as key
        sort_order = np.argsort(self.y)
        ordered_area = np.asarray(self.area)[sort_order]
        ordered_values = self.y[sort_order]

        break_idxs = dpOptimalWeightedEqualAreaBreaks(ordered_area.tolist(), self.k, self.w)
        break_idxs = list(map(lambda i : i - 1, break_idxs))
        self.bins = np.append(ordered_values[break_idxs], [ordered_values[-1]])

setattr(mc, Equal_Area_Weighted_DP.__name__, Equal_Area_Weighted_DP)
mc.CLASSIFIERS = mc.CLASSIFIERS + (Equal_Area_Weighted_DP.__name__,)

class PSums:
    def __init__(self, nums):
        self.sums = [0]
        s = 0
        for x in nums:
            s = s + x
            self.sums.append(s)

    def sum(self):
        return self.sums[-1]

    def nth_sum(self, n):
        return self.sums[n]

    def inner_sum(self, i, j):
        return self.sums[j] - self.sums[i]

def dpOptimalEqualAreaBreaks(numbers, k):
    psum = PSums(numbers)

    avg = psum.sum() / k

    best_error = [[None for _ in range(0,k)] for _ in range(0, len(numbers) + 1)]
    best_breaks = [[None for _ in range(0,k)] for _ in range(0, len(numbers) + 1)]

    for m in range(0, len(numbers) + 1):
        best_error[m][0] = abs(psum.nth_sum(m) - avg)
        best_breaks[m][0] = []

    for b in range(1, k):
        m = len(numbers)
        break_idx = len(numbers)
        while m >= 0:
            if break_idx > m:
                break_idx = m

            while psum.inner_sum(break_idx, m) < avg and break_idx > 0:
                break_idx -= 1

            if (best_error[break_idx + 1][b - 1] + abs(psum.inner_sum(break_idx + 1, m) - avg)) < (best_error[break_idx][b - 1] + abs(psum.inner_sum(break_idx, m) - avg)):
                break_idx += 1

            best_error[m][b] = best_error[break_idx][b - 1] + abs(psum.inner_sum(break_idx, m) - avg)
            best_breaks[m][b] = best_breaks[break_idx][b - 1] + [break_idx]

            m -= 1

    return best_breaks[len(numbers)][k - 1]

def dpOptimalWeightedEqualAreaBreaks(numbers, k, w):
    psum = PSums(numbers)

    avg = psum.sum() / k
    avg_len = len(numbers) / k

    best_error = [[None for _ in range(0,k)] for _ in range(0, len(numbers) + 1)]
    best_breaks = [[None for _ in range(0,k)] for _ in range(0, len(numbers) + 1)]

    for m in range(0, len(numbers) + 1):
        best_error[m][0] = (1 - w) * abs((psum.nth_sum(m) - avg) / psum.sum()) ** 2 + w * abs((m - avg_len) / len(numbers))  ** 2
        best_breaks[m][0] = []

    for b0 in range(1, k):
        for m in range(0, m+1):
            min_error = None
            best_break = None

            for b1 in range(0, m+1):
                break_error = best_error[b1][b0 - 1] + (1 - w) * abs((psum.inner_sum(b1,m) - avg) / psum.sum()) ** 2 + w * abs(((m - b1) - avg_len) / len(numbers))  ** 2

                if min_error is None or break_error < min_error:
                    min_error = break_error
                    best_break = b1

            best_error[m][b0] = min_error
            best_breaks[m][b0] = best_breaks[best_break][b0 - 1] + [best_break]

    return best_breaks[len(numbers)][k - 1]
