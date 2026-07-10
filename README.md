# Workshop_Modules

Teaching notebooks for a hands-on deep-learning workshop that walks through training
a 2D liver segmentation model on CT images with TensorFlow/Keras. Teaching material,
not a maintained library.

The workshop is provided in two parallel versions:

- `TF_1/` — TensorFlow 1.x version
- `TF_2/` — TensorFlow 2.x version

Each folder contains the same sequence of notebooks, meant to be worked through in order:

- `Download_Data_Template.ipynb` — fetch the workshop dataset
- `DeepBox.ipynb` — supporting deep-learning building blocks
- `Data_Curation.ipynb` — prepare TFRecords / train/validation/test splits
- `Liver_Model.ipynb` — build image processors, train the liver segmentation model, and view results (TensorBoard)
- `Merge_Notebooks.py` — merges the notebooks above into a single runnable `Click_Me.ipynb` (uses `nbmerge`)

## Requirements

- Python with Jupyter, TensorFlow (1.x or 2.x depending on folder)
- The author's `Deep_Learning` / `Base_Deeplearning_Code` code on the path — the
  notebooks import data generators, callbacks, and plotting helpers from it
- `nbmerge` (only for `Merge_Notebooks.py`)

## Notes

The notebooks resolve paths by searching parent directories for `Deep_Learning` and
`Data` folders, so they expect to run inside that surrounding project layout. Last
updated in 2020; pinned to the TensorFlow versions of that era.
