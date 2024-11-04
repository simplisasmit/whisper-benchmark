import os
from pydub import AudioSegment
import random


def create_random_audio(input_file, output_dir, num_files, duration_range, seed):
    random.seed(seed)

    audio = AudioSegment.from_file(input_file)

    os.makedirs(output_dir, exist_ok=True)

    for i in range(num_files):
        duration = random.uniform(duration_range[0], duration_range[1])
        duration_ms = int(duration * 1000)
        
        max_start = len(audio) - duration_ms
        start_pos = random.randint(0, max_start)
        
        chunk = audio[start_pos:start_pos + duration_ms]
        
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