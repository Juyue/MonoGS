import os, pathlib
import cv2
import os

home_dir = str(pathlib.Path.home())
print(home_dir)
input_path =  "datasets/umi/demo_sessions/20240424_pick/raw_videos/mapping.mp4"
output_dir = "datasets/umi_3dgs/rgb_20240424_pick_mapping_tmp"

video_path = os.path.join(home_dir, input_path)
output_dir = os.path.join(home_dir, output_dir)

if not os.path.exists(video_path):
    print(f"Video file not found: {video_path}")

# Create a directory to store the extracted images
rgb_output_dir = os.path.join(output_dir, "rgb") 
os.makedirs(rgb_output_dir, exist_ok=True)

# Create a txt to store the rgb.txt
rgb_txt_path = os.path.join(output_dir, "rgb.txt")
rgb_txt_file = open(rgb_txt_path, "w")

# write the header of the rgb.txt
rgb_txt_file.write("# color images\n")
rgb_txt_file.write(f"# file: '{video_path}'\n")
rgb_txt_file.write("# timestamp filename\n")

# Create a txt to store the output of ORB_SLAM3 trajectory
# Open the MP4 file
cap = cv2.VideoCapture(video_path)

# Get the video's frame rate
fps = cap.get(cv2.CAP_PROP_FPS)

# Initialize the frame counter
frame_count = 0

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Calculate the timestamp based on the frame count and FPS
    timestamp = frame_count / fps

    print(f"Processing frame {frame_count} at timestamp {timestamp:.6f}")

    # Generate the filename with the timestamp
    filename = f"{timestamp:.6f}.png"
    filepath = os.path.join(rgb_output_dir, filename)

    # Save the frame as an image
    cv2.imwrite(filepath, frame)

    # Save the timestamp and filename to the rgb.txt
    rgb_txt_file.write(f"{timestamp:.6f} rgb/{filename}\n")

    # Increment the frame counter
    frame_count += 1
    if frame_count >= 1000:
        break

# Release the video capture object
cap.release()
rgb_txt_file.close()

# Also, write the txt