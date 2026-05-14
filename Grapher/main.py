# ----- IMPORTS ----- #
from turtle import bye
from functionManager import formatFunction, createTable
from graphManager import initialiseGraph, plotFunction
from calculationsManager import *

# ----- VARIABLES ----- #
FunctionList = [] 

# ----- FUNCTIONS ----- #
# Formatter for displaying values in calculations
def formatter(val):
    if val == int(val):         # If the value is an integer, display it without decimal places
        return str(int(val))    # Otherwise, display it with 2 decimal places
    return f"{val:.2f}"         # Format the value to 2 decimal places


# Creates a function based on user input and adds it to the FunctionList
def CreateFunction():
    print("Function type: 1. Linear  2. Quadratic") # Linear or quadratic
    ftype = input("Choice: ").strip() # Get the function type from the user

    # Linear function
    if ftype == "1":
        # Get a and b coefficients from the user
        print("Input a and b like this: a, b")
        a, b = map(float, map(str.strip, input().split(","))) # Split by comma, strip whitespace, and convert to float
        coeffs = (a, b) # Store them in a tuple

    # Quadratic function
    elif ftype == "2": 
        # Get a, b and c coefficients from the user
        print("Input a, b and c like this: a, b, c")
        a, b, c = map(float, map(str.strip, input().split(","))) # Split by comma, strip whitespace, and convert to float
        coeffs = (a, b, c) # Store them in a tuple

    # Invalid choice
    else:
        print("Invalid choice.")
        return

    # Get a name for the function from the user
    # If left blank, the default name will be used (y1, y2, etc.)
    print("Input a name for the function (leave blank for default):")
    name = input().strip() # Get the name from the user and strip whitespace
    FunctionList.append((coeffs, name)) # Add the function to the FunctionList as a tuple of coefficients (a, b(, c)) and name


# Lists the functions in the FunctionList with their indices, names and formatted expressions
def listFunctions():
    # If there are no functions in the list, print a message and return
    if not FunctionList:
        # This message is printed when the user tries to list functions but there are none added yet
        print("No functions added yet.") # Inform the user that there are no functions to list
        return
    
    # If there are functions, print them with their indices, names and formatted expressions
    print("Available functions:")
    # Iterate through the FunctionList and print each function with its index, name and formatted expression (function) 
    for i, (coeffs, name) in enumerate(FunctionList):
        label = name if name else f"y{i + 1}" # Use the name if provided, otherwise use a default label like y1, y2, etc.
        print(f"  {i + 1}. {label}: {formatFunction(*coeffs)}") # Format the function using the formatFunction from functionManager and print it with its index and name
    print()


# Redraws the graph by clearing the screen and plotting all functions in the FunctionList
def redraw():
    initialiseGraph() # Clear the graph and set up the axes
    # Iterate through the FunctionList and plot each function with its index and name
    for index, (coeffs, name) in enumerate(FunctionList): 
        plotFunction(coeffs, index, name) # Plot the function using the plotFunction, pass the coefficients, index (for color) and name (for labeling)


# ----- MAIN ----- #
# Main loop that displays the menu, gets user input and calls the appropriate functions based on the user's choice
while True:
    print("What do you want to do?")            # Main menu prompt
    print("1. Add a function")                  # Add function option
    print("2. Create a table for a function")   # Create table option
    print("3. Edit function")                   # Edit function option
    print("4. Do calculations")                 # Calculations option
    print("5. Exit")                            # Exit option
    print()                                     # Empty line

    # Get the user's choice and strip whitespace
    choice = input("Enter your choice (1-5): ").strip()

    # Call the appropriate functions based on the user's choice using a match-case statement
    match choice:
       
        case "1":
            # Add a function
            CreateFunction() # Call the CreateFunction function
            redraw() # Redraw the graph to show the new function

        
        case "2":
            # Create a table for a function
            listFunctions() # List the functions so the user can choose which one to create a table for
            print("Enter the index of the function for which to create a table:") # Enter the index of the function they want to create a table for
            index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

            # Check if the index is valid and create the table for the chosen function
            if 0 <= index < len(FunctionList): 
                coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                print("Enter the start and end values for the table (separated by a comma):") # Prompt the user to enter the start and end values for the table
                xStart, xEnd = map(int, map(str.strip, input().split(","))) # Get the start and end values, split by comma, strip whitespace and convert to integers
                createTable(coeffs, xStart, xEnd) # Call the createTable function from functionManager 
            
            # If the index is invalid, print an error message
            else:
                print("Invalid function index.") # Error message

        
        case "3":
            # Edit function

            listFunctions() # List the functions so the user can choose which one to edit
            print("Enter the index of the function to edit:") # Enter the index of the function they want to edit
            index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

            # Check if the index is valid and allow the user to edit the chosen function
            if 0 <= index < len(FunctionList):
                coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                print(f"Editing function: {name if name else f'y{index + 1}'}") # Inform the user which function they are editing
                print("Function type: 1. Linear  2. Quadratic") # Choose the new function type (linear or quadratic)
                ftype = input("Choice: ").strip() # Get the new function type from the user and strip whitespace

                # Get the new coefficients based on the chosen function type and update the FunctionList with the new coefficients and name
                # Linear function
                if ftype == "1":
                    print("Input new a and b values (separated by a comma):") # Enter the new a and b values for a linear function
                    a, b = map(float, map(str.strip, input().split(","))) # Get the new a and b values, split by comma, strip whitespace and convert to float
                    FunctionList[index] = ((a, b), name) # Update the FunctionList with the new coefficients for a linear function (a, b) and the same name
                
                # Quadratic function
                elif ftype == "2":
                    print("Input new a, b and c values (separated by a comma):") # Enter the new a, b and c values for a quadratic function
                    a, b, c = map(float, map(str.strip, input().split(","))) # Get the new a, b and c values, split by comma, strip whitespace and convert to float
                    FunctionList[index] = ((a, b, c), name) # Update the FunctionList with the new coefficients for a quadratic function (a, b, c) and the same name
                
                # If the user enters an invalid function type, print an error message and skip the update
                else:
                    print("Invalid choice.") # Error message
                    continue

                redraw() # Redraw the graph to show the updated function

            # If the index is invalid, print an error message
            else:
                print("Invalid function index.") # Error message

        
        case "4":
            # Do calculations

            # Display the calculations menu and get the user's choice for which calculation to perform
            # Each calculation option corresponds to a function in calculationsManager 
            # that performs the calculation and returns the result, which is then formatted and displayed to the user
            print("What would you like to do?")                                         # Calculations menu prompt
            print()                                                                     # Empty line
            print("----- Calculations -----")                                           # Calculations header
            print("1. Calculate y at a specific x value")                               # Calculate y option
            print("2. Calculate x for a specific y value")                              # Calculate x option 
            print("3. Calculate the slope at a specific x value")                       # Calculate slope option
            print()                                                                     # Empty line               
            print("----- Quadratic-specific -----")                                     # Quadratic-specific calculations header
            print("4. Calculate the top/bottom of a quadratic function")                # Calculate vertex option
            print()                                                                     # Empty line
            print("----- Intersections -----")                                          # Intersections header
            print("5. Calculate the intersection coordinates of two functions")         # Calculate intersection of two functions option
            print("6. Calculate the intersection with the x-axis")                      # Calculate intersection with x-axis option
            print("7. Calculate the intersection with the y-axis")                      # Calculate intersection with y-axis option
            print()                                                                     # Empty line
            print("----- Other -----")                                                  # Other calculations header
            print("8. Calculate the minimum/maximum of a function in a given range")    # Calculate min/max in range option
            print("9. Calculate the minimum/maximum of a function")                     # Calculate global min/max option
            print("10. Back to main menu")                                              # Back to main menu option
            print()                                                                     # Empty line

            # Get the user's choice for which calculation to perform and strip whitespace
            choice = input("Enter your choice (1-9): ").strip()

            # Use a match-case statement to call the appropriate calculation function based on the user's choice, 
            # passing the necessary parameters and formatting the results for display
            match choice:

                case "1":
                    # Calculate y at a specific x value
                    listFunctions() # List the functions so the user can choose which one to calculate for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue 

                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                    print("Enter the x value:") # Enter the x value for which to calculate y
                    x = float(input()) # Get the x value and convert it to a float
                    y = CalculateY(x, coeffs) # Call the CalculateY function, pass the x value and coefficients of the chosen function to get the corresponding y value
                    print(f"y = {formatter(y)}") # Format the y value using the formatter function and display it to the user

                case "2":
                    # Calculate x for a specific y value
                    listFunctions() # List the functions so the user can choose which one to calculate for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue

                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                    print("Enter the y value:") # Enter the y value for which to calculate x
                    y = float(input()) # Get the y value and convert it to a float
                    result = CalculateX(y, coeffs) # Call the CalculateX function, pass the y value and coefficients of the chosen function to get the corresponding x value(s). The result can be None (no solutions), a single value (one solution) or a tuple of two values (two solutions) depending on the function and y value.

                    # Format and display the result to the user based on whether there are no solutions, one solution or two solutions
                    # If there are no solutions, there are no real solutions (print message). 
                    # If there is one solution, print the x value. 
                    # If there are two solutions, print both x values.

                    if result is None:
                        print("No real solutions.") # Inform the user that there are no real solutions for x given the y value and function

                    elif isinstance(result, tuple):
                        print(f"x = {formatter(result[0])} or x = {formatter(result[1])}") # Format and display both x values if there are two solutions

                    else:
                        print(f"x = {formatter(result)}") # Format and display the single x value if there is one solution

                case "3":
                    # Calculate the slope at a specific x value
                    listFunctions() # List the functions so the user can choose which one to calculate the slope for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate the slope for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue
                    
                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function

                     # If it's a linear function, the slope is constant and can be calculated without an x value
                    if len(coeffs) == 2:
                        slope = CalculateSlope(0, coeffs) # Call the CalculateSlope function, pass any x value (0 in this case) and the coefficients of the chosen linear function to get the slope (which is the same for all x values in a linear function)
                        print(f"Slope = {formatter(slope)}") # Format and display the slope to the user

                    # If it's a quadratic function, the slope varies with x and the user needs to enter an x value to calculate the slope at that point
                    else:
                        print("Enter the x value:") # Enter the x value for which to calculate the slope of the quadratic function
                        x = float(input()) # Get the x value and convert it to a float
                        slope = CalculateSlope(x, coeffs) # Call the CalculateSlope function, pass the x value and coefficients of the chosen quadratic function to get the slope at that specific x value
                        print(f"Slope at x={formatter(x)} = {formatter(slope)}") # Format and display the slope at the specific x value to the user

                case "4":
                    # Calculate the top/bottom of a quadratic function
                    listFunctions() # List the functions so the user can choose which one to calculate the vertex for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate the vertex for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue
                    
                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                    result = CalculateVertex(coeffs) # Call the CalculateVertex function, pass the coefficients of the chosen function to get the vertex (top/bottom) of the quadratic function. The result is a tuple of (x, y) coordinates for the vertex, or None if the function is not quadratic.
                    
                    # Format and display the result to the user based on whether the function is quadratic or not. 
                    # If it's not quadratic, inform the user. 
                    # If it is quadratic, display the vertex coordinates.

                    if result is None:
                        print("This is not a quadratic function.") # Function is not quadratic
                    
                    # If the result is not None, it contains the vertex coordinates (x, y) which are formatted and displayed to the user
                    else:
                        x_v, y_v = result # Unpack the vertex coordinates from the result tuple
                        print(f"Vertex at ({formatter(x_v)}, {formatter(y_v)})") # Format and display the vertex coordinates to the user

                case "5":
                    # Calculate the intersection coordinates of two functions
                    listFunctions() # List the functions so the user can choose which two to calculate the intersection for
                    print("Enter the index of the first function:") # Enter the index of the first function for the intersection calculation
                    i1 = int(input()) - 1 # Get the index of the first function, convert it to an integer and adjust for 0-based indexing
                    print("Enter the index of the second function:") # Enter the index of the second function for the intersection calculation
                    i2 = int(input()) - 1 # Get the index of the second function, convert it to an integer and adjust for 0-based indexing

                    # Check if both indices are valid and perform the calculation for the chosen functions
                    if not (0 <= i1 < len(FunctionList)) or not (0 <= i2 < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue

                    coeffs1, _ = FunctionList[i1] # Get the coefficients of the first chosen function 
                    coeffs2, _ = FunctionList[i2] # Get the coefficients of the second chosen function 
                    result = CalculateIntersectionFunction(coeffs1, coeffs2) # Call the CalculateIntersectionFunction, pass the coefficients of the two chosen functions to get the intersection point(s). The result can be None (no intersection), a single tuple of (x, y) coordinates (one intersection) or a list of tuples of (x, y) coordinates (multiple intersections) depending on the functions.
                    
                    # Format and display the result to the user based on whether there are no intersections, one intersection or multiple intersections.
                    # If there are no intersections, inform the user.
                    # If there is one intersection, display the coordinates.
                    # If there are multiple intersections, display the coordinates of each intersection point.
                    if result is None:
                        print("No intersection found.") # Inform the user that there are no intersection points between the two functions

                    # If the result is a list of tuples, it means there are multiple intersection points. Format and display each intersection point to the user.
                    elif isinstance(result[0], tuple):
                        for point in result: # Iterate through each intersection point in the result list
                            print(f"Intersection at ({formatter(point[0])}, {formatter(point[1])})") # Format and display the coordinates of each intersection point to the user

                    # If the result is a single tuple, it means there is one intersection point. Format and display the coordinates to the user.
                    else:
                        print(f"Intersection at ({formatter(result[0])}, {formatter(result[1])})") # Format and display the coordinates of the single intersection point to the user

                case "6":
                    # Calculate the intersection with the x-axis
                    listFunctions() # List the functions so the user can choose which one to calculate the intersection with the x-axis for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate the intersection with the x-axis for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue

                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                    result = CalculateIntersectionXAxis(coeffs) # Call the CalculateIntersectionXAxis function, pass the coefficients of the chosen function to get the x value(s) where the function intersects the x-axis (i.e., where y=0). The result can be None (no intersection), a single value (one intersection) or a tuple of two values (two intersections) depending on the function.
                    
                    # Format and display the result to the user based on whether there are no intersections, one intersection or two intersections with the x-axis.
                    # If there are no intersections, inform the user.
                    # If there is one intersection, display the x value.
                    # If there are two intersections, display both x values.

                    if result is None: 
                        print("No intersection with the x-axis.") # Inform the user that there are no intersection points with the x-axis 

                    # If the result is a tuple, it means there are two intersection points with the x-axis. Format and display both x values to the user.
                    elif isinstance(result, tuple): 
                        print(f"Intersects x-axis at x = {formatter(result[0])} and x = {formatter(result[1])}") # Format and display the x values of both intersection points with the x-axis to the user

                    # If the result is a single value, it means there is one intersection point with the x-axis. Format and display the x value to the user.
                    else:
                        print(f"Intersects x-axis at x = {formatter(result)}") # Format and display the x value of the single intersection point with the x-axis to the user

                case "7":
                    # Calculate the intersection with the y-axis
                    listFunctions() # List the functions so the user can choose which one to calculate the intersection with the y-axis for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate the intersection with the y-axis for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue
                    
                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                    y = CalculateIntersectionYAxis(coeffs) # Call the CalculateIntersectionYAxis function, pass the coefficients of the chosen function to get the y value where the function intersects the y-axis (i.e., where x=0). The result is a single value for all functions since they all intersect the y-axis at x=0.
                    print(f"Intersects y-axis at y = {formatter(y)}") # Format and display the y value of the intersection point with the y-axis to the user

                case "8":
                    # Calculate the minimum/maximum of a function in a given range
                    listFunctions() # List the functions so the user can choose which one to calculate the minimum/maximum for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate the minimum/maximum for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)):
                        print("Invalid function index.") # Error message
                        continue

                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                    print("Enter the start and end of the range (separated by a comma):") # Enter the start and end values for the range in which to calculate the minimum/maximum
                    xStart, xEnd = map(float, map(str.strip, input().split(","))) # Get the start and end values for the range, split by comma, strip whitespace and convert to floats
                    min_y, max_y = CalculateMinMaxRange(coeffs, xStart, xEnd) # Call the CalculateMinMaxRange function, pass the coefficients of the chosen function and the start and end values of the range to get the minimum and maximum y values of the function within that range. The result is a tuple of (min_y, max_y).
                    print(f"Minimum: {formatter(min_y)}, Maximum: {formatter(max_y)}") # Format and display the minimum and maximum y values to the user

                case "9":
                    # Calculate the minimum/maximum of a function globally
                    listFunctions() # List the functions so the user can choose which one to calculate the global minimum/maximum for
                    print("Enter the index of the function to use:") # Enter the index of the function they want to calculate the global minimum/maximum for
                    index = int(input()) - 1 # Get the index, convert it to an integer and adjust for 0-based indexing

                    # Check if the index is valid and perform the calculation for the chosen function
                    if not (0 <= index < len(FunctionList)): 
                        print("Invalid function index.") # Error message
                        continue

                    coeffs, name = FunctionList[index] # Get the coefficients and name of the chosen function
                    min_y, max_y = CalculateMinMax(coeffs) # Call the CalculateMinMax function, pass the coefficients of the chosen function to get the global minimum and maximum y values of the function. The result is a tuple of (min_y, max_y).
                    print(f"Minimum: {formatter(min_y)}, Maximum: {formatter(max_y)}") # Format and display the global minimum and maximum y values to the user

                case "10":
                    # Back to main menu
                    continue
        
        case "5":
            # Exit the program
            break

        case _:
            # Invalid choice
            print("Invalid choice. Please enter a number between 1 and 5.")

# End of program
bye()