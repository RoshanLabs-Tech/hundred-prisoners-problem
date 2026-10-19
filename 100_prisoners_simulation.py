
import random

def random_strategy(boxes, limit=50):
    for prisoner in range(len(boxes)):
        chosen = random.sample(range(len(boxes)), limit)
        if prisoner not in [boxes[i] for i in chosen]:
            return False
    return True

def cycle_following_strategy(boxes, limit=50):
    for prisoner in range(len(boxes)):
        box = prisoner
        found = False

        for _ in range(limit):
            number = boxes[box]

            if number == prisoner:
                found = True
                break

            box = number

        if not found:
            return False

    return True

def run_simulation(trials=10_000, prisoners=100, limit=50, seed=42):
    random.seed(seed)
    random_successes = 0
    cycle_successes = 0

    for _ in range(trials):
        boxes = list(range(prisoners))
        random.shuffle(boxes)

        if random_strategy(boxes, limit):
            random_successes += 1

        if cycle_following_strategy(boxes, limit):
            cycle_successes += 1

    print(f"100 Prisoners Problem — {trials:,} trials")
    print("-" * 77)
    print(f"{'Strategy':<24}{'Trials':>12}{'Successful':>14}"
          f"{'Observed rate':>16}{'Theory':>11}")
    print("-" * 77)

    print(f"{'Random':<24}{trials:>12,}"
          f"{random_successes:>14,}"
          f"{100 * random_successes / trials:>15.6f}%"
          f"{'~0%':>11}")

    print(f"{'Cycle-following':<24}{trials:>12,}"
          f"{cycle_successes:>14,}"
          f"{100 * cycle_successes / trials:>15.4f}%"
          f"{'31.18%':>11}")

    print("-" * 77)
    print("Random-strategy success is too rare to estimate")
    print("reliably with ordinary trial counts.")

run_simulation()

input()
