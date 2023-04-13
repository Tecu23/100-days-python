# Global and local variables
def increase_enemies():
    enemies = 4
    print(f"Enemies inside the function {enemies}")

def increase_enemies_globally():
    global enemies
    enemies = 4
    print(f"Enemies inside the function {enemies}")

enemies = 2

print(f"Enemies outside the function {enemies}")

increase_enemies()

print(f"Enemies outside the function v2 {enemies}")

increase_enemies_globally()

print(f"Enemies outside the function v3 {enemies}")