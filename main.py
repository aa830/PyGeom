import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, simpledialog

def calculate_distance():
    x1, y1, x2, y2 = get_two_points()
    if x1 is None:
        return
    distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    messagebox.showinfo("Distance", f"Distance: {distance:.2f}")
    visualize(x1, y1, x2, y2, "Distance")

def calculate_midpoint():
    x1, y1, x2, y2 = get_two_points()
    if x1 is None:
        return
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    messagebox.showinfo("Midpoint", f"Midpoint: ({mid_x:.2f}, {mid_y:.2f})")
    visualize(x1, y1, x2, y2, "Midpoint", [(mid_x, mid_y)])

def calculate_slope():
    x1, y1, x2, y2 = get_two_points()
    if x1 is None:
        return
    if x1 == x2:
        messagebox.showinfo("Slope", "Slope is undefined (vertical line)")
    else:
        slope = (y2 - y1) / (x2 - x1)
        messagebox.showinfo("Slope", f"Slope: {slope:.2f}")

def calculate_triangle_area():
    x1, y1, x2, y2, x3, y3 = get_three_points()
    if x1 is None:
        return
    area = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
    messagebox.showinfo("Triangle Area", f"Area: {area:.2f}")
    visualize(x1, y1, x2, y2, "Triangle", [(x3, y3)], triangle=True)

def get_two_points():
    try:
        x1 = float(simpledialog.askstring("Input", "Enter x1: "))
        y1 = float(simpledialog.askstring("Input", "Enter y1: "))
        x2 = float(simpledialog.askstring("Input", "Enter x2: "))
        y2 = float(simpledialog.askstring("Input", "Enter y2: "))
        return x1, y1, x2, y2
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
        return None, None, None, None

def get_three_points():
    try:
        x1, y1, x2, y2 = get_two_points()
        if x1 is None:
            return None, None, None, None, None, None
        x3 = float(simpledialog.askstring("Input", "Enter x3: "))
        y3 = float(simpledialog.askstring("Input", "Enter y3: "))
        return x1, y1, x2, y2, x3, y3
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
        return None, None, None, None, None, None

def visualize(x1, y1, x2, y2, title, extra_points=[], triangle=False):
    plt.figure()
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.scatter([x1, x2], [y1, y2], color='red', label='Points')
    plt.plot([x1, x2], [y1, y2], 'r-', label='Line Segment')
    
    for (x, y) in extra_points:
        plt.scatter(x, y, color='blue', label='Extra Point')
    
    if triangle:
        x3, y3 = extra_points[0]
        plt.scatter(x3, y3, color='green', label='Third Point')
        plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'g-', label='Triangle')
    
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()

def main():
    root = tk.Tk()
    root.withdraw()
    while True:
        choice = simpledialog.askinteger("Menu", "1. Distance\n2. Midpoint\n3. Slope\n4. Triangle Area\n5. Exit\nEnter choice (1-5):")
        if choice == 1:
            calculate_distance()
        elif choice == 2:
            calculate_midpoint()
        elif choice == 3:
            calculate_slope()
        elif choice == 4:
            calculate_triangle_area()
        elif choice == 5:
            messagebox.showinfo("Exit", "Goodbye!")
            break
        else:
            messagebox.showerror("Error", "Invalid choice. Please enter a number from 1-5.")

if __name__ == "__main__":
    main()
