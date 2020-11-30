def lambda_handler(event, context):
    # Evaluates whether two numbers are fibonacci nums
    message = evaluate_nums(event, context)
    # Generates log message
    print_to_log(context)

    # generates output on test event
    return {
        'message' : message
    }


def evaluate_nums(event, context):
    my_def = context.function_name
    min_num = event['min_num']
    max_num = event['max_num']
    fibonacci_nums = [0,1] # deals with the irregular start of the sequence
    i = 1

    while i < max_num:
        i += fibonacci_nums[len(fibonacci_nums) - 2]
        fibonacci_nums.append(i)

    if min_num in fibonacci_nums and max_num in fibonacci_nums:
        return f"Yes! {min_num} & {max_num} are valid numbers of the fibonacci sequence"
    elif min_num in fibonacci_nums or max_num in fibonacci_nums:
        return f"Not quite - only one of {min_num}, {max_num} is in the fibonacci sequence..."
    else:
        return f"Sorry...{min_num} & {max_num} are not part of the fibonacci sequence"


def print_to_log(context):
    print(context)
