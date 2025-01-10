
default:
    ludwig train --dataset "export - Score - Grid_cleaned.csv" -c config.yaml

activate:
    micromamba activate twitter_bot

evaluate:
    ludwig evaluate \
        --model_path results/experiment_run/model \
        --dataset "export - Score - Grid_cleaned.csv" \
        --split test \
        --output_directory test_results

install:
    micromamba install python==3.10 -c conda-forge
    micromamba install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
    micromamba install -y torchtext -c pytorch
    pip install git+https://github.com/huggingface/transformers.git # Until the next transformers release, you must install it directly from GitHub like so to use ModernBert:
    pip install ludwig