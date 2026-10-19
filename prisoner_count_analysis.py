
import random

TRIALS = 10000
PRISONER_COUNTS = range(10, 101, 10)

def cycle_following(n):
    slips = list(range(1, n + 1))
    random.shuffle(slips)

    for prisoner in range(1, n + 1):
        box = prisoner

        for _ in range(n // 2):
            box = slips[box - 1]

            if box == prisoner:
                break
        else:
            return False

    return True

print("EFFECT OF PRISONER COUNT")
print("-" * 76)
print(f"{'Prisoners':>10} | {'Successful Trials':>18} | "
      f"{'Observed Rate (%)':>18} | {'Theory (%)':>12}")
print("-" * 76)

for n in PRISONER_COUNTS:
    successes = 0

    for _ in range(TRIALS):
        if cycle_following(n):
            successes += 1

    observed_rate = successes / TRIALS * 100

    theoretical_rate = (
        1 - sum(1 / k for k in range(n // 2 + 1, n + 1))
    ) * 100

    print(f"{n:>10} | {successes:>18} | "
          f"{observed_rate:>18.4f} | "
          f"{theoretical_rate:>12.4f}")

input()