import cv2
import argparse
from typing import Tuple

class Box:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def dimensions(self) -> Tuple[int, int]:
        return self.w, self.h


class Label:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def calculate_label_closeness_and_offset(image_path: str, display: bool = False) -> None:
    """
    Detects the box and label in an image, calculates their closeness, and offset.

    Args:
        image_path: Path to the image file.
        display: Whether to display the image with detected objects. Default is False.

    Returns:
        None
    """
    img = cv2.imread(image_path)

    # Box Detection (using edge detection)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, 50, 150)
    contours_edges, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour_edges = max(contours_edges, key=cv2.contourArea)
    approx = cv2.approxPolyDP(largest_contour_edges, 0.04 * cv2.arcLength(largest_contour_edges, True), True)
    if len(approx) == 4:  # Assuming box is a quadrilateral
        x_box, y_box, w_box, h_box = cv2.boundingRect(largest_contour_edges)
        box = Box(x_box, y_box, w_box, h_box)
        print("Box dimensions (edges):", *box.dimensions())

    # Label Detection (refined)
    thresh_label = cv2.threshold(gray_img, 240, 255, cv2.THRESH_BINARY)[1]
    contours_label, _ = cv2.findContours(thresh_label, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour_label = max(contours_label, key=cv2.contourArea)
    x_label, y_label, w_label, h_label = cv2.boundingRect(largest_contour_label)
    label = Label(x_label, y_label, w_label, h_label)

    # Calculate label closeness
    if contours_label and contours_edges:
        bottom_closeness = ((box.y + box.h) - label.y) / box.h * 100
        print("Closeness to bottom side:", round(bottom_closeness, 2) - 100, "%")

        right_closeness = ((box.x + box.w) - label.x) / box.w * 100
        print("Closeness to right side:", round(right_closeness, 2) - 100, "%")

    # Calculate label offset
    x_offset = label.x - box.x
    y_offset = label.y - box.y

    # Display image with detected objects if required
    if display:
        cv2.rectangle(img, (x_box, y_box), (x_box + w_box, y_box + h_box), (0, 255, 0), 2)  # Draw box
        cv2.rectangle(img, (x_label, y_label), (x_label + w_label, y_label + h_label), (255, 0, 0), 2)  # Draw label
        cv2.imshow("Detected Objects", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect box and label in an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    parser.add_argument("--display", action="store_true", help="Display the image with detected objects.")
    
    args = parser.parse_args()
    
    calculate_label_closeness_and_offset(args.image_path, args.display)