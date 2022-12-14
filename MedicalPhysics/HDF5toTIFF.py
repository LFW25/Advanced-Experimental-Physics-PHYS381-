# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 10:35:25 2022

@author: Lily Williams
"""
from pathlib import Path
import numpy as np
import h5py as h5
import time
import cv2
import os



def convertMarsHDF(pathFound, filePath, pathSave):
    """
    Takes the location of a .hdf5 file and saves .tiff images, sorted into folders by bin

    Parameters
    ----------
    pathFound : String
        Contains the string describing the folder location of a "reconstructed.hdf5" file
        String ends in the FOLDER ("/Folder")
    filePath : String
        Contains the string describing the location of a "reconstructed.hdf5" file
        String ends in the FILE ("/reconstructed.hdf5")
    pathSave : String
        Contains the string describing the folder where you want to save the .TIFF images

    Returns
    -------
    None.

    """
    os.chdir(pathFound) ### Change current dir to pathFound
    
    with h5.File(filePath, 'r') as hf:
        # Open the HDF5 File
        fileKeys = list(hf.keys())
        imageDS = hf[fileKeys[0]]
        print(f'Image Dataset info: Shape={imageDS.shape},Dtype={imageDS.dtype}')
        
        for binCount in range(imageDS.shape[0]):
            # Create new folder for each bin
            binFolder = os.path.join(pathSave, "Bin{}".format(binCount))
            
            try: 
                os.mkdir(binFolder) 
            except OSError as error: 
                pass
            
            # Move into new bin folder
            os.chdir(binFolder)
            for img in range(imageDS.shape[1]):
                # Check if the conversion has already been done (Saves a LOT of processing)
                # With Check: 10876.897811889648 ms
                # Without Check: 39927.45542526245 ms
                
                imageName = f'bin{binCount}_img{img}.tiff'
                
                if os.path.exists(imageName) == False:
                    # Save .TIFF images into the bin folder
                    print(f"Processing {imageName}... ")
                    cv2.imwrite(imageName, imageDS[binCount, img, :]) # uses slice notation
                    print("Done.\n")
                else:
                    pass
                # =============================================================================
                #         Doing this conversion is Insanely faster working on the SSD
                #         global startTime
                #         timeDiff = (time.time() - startTime) * 1000
                #         print(timeDiff)
                # =============================================================================


def convertXineHDF(pathFound, filePath, pathSave):
    """
    Takes the location of a .hdf5 file and saves .tiff images.

    Parameters
    ----------
    pathFound : String
        Contains the string describing the folder location of a "reconstructed.hdf5" file
        String ends in the FOLDER ("/Folder")
    filePath : String
        Contains the string describing the location of a "reconstructed.hdf5" file
        String ends in the FILE ("/reconstructed.hdf5")
    pathSave : String
        Contains the string describing the folder where you want to save the .TIFF images

    Returns
    -------
    None.

    """
    os.chdir(pathFound) ### Change current dir to pathFound
    
    with h5.File(filePath, 'r') as hf:
        
        
        # Open the HDF5 File
        fileKeys = list(hf.keys())
        imageDS = hf[fileKeys[0]]
        print(f'Image Dataset info: Shape={imageDS.shape},Dtype={imageDS.dtype}')
        
        depth = imageDS.shape[0]
        height = imageDS.shape[1]
        width = imageDS.shape[2]
        
        os.chdir(pathSave)
        for img in range(imageDS.shape[0]):
            # Check if the conversion has already been done (Saves a LOT of processing)

            imageName = f'img{img}.tiff'
            if os.path.exists(imageName) == False:
                print(f"Processing {imageName}... ")
                # Save .TIFF images into the bin folder
                cv2.imwrite(imageName, imageDS[img, :]) # uses slice notation
                print("Done.")
            else:
                pass



rootdir = "D:\lfw25\IMBL_Apr2021_Jannis"
fileSearch = "reconstructed.hdf5"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == fileSearch:
            pathFound = subdir
            filePath = os.path.join(subdir, file)
            pathSave = os.path.join(subdir, "ReconstructedImages")
            
            try: 
                os.mkdir(pathSave) 
            except OSError as error: 
                pass
            
            #startTime = time.time()
            if "MARS" in filePath:
                # Detector Type is MARS
                convertMarsHDF(pathFound, filePath, pathSave)
            else:
                # Detector Type is XINEA
                convertXineHDF(pathFound, filePath, pathSave)
                