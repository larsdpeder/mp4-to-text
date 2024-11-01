import os
import whisper
from moviepy.editor import VideoFileClip
from tqdm import tqdm

def convert_mp4_to_text(video_path, output_dir, model):
    """
    Convert audio from an MP4 file to text using Whisper and save it.
    
    Args:
        video_path (str): Path to the MP4 file
        output_dir (str): Directory to save the text file
        model: Loaded Whisper model instance
    """
    try:
        # Extract filename without extension
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        
        # Create temporary audio file path
        temp_audio = os.path.join(output_dir, f"{base_name}_temp.wav")
        
        # Extract audio from video
        print(f"Extracting audio from {video_path}...")
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(temp_audio, verbose=False, logger=None)
        video.close()
        
        # Convert audio to text using Whisper
        print(f"Converting audio to text...")
        result = model.transcribe(temp_audio)
        text = result["text"]
        
        # Save text to file
        text_file_path = os.path.join(output_dir, f"{base_name}.txt")
        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        # Clean up temporary audio file
        os.remove(temp_audio)
        
        print(f"Successfully created {text_file_path}")
        
    except Exception as e:
        print(f"Error processing {video_path}: {str(e)}")

def process_directory(input_dir, output_dir, model_size="base"):
    """
    Recursively process all MP4 files in a directory and its subdirectories.
    
    Args:
        input_dir (str): Input directory to search for MP4 files
        output_dir (str): Output directory for text files
        model_size (str): Whisper model size ('tiny', 'base', 'small', 'medium', 'large')
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load Whisper model
    print(f"Loading Whisper {model_size} model...")
    model = whisper.load_model(model_size)
    
    # Find all MP4 files
    mp4_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.mp4'):
                mp4_files.append(os.path.join(root, file))
    
    print(f"Found {len(mp4_files)} MP4 files")
    
    # Process each MP4 file with progress bar
    for mp4_file in tqdm(mp4_files, desc="Processing videos"):
        convert_mp4_to_text(mp4_file, output_dir, model)

def main():
    """
    Main function with configuration options
    """
    # Set your input and output directories here
    INPUT_DIR = "path/to/your/videos"
    OUTPUT_DIR = "path/to/output/texts"
    
    # Choose model size:
    # - 'tiny': Fastest, least accurate
    # - 'base': Good balance of speed and accuracy
    # - 'small': More accurate than base, but slower
    # - 'medium': Even more accurate, but slower
    # - 'large': Most accurate, but slowest and requires more RAM
    MODEL_SIZE = "base"
    
    process_directory(INPUT_DIR, OUTPUT_DIR, MODEL_SIZE)

if __name__ == "__main__":
    main()
