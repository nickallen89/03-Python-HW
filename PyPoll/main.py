import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    poll_read = csv.reader(csvfile, delimiter=',')

    csv_header = next(poll_read)

    voteTotal = 0
    voteKhan = 0
    voteCorrey = 0
    voteLi = 0
    voteOTooley = 0

    for rows in poll_read:
        
        voteTotal = voteTotal + 1

        if rows[2] == 'Khan':
            voteKhan = voteKhan + 1
        elif rows[2] == 'Correy':
            voteCorrey = voteCorrey + 1
        elif rows[2] == 'Li':
            voteLi = voteLi + 1
        elif rows[2] == "O'Tooley":
            voteOTooley = voteOTooley + 1

percentKhan = voteKhan / voteTotal * 100
percentCorrey = voteCorrey / voteTotal * 100
percentLi = voteLi / voteTotal * 100
percentOTooley = voteOTooley / voteTotal * 100

if voteKhan > voteCorrey:
    if voteKhan > voteLi:
        if voteKhan > voteOTooley:
            winner = "Khan"
        else:
            winner = "O'Tooley"
    elif voteKhan > voteOTooley:
        winner = "Li"
else:
    if voteCorrey > voteLi:
        if voteCorrey > voteOTooley:
            winner = "Correy"
        else:
            winner = "O'Tooley"
    elif voteCorrey > voteOTooley:
        winner = "Li"
        
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voteTotal}")
print("-------------------------")
print(f"Khan: {round(percentKhan, 3)}% ({voteKhan})")
print(f"Correy: {round(percentCorrey, 3)}% ({voteCorrey})")
print(f"Li: {round(percentLi, 3)}% ({voteLi})")
print(f"O'Tooley: {round(percentOTooley, 3)}% ({voteOTooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("Output.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {voteTotal}", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Khan: {round(percentKhan, 3)}% ({voteKhan})", file=text_file)
    print(f"Correy: {round(percentCorrey, 3)}% ({voteCorrey})", file=text_file)
    print(f"Li: {round(percentLi, 3)}% ({voteLi})", file=text_file)
    print(f"O'Tooley: {round(percentOTooley, 3)}% ({voteOTooley})", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print("-------------------------", file=text_file
