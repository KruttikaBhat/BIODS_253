import sys

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def pascal(n):
    for i in range(n):
        i_fact=factorial(i)
        for(j) in range(i+1):
            j_fact=factorial(j)
            diff_fact=factorial(i-j)
            i_choose_j=int(i_fact/(j_fact*diff_fact))
            print(i_choose_j, end=" ")
        print("\n")

# accept number of lines from command line argument
if len(sys.argv) != 2:
    print("Enter python pascal.py <number_of_lines>")
    sys.exit(1)
num_lines = int(sys.argv[1])
pascal(num_lines)
