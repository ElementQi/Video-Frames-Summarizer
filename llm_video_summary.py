from openai import OpenAI
import base64
import argparse
import os


def get_image_as_base64(image_path):
    """
    :param image_path: local image file path
    :return: Base64 encoded string with format data:image/jpeg;base64,<encoded_string>
    """
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

        base64_encoded = base64.b64encode(image_data).decode("utf-8")
        return f"data:image/jpeg;base64,{base64_encoded}"


def get_images_from_folder(folder_path, num_images=4):
    """
    :param folder_path
    :param num_images: default 4
    :return: Base64 list of images(string)
    """

    image_files = [
        f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png"))
    ]

    if len(image_files) < num_images:
        raise ValueError(f"at least {num_images} images")

    selected_images = image_files[:num_images]

    base64_images = [
        get_image_as_base64(os.path.join(folder_path, img)) for img in selected_images
    ]
    return base64_images


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Put frame images from video to Multimodal LLM to do summarization."
    )

    parser.add_argument("--base_url", type=str, required=True, help="API base URL")
    parser.add_argument("--model_id", type=str, required=True, help="Model ID")
    parser.add_argument("--apikey", type=str, required=True, help="Your api key file")
    parser.add_argument(
        "--frame_folder_path", type=str, required=True, help="Image file folder"
    )
    parser.add_argument(
        "--num_images", type=int, default=4, help="Frame extract number, default to 4"
    )

    args = parser.parse_args()

    with open(args.apikey, "r") as f:
        apikey = f.read().strip()

    client = OpenAI(api_key=apikey, base_url=args.base_url)

    base64_images = get_images_from_folder(args.frame_folder_path)

    response = client.chat.completions.create(
        model="Qwen2-VL",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "请理解该视频。这是从视频中提取的 4 帧图片，它们按顺序排列。根据这些帧，推测视频中的主要内容和事件。",
                    },
                    *[
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": base64_image,
                            },
                        }
                        for base64_image in base64_images
                    ],
                ],
            },
        ],
    )

    print(response.choices[0].message.content)
