#!/usr/bin/python3


import sys
import signal

# Dictionary to store the metrics
metrics = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

# Variable to store the total file size
total_file_size = 0

# Counter for the number of lines read
line_count = 0


def compute_metrics(line):
    global metrics, total_file_size, line_count

    try:
        # Split the line into its components
        _, _, _, status_code, file_size = line.split(' ', 4)
        # Update the total file size
        total_file_size += int(file_size)

        # Update the metrics dictionary
        metrics[status_code] = metrics.get(status_code, 0) + 1

        # Increment the line count
        line_count += 1

    except ValueError:
        # Ignore lines that do not match the expected format
        pass


def print_statistics():
    global metrics, total_file_size

    # Print the total file size
    print(f"Total file size: {total_file_size}")

    # Print the number of lines by status code
    for status_code in sorted(metrics.keys()):
        count = metrics[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        # Read a line from stdin
        line = sys.stdin.readline().strip()

        # Compute metrics for the line
        compute_metrics(line)

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
