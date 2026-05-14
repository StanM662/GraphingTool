# ----- IMPORTS ----- #
from functionManager import getResult
from math import sqrt

# ----- FUNCTIONS ----- #
# Calculate y at a specific x value
def CalculateY(x_value, function):
    # Just plug the x value into the function to get the y value
    return getResult(function, x_value)


# Calculate x for a specific y value
def CalculateX(y_value, function):
    # You want to figure out where function = y_value
    # Is the function linear or quadratic?
    # For linear functions, it's just ax + b = y_value -> x = (y_value - b) / a
    # For quadratic functions, it's ax^2 + bx + c = y_value -> ax^2 + bx + (c - y_value) = 0 -> use quadratic formula
    
    # Linear function
    if len(function) == 2:
        a, b = function # get a and b from the function tuple

        # If a is 0, then it's a constant function and we can only solve if b == y_value
        if a == 0:
            return None  # No solution if it's a constant function that doesn't equal y_value
        return (y_value - b) / a # Solve for x in the linear equation ax + b = y_value -> x = (y_value - b) / a
    
    # Quadratic function
    else:
        a, b, c = function # get a, b and c from the function tuple
        # Solve ax^2 + bx + (c - y_value) = 0
        
        # Use the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)
        discriminant = b**2 - 4*a*(c - y_value) # Calculate the discriminant of the quadratic equation
        
        # Check the discriminant to determine the number of solutions
        # If the discriminant is negative, there are no real solutions. 
        # If it's zero, there's one solution. 
        # If it's positive, there are two solutions.
        if discriminant < 0: 
            return None  # No real solutions
        
        elif discriminant == 0:
            return -b / (2*a)  # One solution
        
        else:
            x1 = (-b + sqrt(discriminant)) / (2*a)
            x2 = (-b - sqrt(discriminant)) / (2*a)
            return x1, x2  # Two solutions


# Calculate the slope at a specific x value (for linear functions, this is just a)
def CalculateSlope(x_value, function):
    # For linear functions, the slope is constant and equal to a
    # For quadratic functions, the slope at a specific x value is given by the derivative:
    # f'(x) = 2ax + b for ax^2 + bx + c

    # Linear function
    if len(function) == 2:
        a, _ = function # get a from the function tuple (we don't need b for the slope)
        return a # The slope of a linear function ax + b is just a
    
    # Quadratic function
    else:
        a, b, _ = function # get a and b from the function tuple (we don't need c for the slope)
        return 2*a*x_value + b  # The slope of a quadratic function ax^2 + bx + c 
                                # at a specific x value is given by the derivative: f'(x) = 2ax + b

# Calculate the top/bottom of a quadratic function
def CalculateVertex(function):
    # The vertex of a quadratic function ax^2 + bx + c is at x = -b/(2a), 
    # and the y value can be found by plugging this x back into the function

    # This only applies to quadratic functions, so if it's linear we can return None
    if len(function) == 3:
        a, b, c = function # get a, b and c from the function tuple

        # If a is 0, then it's not a quadratic function and we can't calculate the vertex
        if a == 0:
            return None  # Not a quadratic function
        
        x_vertex = -b / (2*a) # The x value of the vertex is given by -b/(2a)
        y_vertex = getResult(function, x_vertex) # The y value can be found by plugging x back into the function
        return x_vertex, y_vertex # Return the coordinates of the vertex as a tuple (x_vertex, y_vertex)
    return None # Linear function doesn't have a vertex -> return None


# Calculate the intersection coordinates of two functions  
def CalculateIntersectionFunction(function1, function2):
    # To find the intersection, we need to solve function1 = function2
    # This can be done by rearranging to function1 - function2 = 0 and solving for x
    # Then we can plug the x values back into either function to get the y values
    
    # Linear vs Linear
    if len(function1) == 2 and len(function2) == 2:
        a1, b1 = function1 # get a and b from the first function tuple
        a2, b2 = function2 # get a and b from the second function tuple

        # If the slopes are the same, the lines are either parallel (no intersection) 
        # or the same line (infinite intersections)
        if a1 == a2:
            return None  # Parallel lines (or the same line)
        
        # Solve for x in the equation a1*x + b1 = a2*x + b2 -> 
        # (a1 - a2)*x = b2 - b1 -> 
        # x = (b2 - b1) / (a1 - a2)
        x_intersect = (b2 - b1) / (a1 - a2) # Calculate the x coordinate of the intersection
        y_intersect = getResult(function1, x_intersect) # Calculate y by plugging x back into either function 
        return x_intersect, y_intersect # Return the coordinates of the intersection as a tuple (x_intersect, y_intersect)
    
    # Linear vs Quadratic
    elif len(function1) == 2 and len(function2) == 3:
        a1, b1 = function1 # get a and b from the linear function tuple
        a2, b2, c2 = function2 # get a, b and c from the quadratic function tuple

        # Solve a1*x + b1 = a2*x^2 + b2*x + c2
        # Rearranging gives: a2*x^2 + (b2 - a1)*x + (c2 - b1) = 0
        A = a2      # Coefficient of x^2
        B = b2 - a1 # Coefficient of x
        C = c2 - b1 # Constant term

        # Use the quadratic formula: x = (-B ± sqrt(B^2 - 4AC)) / (2A)
        discriminant = B**2 - 4*A*C
        
        # Check the discriminant to determine the number of solutions
        # If the discriminant is negative, there are no real solutions.
        # If it's zero, there's one solution.
        # If it's positive, there are two solutions.
        if discriminant < 0:
            return None  # No real solutions
        
        elif discriminant == 0:
            x_intersect = -B / (2*A) # Calculate the x coordinate of the intersection
            y_intersect = getResult(function1, x_intersect) # Calculate y by plugging x back into either function
            return x_intersect, y_intersect  # One solution
        
        else:
            x1 = (-B + sqrt(discriminant)) / (2*A) # Calculate the x coordinates of the two intersections (+)
            x2 = (-B - sqrt(discriminant)) / (2*A) # Calculate the x coordinates of the two intersections (-)
            y1 = getResult(function1, x1) # Calculate y by plugging x back into either function
            y2 = getResult(function1, x2) # Calculate y by plugging x back into either function
            return (x1, y1), (x2, y2)  # Two solutions
    
    # Quadratic vs Quadratic
    elif len(function1) == 3 and len(function2) == 3:
        a1, b1, c1 = function1 # get a, b and c from the first quadratic function tuple
        a2, b2, c2 = function2 # get a, b and c from the second quadratic function tuple
        # Solve a1*x^2 + b1*x + c1 = a2*x^2 + b2*x + c2
        # Rearranging gives: (a1 - a2)*x^2 + (b1 - b2)*x + (c1 - c2) = 0
        A = a1 - a2 # Coefficient of x^2
        B = b1 - b2 # Coefficient of x
        C = c1 - c2 # Constant term

        # Use the quadratic formula: x = (-B ± sqrt(B^2 - 4AC)) / (2A)
        discriminant = B**2 - 4*A*C

        # Check the discriminant to determine the number of solutions
        # If the discriminant is negative, there are no real solutions.
        # If it's zero, there's one solution.
        # If it's positive, there are two solutions.
        if discriminant < 0:
            return None  # No real solutions
        
        elif discriminant == 0:
            x_intersect = -B / (2*A) # Calculate the x coordinate of the intersection
            y_intersect = getResult(function1, x_intersect) # Calculate y by plugging x back into either function
            return x_intersect, y_intersect  # One solution
        
        else:
            x1 = (-B + sqrt(discriminant)) / (2*A) # Calculate the x coordinates of the two intersections (+)
            x2 = (-B - sqrt(discriminant)) / (2*A) # Calculate the x coordinates of the two intersections (-)
            y1 = getResult(function1, x1) # Calculate y by plugging x back into either function
            y2 = getResult(function1, x2) # Calculate y by plugging x back into either function
            return (x1, y1), (x2, y2)  # Two solutions
    
    else:
        return None  # Unsupported function types
    

# Calculate the intersection with the x-axis
def CalculateIntersectionXAxis(function):
    # To find the intersection with the x-axis, we need to solve function = 0
    # For linear functions, it's just ax + b = 0 -> x = -b/a
    # For quadratic functions, it's ax^2 + bx + c = 0 -> use quadratic formula

    # Linear function
    if len(function) == 2:
        a, b = function # get a and b from the function tuple

        # If a is 0, then it's a constant function and we can only solve if b == 0
        if a == 0: 
            return None  # No solution
        
        # Solve for x in the linear equation ax + b = 0 -> x = -b/a
        return -b / a # Returns the x value where the function intersects the x-axis (y = 0)
    
    # Quadratic function
    else:
        a, b, c = function # get a, b and c from the function tuple
        # Solve ax^2 + bx + c = 0

        # Use the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)
        discriminant = b**2 - 4*a*c

        # Check the discriminant to determine the number of solutions
        # If the discriminant is negative, there are no real solutions.
        # If it's zero, there's one solution.
        # If it's positive, there are two solutions.

        if discriminant < 0:
            return None  # No real solutions
        
        elif discriminant == 0:
            return -b / (2*a)  # One solution
        
        else:
            x1 = (-b + sqrt(discriminant)) / (2*a) # Calculate the x coordinates of the two intersections (+)
            x2 = (-b - sqrt(discriminant)) / (2*a) # Calculate the x coordinates of the two intersections (-)
            return x1, x2  # Two solutions


# Calculate the intersection with the y-axis
def CalculateIntersectionYAxis(function):
    # To find the intersection with the y-axis, we need to solve function at x = 0
    return getResult(function, 0) # Returns the y value when x is 0, which is the intersection with the y-axis


# Calculate the minimum/maximum of a function in a given range
def CalculateMinMaxRange(function, xStart, xEnd):
    # For linear functions, the minimum/maximum in a range will just be at one of the endpoints
    # For quadratic functions, we need to check the vertex as well as the endpoints
    
    # Linear function
    if len(function) == 2:
        a, b = function # get a and b from the function tuple
        
        # Evaluate the function at the endpoints
        y_start = getResult(function, xStart) # Calculate the y value at the start of the range
        y_end = getResult(function, xEnd) # Calculate the y value at the end of the range

        # For linear functions, the minimum and maximum are at the endpoints
        return min(y_start, y_end), max(y_start, y_end) # Return the minimum and maximum y values in the given range as a tuple (min_y, max_y)
    
    # Quadratic function
    else:
        a, b, c = function # get a, b and c from the function tuple

        # Find the vertex
        vertex_x = -b / (2 * a) # The x value of the vertex is given by -b/(2a)
        vertex_y = getResult(function, vertex_x) # The y value can be found by plugging the x back into the function
        
        # Evaluate the function at the endpoints 
        y_start = getResult(function, xStart) # Calculate the y value at the start of the range
        y_end = getResult(function, xEnd) # Calculate the y value at the end of the range

        # Determine the minimum and maximum based on the vertex and endpoints
        if a > 0:  # Parabola opens upwards
            min_y = vertex_y # The minimum is at the vertex for an upward-opening parabola
            max_y = max(y_start, y_end) # The maximum is at one of the endpoints for an upward-opening parabola

        else:  # Parabola opens downwards
            min_y = min(y_start, y_end) # The minimum is at one of the endpoints for a downward-opening parabola
            max_y = vertex_y # The maximum is at the vertex for a downward-opening parabola
        
        return min_y, max_y # Return the minimum and maximum y values in the given range as a tuple (min_y, max_y)

# Calculate the minimum/maximum of a function (for quadratic functions, this is just the vertex)
def CalculateMinMax(function):
    # For linear functions, there is no minimum or maximum (unless it's a constant function)
    # For quadratic functions, the minimum or maximum is at the vertex

    # Quadratic function
    if len(function) == 3: 
        a, b, c = function # get a, b and c from the function tuple

        # If a is 0, then it's not a quadratic function and we can't calculate the minimum/maximum
        if a == 0:
            return None  # Not a quadratic function
        
        # Find the vertex
        vertex_x = -b / (2 * a) # The x value of the vertex is given by -b/(2a)
        vertex_y = getResult(function, vertex_x) # The y value can be found by plugging the x back into the function
        return vertex_y, vertex_y  # For a quadratic function, min and max are the same at the vertex
    
    else:
        return None  # Unsupported function type