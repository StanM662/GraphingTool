# ----- IMPORTS ----- #
from turtle import *
from functionManager import getResult, formatFunction

# ----- VARIABLES ----- #
# Colors for plotting functions, will cycle through if more than 8 functions are plotted
COLORS = ["black", "blue", "red", "green", "orange", "purple", "brown", "pink"]

# ----- FUNCTIONS ----- #
# Function to set up the graph with axes and labels
def initialiseGraph():
    clearscreen() # Clear the graph to start fresh
    setworldcoordinates(-10, -10, 10, 10) # Set the coordinate system to go from -10 to 10 on both axes
    speed(0) # Set the turtle speed to the fastest for quick drawing
    penup() # Move the turtle without drawing to the starting position for the axes
    
    goto(-10, 0) # Move to the left end of the x-axis
    pendown() # Start drawing the x-axis
    goto(10, 0) # Draw the x-axis to the right end
    penup() # Move the turtle without drawing to the starting position for the y-axis

    goto(0, -10) # Move to the bottom end of the y-axis
    pendown() # Start drawing the y-axis
    goto(0, 10) # Draw the y-axis to the top end

    penup() # Move the turtle without drawing to the position for labeling the axes
    goto(9.5, 0.2) # Move to the position near the end of the x-axis for labeling
    write("x", font=("Arial", 10, "normal")) # Label the x-axis
    goto(0.2, 9.5) # Move to the position near the end of the y-axis for labeling
    write("y", font=("Arial", 10, "normal")) # Label the y-axis
    update() # Update the graph to show the axes and labels

# Function to plot a function on the graph given its coefficients, index for color and name for labeling
def plotFunction(coeffs, index=0, name=""):
    col = COLORS[index % len(COLORS)] # Choose the color for plotting based on the index, cycling through the COLORS list
    color(col) # Set the turtle color for plotting the function

    # Label
    funcName = name if name else f"y{index + 1}" # Use the provided name for labeling if available, otherwise use a default name like y1, y2, etc. based on the index
    label = formatFunction(*coeffs) # Format the function for labeling
    penup() # Move the turtle without drawing to the position for labeling the function
    goto(-9.5, 9.5 - (index * 1.2)) # Move to a position in the top left corner for labeling, adjusting the y position based on the index to avoid overlap
    write(f"{funcName}: {label[4:]}", font=("Arial", 10, "normal")) # Write the label for the function, showing the name and the formatted function expression (excluding the "y = " part)

    # Plot
    penup() # Move the turtle without drawing to the starting position for plotting the function
    x = -10.0 # Start plotting from x = -10
    first = True # Flag to indicate whether it's the first point being plotted, used to determine when to pen down for drawing
    
    # Iterate through x values from -10 to 10 in increments of 0.1 to plot the function
    while x <= 10.0:
        y = getResult(coeffs, x) # Calculate the corresponding y value for the current x using the getResult function from functionManager, passing the coefficients of the function and the current x value
        
        # Only plot points where y is between -10 and 10 to keep the graph within the visible area. If y is out of bounds, pen up to move without drawing until we get back into bounds.
        if -10 <= y <= 10: 
            # If it's the first point being plotted, pen down to start drawing. 
            # For subsequent points, just go to the new position to continue drawing the function. 
            # If we encounter a point where y is out of bounds, 
            # pen up and set the first flag to True so that when we get back into bounds, we know to pen down again.
            if first:
                penup() # Move the turtle without drawing to the first point of the function
                first = False # Set the first flag to False after plotting the first point
            
            # For subsequent points, if the y value is within bounds, we continue drawing by going to the new position. 
            # If we encounter a point where y is out of bounds, 
            # we pen up and set the first flag to True so that when we get back into bounds, we know to pen down again.
            else:
                pendown() # Start drawing to the next point of the function

            goto(x, y) # Move to the new position (x, y) to continue drawing the function
        
        # If the y value is out of bounds, we pen up to move without drawing until we get back into bounds. 
        # We also set the first flag to True so that when we get back into bounds, 
        # we know to pen down again for drawing.
        else:
            penup() # Move the turtle without drawing to the next point since it's out of bounds
            first = True # Set the first flag to True so that when we get back into bounds, we know to pen down again for drawing

        x += 0.1 # Increment x by 0.1 to plot the next point of the function

    penup() # Move the turtle without drawing after finishing plotting the function
    update() # Update the graph to show the newly plotted function