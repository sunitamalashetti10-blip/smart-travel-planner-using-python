# Smart Travel Planner

Smart Travel Planner is a beginner-friendly Python console program that estimates
the cost of a trip. It uses only Python built-in features: variables, basic data
types, `input()`, type conversion, a dictionary, functions, parameters, return
values, arithmetic operations, validation, and formatted output.

## What the program collects

- Travel name and destination
- Number of travelers and travel days
- Transportation cost per traveler
- Hotel cost per day
- Food cost per traveler per day
- Activity cost per traveler

The food input is included because a food total is one of the requested results.
All cost values may be zero but cannot be negative. The number of travelers and
travel days must be greater than zero.

## Calculations

The program uses separate functions for each major calculation:

- Total transportation cost = transportation cost per traveler x travelers
- Total hotel cost = hotel cost per day x travel days
- Total food cost = food cost per traveler per day x travelers x travel days
- Total activity cost = activity cost per traveler x travelers
- Overall trip cost = transportation + hotel + food + activities
- Cost per traveler = overall trip cost / travelers
- Average daily cost = overall trip cost / travel days

Related travel inputs and calculated costs are organized in dictionaries. The
program does not use a database, files, APIs, external libraries, or classes.

## Run the program

From this folder, run:

```text
python smart_travel_planner.py
```

After entering the requested information, the program displays a formatted trip
summary with each cost and the overall totals.