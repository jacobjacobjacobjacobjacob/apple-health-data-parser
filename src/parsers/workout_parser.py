# src/parsers/workout_parsers.py
from src.parsers.base_parser import BaseParser


class WorkoutDataParser(BaseParser):
    def __init__(self, file_path: str, workout_type: str = None):
        """Initializes the WorkoutParser with the specified file path and workout type."""
        super().__init__(file_path)
        self.workout_type = workout_type  # Can be None to parse all types

    def handle_element(self, elem):
        if elem.tag == "Workout":
            # Parse all workouts if workout_type is None, otherwise filter by workout type
            if (
                self.workout_type is None
                or elem.attrib.get("workoutActivityType") == self.workout_type
            ):
                record = {
                    "date": elem.attrib.get("startDate"),
                    "duration": elem.attrib.get("duration"),
                    "workout_type": elem.attrib.get("workoutActivityType"),
                    "type": "Workout",
                    
                }
            self.data.append(record)
