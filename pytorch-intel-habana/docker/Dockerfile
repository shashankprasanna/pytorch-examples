FROM vault.habana.ai/gaudi-docker/1.8.0/ubuntu20.04/habanalabs/pytorch-installer-1.13.1:latest
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install autoconf automake gdb git libffi-dev zlib1g-dev libssl-dev libsndfile1 -y
RUN pip install jupyterlab ipykernel matplotlib ipywidgets
RUN pip install huggingface transformers datasets
RUN pip install diffusers["torch"] accelerate soundfile librosa
WORKDIR /pytorch-habana
ENTRYPOINT ["jupyter", "lab", "--ip='*'", "--NotebookApp.token=''", "--NotebookApp.password=''","--allow-root"]
