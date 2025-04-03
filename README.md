# Layup

Layup Parts Software Engineer Take Home Test

## Prerequisites
python3
numpy
matplotlib

## Setup Instructions

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/Leon753/Layup.git
cd Layup
```

### Airplane Simulator
```bash
python3 simulator.py
```
### Explanation of Trajectory Calculations

- **Displacement Calculation:**  
  - Computes horizontal (`dx`) and vertical (`dy`) displacements using:
    - `dx = speed * cos(angle) * dt`
    - `dy = speed * sin(angle) * dt`  
  where `angle` is the yaw (in radians) and `dt` is the time step.

- **Position Update:**  
  - Adds the computed `dx` and `dy` to the current position to get the new position.

- **Wrap-Around Logic:**  
  - Uses modulo arithmetic to wrap the position:
    - `wrapped_x = new_x % canvas_width`
    - `wrapped_y = new_y % canvas_height`  
  This ensures that if the airplane leaves one side of the canvas, it reappears on the opposite side.

- **Drawing the Trajectory:**  
  - Draws a line from the previous position to the new position **only if** no wrap-around occurs, preventing an unwanted line across the screen.

### Layup Sequence
```bash
python3 layup_sequence.py
```

### Runtime/Time Complexity/Optimzations

- **Runtime:**  
  - As shown in the graph we can see visually that the linear regression line fits
    well. Unfortunately the R^2 value is quiet low but that is probably due to
    operations being so fast, that noise is a larger factor.

- **Time Complexity:**  
  - O(n) -> The algorithm performs a single loop that iterates n times 
    and does constant work (2 constant calls (n-1) and (n-2) inside the loop, 
    its time complexity is O(n)

- **Optimizaitons Made:**  
  - I used memoization to store already seen values, making repetitive
    calls constant time.