FROM ghcr.io/pytorch/pytorch-nightly:latest
#RUN apt-get update
#RUN apt-get install build-essential -y
RUN apt-get install graphviz autoconf automake gdb git libffi-dev zlib1g-dev libssl-dev libsndfile1 -y
RUN pip install jupyterlab ipykernel matplotlib ipywidgets
RUN pip install pydot huggingface transformers datasets
RUN pip install diffusers["torch"] accelerate soundfile librosa
# RUN jupyter labextension disable "@jupyterlab/apputils-extension:announcements"
ENTRYPOINT ["jupyter", "lab", "--ip='*'", "--NotebookApp.token=''", "--NotebookApp.password=''","--allow-root"]
