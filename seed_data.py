from datetime import datetime, timedelta
from models import FitnessClass

fitness_classes = [
    FitnessClass(1, "Yoga", datetime(2025, 6, 5, 7, 0), "Alice", 5),
    FitnessClass(2, "Zumba", datetime(2025, 6, 5, 9, 0), "Bob", 8),
    FitnessClass(3, "HIIT", datetime(2025, 6, 6, 18, 0), "Charlie", 10),
]
