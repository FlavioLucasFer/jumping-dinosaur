from typing import List
from uuid import UUID

from object import Object
		  
__objects: List[Object]=[]

def render_obj(object: Object) -> Object:
	global __objects

	__objects.append(object)
	return object

def unrender_obj(object: Object) -> Object:
	global __objects

	__objects.remove(object)
	return object

def unrender_obj(uuid: UUID) -> Object:
	global __objects

	for object in __objects:
		if object.uuid == uuid:
			__objects.remove(object)
			return object
			
def render_objects():
	global __objects

	for object in __objects:
		print(__objects)
		object.render()

def rendered_object() -> int:
	global __objects

	return len(__objects)
