import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_face():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw the head (circle)
    head = patches.Circle((0.5, 0.5), radius=0.4, edgecolor='black', facecolor='none')
    ax.add_patch(head)

    # Draw the eyes (circles)
    left_eye = patches.Circle((0.35, 0.65), radius=0.05, edgecolor='black', facecolor='black')
    right_eye = patches.Circle((0.65, 0.65), radius=0.05, edgecolor='black', facecolor='black')
    ax.add_patch(left_eye)
    ax.add_patch(right_eye)

    # Draw the mouth (ellipse)
    mouth = patches.Ellipse((0.5, 0.35), width=0.2, height=0.1, edgecolor='black', facecolor='none')
    ax.add_patch(mouth)

    # Set aspect ratio to be equal and remove axes
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Show the plot
    plt.show()

# Call the function to draw the face
draw_face()
