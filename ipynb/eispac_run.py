import eispac 
from eispac_fit import eispac_fit
from glob import glob 
import os 

if __name__ == "__main__":

    data_filepaths = sorted(glob("../data/*.data.h5"))
    save_dir = "../results/"

    fe_12_195_1c_template = "../templates/fe_12_195_119.1c.template.h5"
    fe_08_185_1c_template = "../templates/fe_08_185_213.1c.template.h5"


    for data_filepath in data_filepaths:
        if not os.path.exists(
            os.path.join(save_dir, os.path.basename(data_filepath).replace(".data.h5", ".fe_12_195_119.1c-0.fit.h5"))
            ):
            eispac_fit(data_filepath, fe_12_195_1c_template, save_dir=save_dir, ncpu=4)
    
    eispac_fit(data_filepaths[2], fe_08_185_1c_template, save_dir=save_dir, ncpu=4)