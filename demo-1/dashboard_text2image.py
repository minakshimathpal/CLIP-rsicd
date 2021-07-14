import matplotlib.pyplot as plt
import nmslib
import numpy as np
import os
import streamlit as st

from transformers import CLIPProcessor, FlaxCLIPModel


BASELINE_MODEL = "openai/clip-vit-base-patch32"
IMAGE_VECTOR_FILE = "/home/shared/data/vectors/test-baseline.tsv"
IMAGES_DIR = "/home/shared/data/RSICD_images"


@st.cache(allow_output_mutation=True)
def load_index():
    filenames, image_vecs = [], []
    fvec = open(IMAGE_VECTOR_FILE, "r")
    for line in fvec:
        cols = line.strip().split('\t')
        filename = cols[0]
        image_vec = np.array([float(x) for x in cols[1].split(',')])
        filenames.append(filename)
        image_vecs.append(image_vec)
    V = np.array(image_vecs)
    index = nmslib.init(method='hnsw', space='cosinesimil')
    index.addDataPointBatch(V)
    index.createIndex({'post': 2}, print_progress=True)
    return filenames, index


@st.cache(allow_output_mutation=True)
def load_model():
    model = FlaxCLIPModel.from_pretrained(BASELINE_MODEL)
    processor = CLIPProcessor.from_pretrained(BASELINE_MODEL)
    return model, processor


def app():
    filenames, index = load_index()
    model, processor = load_model()

    st.title("Text to Image Retrieval")
    query = st.text_input("Text Query:")
    if st.button("Query"):
        inputs = processor(text=[query], images=None, return_tensors="jax", padding=True)
        query_vec = model.get_text_features(**inputs)
        query_vec = np.asarray(query_vec)
        ids, distances = index.knnQuery(query_vec, k=10)
        result_filenames = [filenames[id] for id in ids]
        images, captions = [], []
        for result_filename, score in zip(result_filenames, distances):
            images.append(
                plt.imread(os.path.join(IMAGES_DIR, result_filename)))
            captions.append("{:s} (score: {:.3f})".format(result_filename, score))
        st.image(images[0:3], caption=captions[0:3])
        st.image(images[3:6], caption=captions[3:6])
        st.image(images[6:9], caption=captions[6:9])
        st.image(images[9:], caption=captions[9:])