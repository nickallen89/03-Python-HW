import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    budget_read = csv.reader(csvfile, delimiter=',')

    csv_header = next(budget_read)

    maxVal = 0
    minVal = 0
    months = []
    total = 0
    prevVal = 0
    totalChange = 0
    totalMonths = 0

    for row in budget_read:
        
        totalMonths = totalMonths + 1

        currentVal = float(row[1])

        months.append(row[0])

        total = total + currentVal

        if prevVal != 0:
            change = currentVal - prevVal
            totalChange = totalChange + change

            if change > maxVal:
                maxVal = change
                rowMax = row[0]
            elif change < minVal:
                minVal = change
                rowMin = row[0]

        prevVal = currentVal

    avgChange = totalChange / (len(months) - 1)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${round(total,2)}")
    print(f"Average Change: ${round(avgChange,2)}")
    print(f"Greatest Increase in Profits: {rowMax} ({round(maxVal,2)})")
    print(f"Greatest Decrease in Profits: {rowMin} ({round(minVal,2)})")

    with open("Output.txt", "w") as text_file:
        print("Financial Analysis", file=text_file)
        print("----------------------------", file=text_file)
        print(f"Total Months: {len(months)}", file=text_file)
        print(f"Total: ${round(total,2)}", file=text_file)
        print(f"Average Change: ${round(avgChange,2)}", file=text_file)
        print(f"Greatest Increase in Profits: {rowMax} ({round(maxVal,2)})", file=text_file)
        print(f"Greatest Decrease in Profits: {rowMin} ({round(minVal,2)})", file=text_file)
