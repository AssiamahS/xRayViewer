import pydicom
import matplotlib.pyplot as plt

def show_xray(file_path):
    # Read the DICOM file
    dicom_file = pydicom.dcmread(file_path)
    
    # Extract the pixel data
    pixel_array = dicom_file.pixel_array
    
    # Display the image
    plt.imshow(pixel_array, cmap=plt.cm.bone)
    plt.show()

# Example usage
file_path = 'path_to_your_dicom_file.dcm'
show_xray(file_path)
