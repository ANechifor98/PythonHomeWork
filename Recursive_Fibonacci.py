def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))
    
if __name__ == "__main__":
    nums = int(input("How many numbers? "))
    if nums <= 0:
       print("Plese enter a positive number")
    else:
       print("Fibonacci sequence:")
    for i in range(nums):
       print(recursive_fibonacci(i))
