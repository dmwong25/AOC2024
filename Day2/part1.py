with open("day2/day2_input.txt", "r") as file:
    input_data = file.readlines()

correct = 0

for string_list in input_data:
    line = list(map(int, string_list.split()))  # Convert the line to a list of integers

    if len(line) < 2:  # Skip lines with fewer than 2 numbers
        continue

    # Determine the initial trend (increasing or decreasing)
    diff = line[1] - line[0]
    if diff > 0:
        ante = 1  # Increasing
    elif diff < 0:
        ante = -1  # Decreasing
    else:
        continue  # Skip if the first two numbers are the same

    is_valid = True  # Assume the sequence is valid

    # Check the entire sequence
    for i in range(1, len(line)):
        current_diff = line[i] - line[i - 1]

        # Check if the difference is within bounds
        if not (1 <= abs(current_diff) <= 3):
            is_valid = False
            break

        # Check monotonicity based on `ante`
        if ante == 1 and current_diff <= 0:  # Increasing sequence must strictly increase
            is_valid = False
            break
        elif ante == -1 and current_diff >= 0:  # Decreasing sequence must strictly decrease
            is_valid = False
            break

    if is_valid:
        correct += 1  # Increment the count of valid sequences

print(correct)
