import random


def cd_keys():
    while True:
        first_segment = "{:03d}".format(random.randint(1, 999))
        if first_segment not in ['333', '444', '555', '666', '777', '888', '999']:
            while True:
                # Generate a 7-digit number
                digits = [random.randint(0, 9) for _ in range(7)]

                # Check if the sum of digits is divisible by 7
                if sum(digits) % 7 == 0:
                    # Check if the last digit is not 0 or ≥ 8
                    if digits[-1] not in [0, 8, 9]:
                        second_segment = ''.join(map(str, digits))
                        return f"{first_segment}-{second_segment}"
            break
print("cd key")
print(cd_keys())
