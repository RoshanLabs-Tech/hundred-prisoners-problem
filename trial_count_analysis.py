
import random

PRISONERS = 100
MAX_OPENS = 50

TRIAL_COUNTS = [
    100, 500, 1000, 5000, 10000,
    20000, 30000, 40000, 50000,
    60000, 70000, 80000, 90000, 100000
]

def cycle_following():
    slips = list(range(1, PRISONERS + 1))
    random.shuffle(slips)

    for prisoner in range(1, PRISONERS + 1):
        box = prisoner

        for _ in range(MAX_OPENS):
            box = slips[box - 1]

            if box == prisoner:
                break
        else:
            return False

    return True

print("EFFECT OF TRIAL COUNT ON CYCLE-FOLLOWING")
print("-" * 76)
print(f"{'Trials':>10} | {'Successful Trials':>18} | "
      f"{'Observed Rate (%)':>18} | {'Theory (%)':>12}")
print("-" * 76)

for trials in TRIAL_COUNTS:
    successes = 0

    for _ in range(trials):
        if cycle_following():
            successes += 1

    observed_rate = (successes / trials) * 100

    print(f"{trials:>10} | {successes:>18} | "
          f"{observed_rate:>18.4f} | {31.18:>12.2f}")

input()
