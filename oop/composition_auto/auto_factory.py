from autos.auto import Door, Wheel, Engine, Body, Auto

# new_door = Door("automatic")
# print(new_door.close())

# new_wheel = Wheel("large", "Pirelli")
# print(new_wheel.stop())

# new_engine = Engine("Gasoline", "four cilinder")
# print(new_engine.stop())

# new_body = Body("Metal", True, False)
# print(new_body.open_roof())

new_auto = Auto("car", "diesel", 1.6, "carbon fibre", True, True)
print(new_auto.drive())
print(new_auto.stop())
print(new_auto.description())