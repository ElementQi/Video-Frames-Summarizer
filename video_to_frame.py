import cv2
import os
import argparse


def extract_frames(video_path, output_folder, num_frames=4):
    """
    Extract frames with mean gap
    """

    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("can't open file")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_indices = [int(i * total_frames / num_frames) for i in range(num_frames)]

    extracted_frames = 0
    for idx in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        if idx in frame_indices:
            frame_filename = os.path.join(
                output_folder, f"frame_{extracted_frames + 1}.jpg"
            )
            cv2.imwrite(frame_filename, frame)
            print(f"Saved frame: {frame_filename}")
            extracted_frames += 1

    cap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract n frames from a video")

    parser.add_argument(
        "--video_path", type=str, required=True, help="Input video path"
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        required=True,
        help="Output video frames images path",
    )
    parser.add_argument(
        "--num_frames", type=int, default=4, help="Frame extract number, default to 4"
    )

    args = parser.parse_args()

    extract_frames(args.video_path, args.output_folder, args.num_frames)
