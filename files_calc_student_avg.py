import csv

'''
Student Scores CSV

Jacob,84,94,91
Michael,86,98,100
Joshua,94,88,90
Matthew,84,85,88
Daniel,80,92,80
Christopher,89,93,96
Andrew,93,91,92
'''

def main():
    student_scores_infile = open('student_scores.csv', 'r') # Reading customer.csv file
    csv_reader = csv.reader(student_scores_infile)

    student_scores_outfile = open('student_avg.csv', 'w', newline='') #create new file 'custoemr_country.csv' (newline is to create any empty spaces in between)
    csv_writer = csv.writer(student_scores_outfile)
    
    for line in csv_reader:
        student = [line[0], round( ( int(line[1]) + int(line[2]) + int(line[3]) )/3, 2)]
        csv_writer.writerow(student)

    student_scores_infile.close()

main()