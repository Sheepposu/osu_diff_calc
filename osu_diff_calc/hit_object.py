class DifficultyHitObject:
    def __init__(self, hit_obj, last_obj, clock_rate, objects, index):
        self.difficulty_hit_objects = objects
        self.index = index
        self.base_object = hit_obj
        self.last_object = last_obj
        self.delta_time = (hit_obj.time - last_obj.time) / clock_rate
        self.start_time = hit_obj.time / clock_rate
        self.end_time = (hit_obj.end_time if hasattr(hit_obj, "end_time") else hit_obj.time) / clock_rate
        
    def previous(self, back_index):
        try:
            return self.difficulty_hit_objects[self.index - (back_index + 1)]
        except IndexError:
            return

    def next(self, forward_index):
        try:
            return self.difficulty_hit_objects[self.index + (forward_index + 1)]
        except IndexError:
            return
