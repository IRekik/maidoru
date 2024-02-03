def generate_collision_map(image_path):
    coordinate_list = []
    with open(image_path) as file:
        lines = file.readlines()
        for i in range(len(lines) - 1):
            start_coordinate = list(map(int, lines[i].rstrip().split()))
            end_coordinate = list(map(int, lines[i + 1].rstrip().split()))

            x1, y1 = start_coordinate
            x2, y2 = end_coordinate

            # Generate coordinates between the start and end points
            if x1 == x2:
                coordinates_between = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
            elif y1 == y2:
                coordinates_between = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
            else:
                # Handle diagonal walls (optional)
                # You can customize this part based on your needs
                # For simplicity, this example assumes diagonal walls are treated as separate walls
                coordinates_between = []

            coordinate_list.extend(coordinates_between)

    # Add the last coordinate from the file
    last_coordinate = list(map(int, lines[-1].rstrip().split()))
    coordinate_list.append(tuple(last_coordinate))

    return coordinate_list
