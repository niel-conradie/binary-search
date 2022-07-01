import time

from search import Search


def run():
    """Naive and Binary Search."""
    run = Search()

    while True:
        # Requesting user input.
        user_input = run.user_input()
        # Generating a sorted list.
        sorted_list = run.generate_list(user_input)

        # Naive search.
        start = time.time()
        for target in sorted_list:
            run.naive_search(sorted_list, target)
        end = time.time()
        print(f"\nNaive search: {(end - start) / user_input} seconds.")

        # Binary search.
        start = time.time()
        for target in sorted_list:
            run.binary_search(sorted_list, target)
        end = time.time()
        print(f"\nBinary search: {(end - start) / user_input} seconds.")

        # Requesting user input.
        run.restart()

        continue


if __name__ == "__main__":
    run()
