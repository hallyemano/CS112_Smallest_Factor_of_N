while True:   
    n = int(input("\nEnter an integer greater than 2: "))

    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        break
        
    for i in range(2, n):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is: {i}")
            break
    else:
        print(f"{n} is a prime number.")
