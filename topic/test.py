import cv2
import pytube

# Function to download YouTube video
def download_video(url, output_path):
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(file_extension='mp4', res='360p').first()  # Adjust resolution as needed
    stream.download(output_path)

# Function to extract frames from video with specified frame interval
def extract_frames(video_path, output_folder, frame_interval_sec=1):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break
        if frame_count % int(frame_interval_sec * fps) == 0:
            frame_path = f"{output_folder}/frame_{frame_count}.jpg"
            cv2.imwrite(frame_path, frame)
            print(f"Frame {frame_count} saved")
        frame_count += 1

        # To break the loop at frame 100
        if frame_count == 100:
            break

    cap.release()

if __name__ == "__main__":
    video_url = "https://youtu.be/dQw4w9WgXcQ?si=bO_VUuy6MStL0iJb"
    output_folder = "topic\\vid"
    # The interval between frames in seconds
    # In this example, a 30fps video will be extracted every 0.1 seconds
    frame_interval_sec = 0.1

    # # Download video
    # print("Downloading video...")
    # download_video(video_url, output_folder)

    print("Extracting frames from video...")
    video_path = f"{output_folder}/video.mp4"
    extract_frames(video_path, output_folder, frame_interval_sec)

    print("Frames extraction complete!")

