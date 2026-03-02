# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    count = 0 

    f = open("labs/lab08/exercise2/data/list1.txt", "r")
    list1 = f.readlines()
    f.close()

    f = open("labs/lab08/exercise2/data/list2.txt", "r")
    list2 = f.readlines()
    f.close()

    # combine and remove duplicates
    duplicates = set(list1 + list2)

    # Sort names
    sort = sorted(duplicates)
    count += len(sort)

    # Write sorted names to output file
    f = open("merge.txt", "w")
    for name in sort: 
        f.write(name)
    f.close()
    return count 
    
    """
    Merge two lists of names, remove duplicates, and sort.
    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file
    Returns:
        int: count of unique names
    """

# Test your code here
result = merge_lists("data/list1.txt", "data/list2.txt", "data/merged.txt")
print(f"Unique names: {result}")
