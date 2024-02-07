import numpy as np
import matplotlib.pyplot as plt

def plot_chernoff_face(features):
    fig, ax = plt.subplots()

    # Set axis limits
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    # Draw face outline
    face_outline = plt.Circle((0, 0), 1, color='lightgray', fill=True)
    ax.add_patch(face_outline)

    # Extract features
    eye_size = features[0]
    eye_spacing = features[1]
    eye_height = features[2]
    eye_color = tuple(features[3:6])  # Use a tuple for RGB color
    eye1_x = -eye_spacing / 2
    eye2_x = eye_spacing / 2

    # Draw eyes
    eye1 = plt.Circle((eye1_x, 0.25), eye_size, color=eye_color, fill=True)
    eye2 = plt.Circle((eye2_x, 0.25), eye_size, color=eye_color, fill=True)

    # Draw nose
    nose_height = features[6]
    nose_width = features[7]
    nose = plt.Rectangle((-nose_width / 2, -nose_height / 2), nose_width, nose_height, color='saddlebrown', fill=True)

    # Draw mouth
    mouth_width = features[8]
    mouth_height = features[9]
    mouth = plt.Rectangle((-mouth_width / 2, -0.75), mouth_width, mouth_height, angle=0, color='red', fill=True)

    # Add features to the plot
    ax.add_patch(eye1)
    ax.add_patch(eye2)
    ax.add_patch(nose)
    ax.add_patch(mouth)

    # Remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

# Example: Randomly generated features
random_features = np.random.rand(10)
plot_chernoff_face(random_features)
