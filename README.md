# Improving Action Recognition using Temporal Regions

**[This page is still a work in progress!]**

This page contains a supplemental material to the extended version of the paper accepted in the The Symposium on Knowledge Discovery, Mining and Learning (KDMiLe) by João P. Aires, Juarez Monteiro, Roger Granada, Felipe Meneguzzi and Rodrigo C. Barros. The full text can be found in [KDMiLe proceedings](http://www.facom.ufu.br/~kdmile/proceedings/anais-kdmile-2017.pdf).

---
## Abstract

Recognizing actions in videos is an important task in computer vision area, having important applications such as the surveillance and assistance of the sick and disabled. Automatizing this task can improve the way we monitor actions since it is not necessary to have a human watching a video all the time. However, the classification of actions in a video is challenging since we have to identify temporal features that best represent each action. In this work, we propose an approach to obtain temporal features from videos by dividing the sequence of frames of a video into regions. Frames from these regions are merged in order to identify the temporal aspect that classifies actions in a video. Our approach yields better results when compared to a frame-by-frame classification.

---
## Method

Recognizing actions from videos often involves an analysis of how objects in frames modify along the time.
An approach for action recognition in videos involves obtaining the temporal information, which may contain descriptions about how objects are moving and the main modifications between frames.
Since an action consists of a sequence of movements, obtaining the temporal information may help systems to better understand which action is being performed.
In this work, we propose an approach to obtain temporal information from a video by dividing its frames into regions.
Thus, instead of classifying an action using only the information of each frame, we extract and merge the information from several regions of the video in order to obtain its temporal aspect.
The [Figure](#image) bellow illustrates the pipeline of our architecture, which is divided into four phases:

1. Pre-processing
2. CNNs
3. Regions Division
4. Classification

[image]: pipeline.png "Pipeline of our architecture for action recognition using multiple regions"
![Alt text][image]

For more details about the phases you can check our paper at [KDMiLe proceedings](http://www.facom.ufu.br/~kdmile/proceedings/anais-kdmile-2017.pdf).


---
## Experiments

In this work we analyze the performance of algorithms for action recognition using deep learning in small datasets (ranging from a few thousand videos to hundreds of thousands). Each selected dataset differs from others by means of characteristics such as images recorded with a static/dynamic camera, egocentric/third-person view of the camera, *etc*.

### DogCentric dataset

The DogCentric Activity dataset ([DogCentric](http://robotics.ait.kyushu-u.ac.jp/~yumi/db/first_dog.html)) [[1](#references)] consists of first-person videos with outdoor scenes of wearable cameras mounted on dogs' back.

### UCF-11

UCF YouTube Action Dataset ([UCF-11](http://crcv.ucf.edu/data/UCF_YouTube_Action.php)) [[2](#references)] consists of videos that were manually collected from YouTube with a fixed resolution of 240x320 pixels. This dataset is very challenging due to large variations in camera motion, object appearance and pose, object scale, viewpoint, cluttered background, illumination conditions, *etc*.


---
## Results
In order to evaluate our approach, we calculate accuracy, precision, recall and F-measure that each model achieves.
Since classification accuracy takes into account only the proportion of correct results that a classifier achieves, it is not suitable for unbalanced datasets since it may be biased towards classes with a larger number of examples.
Although other factors may change results, classes with a larger number of examples tend to achieve better results since the network has more examples to learn the variability of the features.
By analyzing both datasets, we notice that they are indeed unbalanced, *i.e.*, classes are not equally distributed over frames.
Hence, we decided to calculate precision, recall, and F-measure to make a better evaluation of the unbalanced dataset.
We calculate scores considering all classes presented in the test set as explained in Section Datasets presented in our paper.
We keep the results separated by dataset as follows:

### DogCentric Dataset

To see the grid search results using the DogCentric dataset, click [here](grid_search_dog.md).


### UCF-11

To see the grid search results using the UCF-11 dataset, click [here](grid_search_ucf11.md).

---
## How to cite

When citing our work in academic papers, please use this BibTeX entry:

```
@inproceedings{aires2017temporalkdmile,
  title={Improving Activity Recognition using Temporal Regions},
  author={Aires, Joao Paulo and Monteiro, Juarez and Granada, Roger and Meneguzzi, Felipe and Barros, Rodrigo C},
  booktitle={Proceedings of the 5th Symposium on Knowledge Discovery, Mining and Learning (KDMILE)},
  year={2017},
  organization={SBC}
}
```

---
## References

[1] Iwashita, Yumi and Takamine, Asamichi and Kurazume, Ryo and Ryoo, Michael S. [First-Person Animal Activity Recognition from Egocentric Videos](http://dx.doi.org/10.1109/ICPR.2014.739). Proceedings of the 22nd International Conference on Pattern Recognition (ICPR'14), Stockholm, Sweden, pp. 4310-4315, IEEE, 2014.  
[2] Liu, Jingen and Luo, Jiebo and Shah, Mubarak. [Recognizing Realistic Actions from Videos "in the Wild"](https://doi.org/10.1109/CVPR.2009.5206744). Proceedings of the 2009 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR'09), Miami, FL, USA, pp. 1996-2003, IEEE, 2009.  
