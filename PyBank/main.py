# Import CSV file and set path to file
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    budget_read = csv.reader(csvfile, delimiter=',')

    # Skip header
    csv_header = next(budget_read)

    #set variables
    maxVal = 0
    minVal = 0
    months = []
    total = 0
    prevVal = 0
    totalChange = 0
    totalMonths = 0

    # Run through data
    for row in budget_read:
        # Add to the total month counter
        totalMonths = totalMonths + 1

        # Store this row's profit/loss value
        currentVal = float(row[1])

        # Store month values in a series
        months.append(row[0])

        # Add current profit/loss to the total
        total = total + currentVal

        # Determine the magnitude of change
        if prevVal != 0:
            change = currentVal - prevVal
            totalChange = totalChange + change

            # Store max/min changes and their row value for reference later
            if change > maxVal:
                maxVal = change
                rowMax = row[0]
            elif change < minVal:
                minVal = change
                rowMin = row[0]

        # Store current profit/loss for use in next loop
        prevVal = currentVal

    # Calculate the average change
    avgChange = totalChange / (len(months) - 1)

    # Display results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${round(total,2)}")
    print(f"Average Change: ${round(avgChange,2)}")
    print(f"Greatest Increase in Profits: {rowMax} ({round(maxVal,2)})")
    print(f"Greatest Decrease in Profits: {rowMin} ({round(minVal,2)})")

    # Export results
    with open("Output.txt", "w") as text_file:
        print("Financial Analysis", file=text_file)
        print("----------------------------", file=text_file)
        print(f"Total Months: {len(months)}", file=text_file)
        print(f"Total: ${round(total,2)}", file=text_file)
        print(f"Average Change: ${round(avgChange,2)}", file=text_file)
        print(f"Greatest Increase in Profits: {rowMax} ({round(maxVal,2)})", file=text_file)
        print(f"Greatest Decrease in Profits: {rowMin} ({round(minVal,2)})", file=text_file)
