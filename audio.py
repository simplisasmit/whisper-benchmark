import os
from pydub import AudioSegment
import random


def create_random_audio(input_file, output_dir, num_files, duration, seed):
    random.seed(seed)

    audio = AudioSegment.from_file(input_file)

    os.makedirs(output_dir, exist_ok=True)
    
    duration_ms = duration*1000.0

    for i in range(num_files):
        start_pos_ms = random.uniform(0, len(audio)-duration_ms)
        
        chunk = audio[start_pos_ms:start_pos_ms + duration_ms]
        
        chunk = chunk.set_frame_rate(16000)
        
        output_file = os.path.join(output_dir, f"random_chunk_{i+1}.wav")
        
        chunk.export(output_file, format="wav")
        
        print(f"Created: {output_file}")

    print(f"Used seed: {seed}")
    

def convert_to_wav(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(os.path.basename(input_file))[0]

    audio = AudioSegment.from_file(input_file)

    output_file = os.path.join(output_dir, f"{filename}.wav")

    audio.export(output_file, format="wav")

    print(f"Converted {input_file} to {output_file}")
    return output_file