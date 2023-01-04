from sys import exit

from search import Search


def run():
    """Binary Search."""
    run = Search()

    try:
        # Starting the game.
        run.start_app()
    except KeyboardInterrupt:
        # Stopping the game.
        exit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
