import os
import time
import csv
import numpy as np
from faster_whisper import WhisperModel
import torch

def get_gpu_name():
    if torch.cuda.is_available():
        return torch.cuda.get_device_name(0)
    else:
        return "CPU"

def process_audio_files(audio_files, model):
    latencies = []
    for audio_file in audio_files:
        start_time = time.time()
        segments, _ = model.transcribe(audio_file)

        list(segments)
        end_time = time.time()
        latency = end_time - start_time
        latencies.append(latency)
        print(f"Processed {audio_file} in {latency:.2f} seconds")
    return latencies

def calculate_metrics(latencies):
    latencies_array = np.array(latencies)
    p25 = np.percentile(latencies_array, 25)
    p50 = np.percentile(latencies_array, 50)
    p90 = np.percentile(latencies_array, 90)
    p99 = np.percentile(latencies_array, 99)
    avg = np.mean(latencies_array)
    return p25, p50, p90, p99, avg

def save_results_to_csv(gpu_name, p25, p50, p90, p99, avg):
    filename = f"whisper_latency_{gpu_name.replace(' ', '_')}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Metric', 'Value (seconds)'])
        writer.writerow(['GPU', gpu_name])
        writer.writerow(['p25', f'{p25:.2f}'])
        writer.writerow(['p50', f'{p50:.2f}'])
        writer.writerow(['p90', f'{p90:.2f}'])
        writer.writerow(['p99', f'{p99:.2f}'])
        writer.writerow(['avg', f'{avg:.2f}'])
    print(f"Results saved to {filename}")

def main():
    gpu_name = get_gpu_name()
    print(f"Using device: {gpu_name}")

    audio_files = []

    model = WhisperModel("whisper-large-v3-turbo", device="cuda", compute_type="float16")

    latencies = process_audio_files(audio_files, model)

    p25, p50, p90, p99, avg = calculate_metrics(latencies)

    save_results_to_csv(gpu_name, p25, p50, p90, p99, avg)

if __name__ == "__main__":
    main()