# Read the number of triples
N = int(input())

for _ in range(N):
    # Read the three numbers in a triplet
    a, b, c = map(int, input().split())
    
    # Find the second-maximum number among the three
    second_max = sorted([a, b, c])[1]
    
    # Print the second-maximum number
    print(second_max)
