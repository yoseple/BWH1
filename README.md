Project Overview:

A pipeline where you can upload a CT scan in NIfTI format (nii.gz file), which then segments the lower lumbar region of the scan. This process includes the segmentation of the disks within the scan. Following segmentation, 
the file undergoes a conversion from nii.gz to .obj format. The result can then be viewed in a 3D plane using the Three.js Model Viewer. With this pipeline, you have the option to either download the .obj file or view it using
Three.js.

How it works:
Using the Verse Dataset which has all the 

















Sources used: 
  Dolz J, Desrosiers C, Ben Ayed I. IVD-Net: Intervertebral disc localization and segmentation in MRI with a multi-modal UNet. arXiv preprint arXiv:1811.08305. 2018 Nov 19.

  Sekuboyina A et al., VerSe: A Vertebrae Labelling and Segmentation Benchmark for Multi-detector CT Images, 2021.
  In Medical Image Analysis: https://doi.org/10.1016/j.media.2021.102166
  Pre-print: https://arxiv.org/abs/2001.09193

  Löffler M et al., A Vertebral Segmentation Dataset with Fracture Grading. Radiology: Artificial Intelligence, 2020.
  In Radiology AI: https://doi.org/10.1148/ryai.2020190138

  Liebl H and Schinz D et al., A Computed Tomography Vertebral Segmentation Dataset with Anatomical Variations and Multi-Vendor Scanner Data, 2021.
  Pre-print: https://arxiv.org/pdf/2103.06360.pdf

  Wasserthal, J., Breit, H.-C., Meyer, M.T., Pradella, M., Hinck, D., Sauter, A.W., Heye, T., Boll, D., Cyriac, J., Yang, S., Bach, M., Segeroth, M., 2023. TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images. Radiology: Artificial Intelligence. https://doi.org/10.1148/ryai.230024
    
  https://github.com/neurolabusc/nii2mesh
