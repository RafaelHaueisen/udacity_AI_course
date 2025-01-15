check_prime = [26, 39, 51, 53, 57, 79, 85]

for number in check_prime:
    if number == 2:
        print(f"{number} IS a prime number")
        continue
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is NOT a prime number, because {i} is a factor of {number}")
            break
        elif i == number - 1:
            print(f"{number} IS a prime number")