# Video to Text Converter

This project converts audio from MP4 video files to text using OpenAI's Whisper speech recognition model. It can process a single video file or recursively process all MP4 files in a directory and its subdirectories.

## Features

- Extracts audio from MP4 video files
- Converts audio to text using OpenAI's Whisper model
- Supports different Whisper model sizes for balancing speed and accuracy
- Processes multiple video files recursively in a directory
- Displays progress bar during processing

## Installation

1. Clone the repository:

2. 2. Navigate to the project directory:
  
   3. 3. Install the required dependencies:
     
## Usage

1. Open the `video_to_text.py` file and set the following variables:
- `INPUT_DIR`: Path to the directory containing the MP4 video files.
- `OUTPUT_DIR`: Path to the directory where the extracted text files will be saved.
- `MODEL_SIZE`: Whisper model size to use ('tiny', 'base', 'small', 'medium', 'large').

Run the script:

The script will process all the MP4 files in the specified input directory and its subdirectories. The extracted text will be saved as individual text files in the specified output directory.

## License

This project is licensed under the [MIT License](LICENSE).

