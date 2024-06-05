import gradio as gr
import os
import shutil
import subprocess
import string
import random

# Global variable to store the previous video file name
previous_video_file_name = None

def generate_random_string(length=4):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def run_inference(uploaded_video, uploaded_audio):
    global previous_video_file_name
    
    # Placeholder values
    command = ""
    video_path = ""
    audio_path = ""
    execution_result = "Command not executed."  # Default value assigned
    
    if previous_video_file_name:
        video_file_name = previous_video_file_name
    else:
        video_file_name = generate_random_string() + ".mp4"
        previous_video_file_name = video_file_name

    if not uploaded_video or not uploaded_audio:
        return "Please upload both video and audio files.", "", "", "Please upload both video and audio files."
    
    # Define paths where you want to save the uploaded files
    video_file_path = f"examples/face/{video_file_name}"
    audio_file_path = "examples/audio/audio.wav"
    output_file_path = "results/result.mp4"

    # Ensure directories exist
    for directory in ["examples/face", "examples/audio", "results"]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Save the uploaded files to the specified locations
    shutil.copyfile(uploaded_video, video_file_path)
    shutil.copyfile(uploaded_audio, audio_file_path)

    # Create the command string
    command = f"python inference.py --face {video_file_path} --audio {audio_file_path} --outfile {output_file_path}"

    try:
        execution_result = subprocess.check_output(command, shell=True).decode("utf-8")
        video_path = output_file_path  # set the video_path to the processed video if the command is executed
    except subprocess.CalledProcessError as e:
        execution_result = str(e)

    # Cleanup: Delete temporary video and audio files
    if os.path.exists(video_file_path):
        os.remove(video_file_path)
        previous_video_file_name = None  # Reset the video file name once it's removed
    if os.path.exists(audio_file_path):
        os.remove(audio_file_path)

    return command, video_path, execution_result

def display_uploaded_files(video, audio):
    return video, audio

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Video-Retalking-HQ\nGUI by Shmuel Ronen")
    
    with gr.Row():
        with gr.Column():
            video_input = gr.File(label="Upload Video")
            audio_input = gr.File(label="Upload Audio")
            video_display = gr.Video(label="Uploaded Video")
            audio_display = gr.Audio(label="Uploaded Audio")

        with gr.Column():
            command_output = gr.Textbox(label="Generated Command")
            processed_video_output = gr.Video(label="Processed Video (or Uploaded Video if not processed)")
            execution_result_output = gr.Textbox(label="Execution Result")

    upload_button = gr.Button("Submit")

    def display_files(video, audio):
        return video, audio

    video_input.change(
        fn=display_files,
        inputs=[video_input, audio_input],
        outputs=[video_display, audio_display]
    )

    audio_input.change(
        fn=display_files,
        inputs=[video_input, audio_input],
        outputs=[video_display, audio_display]
    )

    upload_button.click(
        fn=run_inference, 
        inputs=[video_input, audio_input], 
        outputs=[command_output, processed_video_output, execution_result_output]
    )

demo.launch()
