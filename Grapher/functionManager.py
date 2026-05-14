# ----- FUNCTIONS ----- #
# Formatting function for functions
def formatFunction(a, b, c=None):
   
    # Helper function to format the coefficient and variable part of the function for labeling
    def format_coef(val, var, is_first=False):
        val = int(val) if val == int(val) else val # Value is converted to int if it's a whole number for cleaner display
        
        # If the coefficient is zero, we skip it entirely
        if val == 0:
            return ""
        
        # For the first term, we don't include a leading '+' sign. 
        # For subsequent terms, we include a '+' or '-' based on the sign of the coefficient.
        if is_first:
            # If the coefficient is 1, we just return the variable without the coefficient. 
            if val == 1:
                return var
            
            # If the coefficient is -1, we return the variable with a '-' sign. 
            if val == -1:
                return f"-{var}"
            
            # For other coefficients, we include the coefficient and variable without a leading '+' sign.
            return f"{val}{var}" 
        
        # For subsequent terms, we include a '+' or '-' sign based on the value of the coefficient.
        else:
            # If the coefficient is 1, we return the variable with a '+' sign.
            if val == 1:
                return f" + {var}"
            
            # If the coefficient is -1, we return the variable with a '-' sign.
            if val == -1:
                return f" - {var}"
            
            # For other coefficients, we include the coefficient and variable with the appropriate sign.
            if val < 0:
                return f" - {abs(val)}{var}"
            
            # For positive coefficients, we include a '+' sign.
            return f" + {val}{var}"

    # Helper function to format the constant part of the function for labeling
    def format_const(val, is_first=False):

        # Similar to format_coef, we convert the value to int if it's a whole number for cleaner display.
        val = int(val) if val == int(val) else val # Value is converted to int if it's a whole number for cleaner display
        
        # If the constant is zero, we skip it entirely.
        if val == 0:
            return ""
        
        # For the first constant term, we just return the value without a leading '+' sign.
        if is_first:
            return str(val)
        
        # For subsequent constant terms, we include a '+' or '-' sign based on the value of the constant.
        if val < 0:
            return f" - {abs(val)}"
        
        # For positive constants, we include a '+' sign.
        return f" + {val}"

    # Format the function expression based on whether it's a quadratic (with c) or linear (without c) function.
    if c is not None:
        a_str = format_coef(a, "x²", is_first=True) # For the first term, we treat it as the first term in the expression for proper formatting.
        b_str = format_coef(b, "x", is_first=not a_str) # For the second term, we check if the first term was included to determine if we need a leading '+' sign.
        c_str = format_const(c, is_first=not a_str and not b_str) # For the constant term, we check if both the first and second terms were included to determine if we need a leading '+' sign.
        expr = a_str + b_str + c_str or "0" # If all terms are zero, we return "0" to represent the function as y = 0.
        return f"y = {expr}" # We return the formatted function expression as a string in the form of "y = ..." for labeling purposes.
    
    # For linear functions, we only have a and b. We format them similarly but without the x² term.
    else:
        a_str = format_coef(a, "x", is_first=True) # For the first term, we treat it as the first term in the expression for proper formatting.
        b_str = format_const(b, is_first=not a_str) # For the constant term, we check if the first term was included to determine if we need a leading '+' sign.
        expr = a_str + b_str or "0" # If both terms are zero, we return "0" to represent the function as y = 0.
        return f"y = {expr}" # We return the formatted function expression as a string in the form of "y = ..." for labeling purposes.

# Function to calculate the result of a function given its coefficients and an x value. It handles both linear and quadratic functions based on the number of coefficients provided.
def getResult(coeffs, x):
    # If there are three coefficients, we treat it as a quadratic function of the form ax² + bx + c. We unpack the coefficients into a, b, and c and calculate the result accordingly.
    if len(coeffs) == 3: 
        a, b, c = coeffs # We unpack the coefficients into a, b, and c for the quadratic function.
        return a * x**2 + b * x + c # We calculate the result of the quadratic function using the formula ax² + bx + c and return it.
    
    # For linear functions, we only have a and b.
    a, b = coeffs # We unpack the coefficients into a and b for the linear function.
    return a * x + b # We calculate the result of the linear function using the formula ax + b and return it.

# Function to create a table of x and y values for a given function within a specified range. It formats the output in a tabular form for easy reading.
def createTable(coeffs, xStart, xEnd):
    xs = list(range(xStart, xEnd + 1)) # We create a list of x values from xStart to xEnd inclusive using the range function and convert it to a list.
    ys = [getResult(coeffs, x) for x in xs] # We calculate the corresponding y values for each x value by calling the getResult function with the coefficients and each x value, and we store the results in a list called ys.

    # Helper function to format values for the table, converting to int if the value is a whole number for cleaner display.
    def format_val(val):
        return str(int(val)) if val == int(val) else str(val) # We check if the value is a whole number by comparing it to its integer conversion. 
                                                              # If it is a whole number, we convert it to an integer and then to a string for cleaner display. 
                                                              # Otherwise, we convert it to a string as is.

    x_strs = [format_val(x) for x in xs] # We format the x values for display in the table by applying the format_val function to each x value and storing the results in a list called x_strs.
    y_strs = [format_val(y) for y in ys] # We format the y values for display in the table by applying the format_val function to each y value and storing the results in a list called y_strs.

    col_widths = [max(len(x_strs[i]), len(y_strs[i])) for i in range(len(xs))] # We calculate the maximum width needed for each column in the table by comparing the lengths of the formatted x and y strings for each column and storing the maximum widths in a list called col_widths.

    x_row = "x | " + " | ".join(x_strs[i].rjust(col_widths[i]) for i in range(len(xs))) + " |" # We create the header row for the x values by joining the formatted x strings with " | " as a separator and right-justifying each string based on the calculated column widths. We also add "x | " at the beginning and " |" at the end for formatting.
    y_row = "y | " + " | ".join(y_strs[i].rjust(col_widths[i]) for i in range(len(xs))) + " |" # We create the header row for the y values in a similar way to the x row, but with "y | " at the beginning. We join the formatted y strings with " | " as a separator and right-justify each string based on the calculated column widths. We also add " |" at the end for formatting.
    sep = "-" * len(x_row) # We create a separator line by repeating the "-" character for the length of the x_row string to visually separate the header from the data rows in the table.

    # We print the x row, separator, and y row to display the table of x and y values in a formatted manner.
    print(x_row) 
    print(sep)
    print(y_row)