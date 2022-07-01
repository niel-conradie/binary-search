import random


class Search:
    """A class to represents a naive and binary search."""

    @staticmethod
    def user_input():
        """Requesting user input and validating number."""
        while True:
            try:
                user_input = int(input("\nEnter the length of the list: "))
                return user_input
            except ValueError:
                print("\nThat is not a number.")
                continue

    @staticmethod
    def generate_list(user_input):
        """Generates a sorted list."""
        sorted_list = set()
        while len(sorted_list) < user_input:
            sorted_list.add(random.randint(-3 * user_input, 3 * user_input))
        sorted_list = sorted(list(sorted_list))
        return sorted_list

    @staticmethod
    def naive_search(sorted_list, target):
        """Verifying each element in the list."""
        for index in range(len(sorted_list)):
            if sorted_list[index] == target:
                return index
        return -1

    def binary_search(self, sorted_list, target, low=None, high=None):
        """Divide and Conquer algorithm."""
        # Parameter conditions.
        if low is None:
            low = 0
        if high is None:
            high = len(sorted_list) - 1
        if high < low:
            return -1

        # Calculate middle point.
        mid_point = (low + high) // 2

        if sorted_list[mid_point] == target:
            return mid_point
        elif target < sorted_list[mid_point]:
            return self.binary_search(sorted_list, target, low, mid_point - 1)
        else:
            return self.binary_search(sorted_list, target, mid_point + 1, high)

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nRestart? Yes/No: ").lower()
            choices = ["yes", "no"]
            if user_input not in choices:
                print("\nPlease type 'yes' or 'no'")
                continue

            # User input conditions.
            if user_input == "yes":
                return
            if user_input == "no":
                print("\nThank you!")
                quit()
