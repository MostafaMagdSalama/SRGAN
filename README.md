# SRGAN


### (SRGAN) with pytorch

we build a model that can realistically increase image resolution.
🚀 using `PyTorch 1.4` in `Python 3.6`.

---

**30 Mar 2020**: Code is now available , you can run the code in  [google colab](https://github.com/mstgdy/SRGAN/blob/master/Aphrodite.ipynb).

---
Super-resolution (SR) models essentially hallucinate new pixels where previously there were none. In this tutorial, we will try to _quadruple_ the dimensions of an image i.e. increase the number of pixels by 16x!

We implemente [_Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network_](https://arxiv.org/abs/1609.04802). It's not just that the results are very impressive... it's also a great introduction to GANs!

---

## SRGAN Architecture

<div align="center">
	<img src="https://github.com/tensorlayer/srgan/raw/master/img/model.jpeg" width="80%" height="10%"/>
</div>

### Our Results
the first training was *100 epoch*

---
## The Training
### Our Checkpoints are available [SRGAN (TAR)](https://drive.google.com/open?id=1ePooVQcEbIjEZfE2ED1dmtCVj-xUbg1c).
you can download it . we train about 3000 epoch from  [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/) dataset . if you want to train another dataset, this [link](https://drive.google.com/open?id=1qEEX29LyVP2NjNxYw2WR-KcehjdSCjEM)for our project you can run file : train-srgan.py

we upload the dataset to google drive , to train it in google colab , this article helped us for  [Downloading Datasets into Google Drive via Google Colab](https://towardsdatascience.com/downloading-datasets-into-google-drive-via-google-colab-bcb1b30b0166).

--- 

## Run
you can run the code using [google colab](https://github.com/mstgdy/SRGAN/blob/master/Aphrodite.ipynb).:
in the third cell -
just change the ``` url ``` in ```afro(url)``` 

---

### Reference
* [1] [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802)
* [2] [SRGAN: Training Dataset Matters](https://arxiv.org/abs/1903.09922)
