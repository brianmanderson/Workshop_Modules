from nbmerge import merge_notebooks, write_notebook
import io, os


def merge_notebooks_function(path_to_notebooks='.',notebook_paths=['.\\Download_Data_Template.ipynb','.\\DeepBox.ipynb',
                                                                   '.\\Data_Curation.ipynb','.\\Liver_Model.ipynb'],
                             notebook_output_path=os.path.join('.','Click_Me.ipynb')):
    '''
    :param path_to_notebooks: Base_dir, rather unneeded
    :param notebook_paths: list of full paths to notebooks
    :param notebook_output_path: path to output notebook
    :return:
    '''
    merged = merge_notebooks(base_dir=path_to_notebooks,file_paths=notebook_paths, verbose=True)
    with io.open(notebook_output_path, 'w', encoding='utf8') as fp:
        write_notebook(merged, fp)

    return None


if __name__ == '__main__':
    pass
