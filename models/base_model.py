#!/usr/bin/python3
import uuid
from datetime import datetime
"""A super class that defines all common attributes/methods for other classes"""

class BaseModel:
    """Represents a super class"""

    def __init__(self):
        self.cretaed_at = datetime.now()



my_model = BaseModel()

print(my_model.cretaed_at)
