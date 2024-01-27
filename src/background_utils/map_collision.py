from PIL import Image

def generate_collision_map(image_path, output_path):
    image = Image.open(image_path)
    width, height = image.size

    # Create a list to store collision information
    collision_map = [['0' for _ in range(width)] for _ in range(height)]

    # Iterate through each pixel in the image
    for y in range(height):
        for x in range(width):
            # Check if the pixel color indicates an obstacle (adjust the color based on your background image)
            pixel_color = image.getpixel((x, y))
            if pixel_color == (0, 0, 0):  # Assuming black color represents obstacles
                collision_map[y][x] = '1'

    # Save collision map to a text file
    with open(output_path, 'w') as file:
        for row in collision_map:
            file.write(' '.join(row) + '\n')

# Example usage
generate_collision_map('../../images/background.jpg', '../../collision_map.txt')