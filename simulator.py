import tkinter as tk
import math

class LayupAirplaneSimulator:
    """
    A simple airplane simulator that visualizes the trajectory on a canvas.
    The airplane wraps around the screen edges.
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Layup Airplane Simulator")

        self.canvas_width = 400
        self.canvas_height = 400
        self.time_step = 0.05
        self.x = self.canvas_width / 2
        self.y = self.canvas_height / 2

        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.create_controls()
        self.draw_marker(self.x, self.y, color="blue")
        self.update_simulation()

    def create_controls(self) -> None:
        """Control sliders for yaw angle and airspeed."""
        controls_frame = tk.Frame(self.master)
        controls_frame.pack(pady=10)

        tk.Label(controls_frame, text="Yaw Angle (degrees):").pack(side=tk.LEFT, padx=5)
        self.yaw_var = tk.DoubleVar(value=0)
        tk.Scale(controls_frame, from_=-180, to=180, orient=tk.HORIZONTAL, variable=self.yaw_var).pack(side=tk.LEFT, padx=5)

        tk.Label(controls_frame, text="Airspeed (knots):").pack(side=tk.LEFT, padx=5)
        self.speed_var = tk.DoubleVar(value=5)
        tk.Scale(controls_frame, from_=0, to=40, orient=tk.HORIZONTAL, variable=self.speed_var).pack(side=tk.LEFT, padx=5)

    def draw_marker(self, x: float, y: float, color: str, size: int = 4) -> None:
        """Draws a small marker on the canvas at the given coordinates."""
        self.canvas.create_oval(x - size/2, y - size/2, x + size/2, y + size/2, fill=color, outline=color)

    def update_simulation(self) -> None:
        """Updates the simulation by computing the new position and drawing the trajectory.
           If a wrap-around is detected, it skips drawing the connecting line.
        """
        dt = self.time_step
        yaw_degrees = self.yaw_var.get()
        speed = self.speed_var.get()
        angle = math.radians(yaw_degrees)

        dx = speed * math.cos(angle) * dt
        dy = speed * math.sin(angle) * dt

        last_x, last_y = self.x, self.y

        new_x = self.x + dx
        new_y = self.y + dy

        wrapped_x = new_x % self.canvas_width
        wrapped_y = new_y % self.canvas_height

        if new_x == wrapped_x and new_y == wrapped_y:
            self.canvas.create_line(last_x, last_y, wrapped_x, wrapped_y, fill="red")

        self.x, self.y = wrapped_x, wrapped_y
        self.master.after(int(dt * 1000), self.update_simulation)

if __name__ == "__main__":
    root = tk.Tk()
    simulator = LayupAirplaneSimulator(root)
    root.mainloop()
