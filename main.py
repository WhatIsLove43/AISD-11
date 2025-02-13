import tkinter as tk
from tkinter import messagebox
import math
import random
import time

class DistanceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Минимальное расстояние между точками")

        window_width = 400
        window_height = 300

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label = tk.Label(root, text="Введите количество точек (N):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.calculate_button = tk.Button(root, text="Сгенерировать точки", command = self.calculate_min_distance)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def generate_random_points(self, n):
        points = [(random.randint(0, 500), random.randint(0, 500)) for _ in range(n)]
        return points

    def calculate_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def calculate_min_distance(self):
        try:
            n = int(self.entry.get())
            if n < 2:
                raise ValueError("Количество точек должно быть больше 1.")

            points = self.generate_random_points(n)
            min_distance = float('inf')
            closest_pair = None

            for i in range(n):
                for j in range(i + 1, n):
                    distance = self.calculate_distance(points[i], points[j])
                    if distance <min_distance:
                        min_distance = distance
                        closest_pair = (points[i], points[j])

            result_text = f"Минимальноерасстояние: {min_distance:.2f}\n"
            result_text += f"Параточек: {closest_pair}"
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    start_time = time.perf_counter()
    root = tk.Tk()
    DistanceCalculator(root)
    end_time = time.perf_counter()
    final_time = end_time - start_time
    print(f"Время работы программы: {final_time:.2f} секунд")
    root.mainloop()
