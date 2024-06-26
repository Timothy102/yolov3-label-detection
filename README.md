# yolov3-label-detection

Hey, team. This is beyond the scope of my 2-hour task. 

### Worfklow

Yolov3 sucked for detecting boxes and corresponding labels largely because it was trained on the COCO dataset and/or might require a fine-tuning solution. We can always do it.

Here's what I did: 

1. used pure OpenCV to detect the box(largest area surface)
2. then used this annotated area to retrieve the area with the label
3. In the manual, it states: 2 inch from bottom and vertical edge. That's what I calculate - both absolute and relative offset for the label to the box. If we have this, we can easily set a threshold for what we consider a valid label and set notifications back to main chargeback system.

## How to Run This

1. Create a Python venv
```
python3 -m venv venv
source venv/bin/activate
```

2. Run the get_image.py script to extract the image with the box from page 45 of the manual you gave me.

```
python3 get_image.py
```

Or bring any other image locally.

3. Run the main script which runs OpenCV to detect images and calculate offset.

```
python3 main.py --display=0
```

### Resulting Example

Box dimensions (edges): 542 237

Closeness to bottom side: 9.280000000000001 %

Closeness to right side: 4.980000000000004 %

![Image Outlining the Box and the Label](outline.png)

### Next Steps From Here:

1. Use Apple Photos Kit(Jaden's idea) to capture the box taken via phone.
2. Build a real-time pipeline that connects to our mainframe notification system.
3. Test it(1000x), streamline on Cloud.
3. Integrate with the tablet.