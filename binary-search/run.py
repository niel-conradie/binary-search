from sys import exit

from search import Search


def run():
    """Binary Search."""
    run = Search()

    try:
        # Starting the application.
        run.start_app()
    except KeyboardInterrupt:
        # Stopping the application.
        exit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
