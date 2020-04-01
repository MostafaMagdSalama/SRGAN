

   
    
#----------------------------------------------------------
from utils import *
from skimage.metrics import peak_signal_noise_ratio, structural_similarity
from datasets import SRDataset
from PIL import Image
import matplotlib.pyplot as plt
from torch import argmax
from google.colab import files
from PIL import Image, ImageDraw, ImageFont
from google.colab import files
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def afro(url):
# Data

  test_data_names = ["Set5"]

# Model checkpoints
  srgan_checkpoint = "/content/drive/My Drive/srresnet/checkpoint_srgan.pth.tar"


# Load model,  the   the SRGAN


# model = srresnet
  srgan_generator = torch.load(srgan_checkpoint)['generator'].to(device)
  srgan_generator.eval()
  model = srgan_generator

# Evaluate
  for test_data_name in test_data_names:
  

    # Custom dataloader
     test_dataset = SRDataset(url= url,
                             split='test',
                             crop_size=0,
                             scaling_factor=4,
                             lr_img_type='imagenet-norm',
                             hr_img_type='[-1, 1]',
                             test_data_name=test_data_name)
     test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1, shuffle=False, num_workers=4,
                                              pin_memory=True)

    

    # Prohibit gradient computation explicitly because I had some problems with memory
     with torch.no_grad():
        # Batches
         for i, (lr_imgs, hr_imgs) in enumerate(test_loader):
            # Move to default device
            lr_imgs = lr_imgs.to(device)  # (batch_size (1), 3, w / 4, h / 4), imagenet-normed
            hr_imgs = hr_imgs.to(device)  # (batch_size (1), 3, w, h), in [-1, 1]
            # Forward prop.
            sr_imgs = model(lr_imgs)# (1, 3, w, h), in [-1, 1]
           
           
            sr_img_srgan = sr_imgs.squeeze(0).cpu().detach()
            sr_img_srgan = convert_image(sr_img_srgan, source='[-1, 1]', target='pil')
            plt.axis('off')
            plt.imshow(sr_img_srgan)
            plt.savefig('test.png')
            files.download('test.png')
            # Calculate PSNR and SSIM
            sr_imgs_y = convert_image(sr_imgs, source='[-1, 1]', target='y-channel').squeeze(
                0)  # (w, h), in y-channel
            hr_imgs_y = convert_image(hr_imgs, source='[-1, 1]', target='y-channel').squeeze(0)  # (w, h), in y-channel
            
    


  print("\n")
#------------------------------------------------------------------------

afro('/content/drive/My Drive/temp/1-100/0064.png')
    