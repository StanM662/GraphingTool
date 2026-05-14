# Graphing Tool

A lightweight, interactive Python application for graphing and analyzing mathematical functions. Built with Python's standard `turtle` library, this tool allows you to visualize linear and quadratic functions and perform a variety of algebraic calculations.

## Features

### Interactive Visualization
- **Live Graphing**: Watch your functions being drawn in real-time on a 2D coordinate system.
- **Multiple Functions**: Add and compare multiple functions on the same graph with distinct colors.
- **Dynamic Updates**: The graph automatically redraws whenever you add or edit a function.

### Supported Functions
- **Linear**: $y = ax + b$
- **Quadratic**: $y = ax² + bx + c$

### Advanced Calculations
The tool includes a robust calculation engine that can:
- **Value Mapping**: Calculate $y$ for any $x$, or find $x$ for a specific $y$.
- **Slope Analysis**: Determine the slope of a linear function or the instantaneous slope (derivative) of a quadratic function at any point.
- **Vertex Detection**: Find the exact coordinates of the top or bottom (vertex) of a parabola.
- **Intersections**: 
  - Find where two functions cross each other.
  - Calculate intersections with the $x$-axis (roots) and $y$-axis.
- **Range Analysis**: Find the minimum and maximum values of a function within a specific domain.

### Data Management
- **Table Generation**: Create a table of values for any function within a custom range.
- **Function Editing**: Update your functions on the fly and see the changes reflected immediately.
- **Naming**: Give your functions custom names for easier identification.

## Installation & Usage

### Prerequisites
- Python 3.x installed.
- No external dependencies required (Uses standard libraries `turtle` and `math`).

### Running the Tool
1. Clone the repository:
   ```bash
   git clone https://github.com/StanM662/GraphingTool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd GraphingTool
   ```
3. Run the application:
   ```bash
   python Grapher/main.py
   ```

## Project Structure
- `Grapher/main.py`: The main entry point and CLI menu logic.
- `Grapher/calculationsManager.py`: The "math brain" which handles all the algebraic calculations.
- `Grapher/graphManager.py`: Manages the `turtle` canvas and plotting logic.
- `Grapher/functionManager.py`: Handles function formatting, evaluation, and table generation.

## License
This project was made for fun and is open-source. Feel free to use, modify, and share!

# To-Do List
## High Priority
- Add support for more functions
- Add ability to change bounds of the graph (Xmin, Xmax, Ymin, Ymax)
- Add ability to add custom values (points) to the graph 

## Medium Priority
- Make the function writing more advanced
- Add more error handling
- Add zoom and pan features
- Exporting/Importing functions/tables
- Settings page to configure values, preferences, etc.

## Low Priority
- Add a simple GUI
- Fix graphing when x value is outside of visible range
- Add ability to save graphs
- Add the ability to save and load functions from a file
- Make table generation more advanced
- Add more advanced calculations 
- Add ability to add functions for cos(), sin(), tan(), etc.