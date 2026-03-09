# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.
    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file
    Returns:
        int: count of unique names
    """
    count = 0 

    f = open(file1, "r")
    list1 = [line.strip() for line in f.readlines()]
    f.close()

    f2 = open(file2, "r")
    list2 = [line.strip() for line in f2.readlines()]
    f2.close()

    output = open(output_file, "w")

    # combine and remove duplicates
    duplicates = set(list1 + list2)

    # Sort names
    sort = sorted(duplicates)
    count = len(sort)

    # Write sorted names to output file
    for name in sort: 
        output.write(name + '\n')

    output.close()
    return count

# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt","labs/lab08/exercise2/data/list2.txt","labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
