from audio import *
import os
from faster_whisper.feature_extractor import FeatureExtractor
from benchmark import *
from faster_whisper import BatchedInferencePipeline


def process(model,audio_files,duration):
    gpu_name = get_gpu_name()
    print(f"Using device: {gpu_name}")

    latencies = process_audio_files(audio_files, model)

    p25, p50, p90, p99, avg = calculate_metrics(latencies)

    save_results_to_csv(gpu_name, p25, p50, p90, p99, avg, duration)
    
model = WhisperModel("whisper-large-v3-turbo", device="cuda", compute_type="float16",)


# duration = 1
# dir = f"{duration}_min_random"
# audio_files = [os.path.join(dir,item) for item in os.listdir(dir) if item.endswith('.wav')]

# process(model,audio_files,duration)

# duration = 5
# dir = f"{duration}_min_random"
# audio_files = [os.path.join(dir,item) for item in os.listdir(dir) if item.endswith('.wav')]

# process(model,audio_files,duration)

duration = 10
dir = f"{duration}_min_random"
audio_files = [os.path.join(dir,item) for item in os.listdir(dir) if item.endswith('.wav')]

process(model,audio_files,duration)