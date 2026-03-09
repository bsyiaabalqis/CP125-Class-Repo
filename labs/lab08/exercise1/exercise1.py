# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    count = 0
    f = open(input_file, "r")
    f2 = open(output_file, "w")

    # Just read the file line by line
    for line in f:
        # Split "S002 92" into ["S002", "92"]
        split_line = line.split()
        
        # Only process if the line actually had data
        if len(split_line) >= 2:
            student_id = split_line[0]
            score = int(split_line[1])

            if score >= 80:
                f2.write(student_id + " " + str(score) + "\n") 
                count += 1
    
    f.close()
    f2.close()
    return count
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id score per line)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
