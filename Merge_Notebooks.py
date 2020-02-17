from nbmerge import merge_notebooks, write_notebook
import io, os


def merge_notebooks_function(path_to_notebooks,
                             notebook_names=['Download_Data.ipynb','DeepBox.ipynb',
                                             'Data_Curation.ipynb','Liver_Model.ipynb'],
                             combined_notebook_path=os.path.join('.','Click_Me.ipynb')):
    file_paths = [os.path.join(path_to_notebooks,i) for i in notebook_names]
    merged = merge_notebooks(base_dir=path_to_notebooks,file_paths=file_paths, verbose=True)
    with io.open(combined_notebook_path, 'w', encoding='utf8') as fp:
        write_notebook(merged, fp)

    return None


if __name__ == '__main__':
    pass
