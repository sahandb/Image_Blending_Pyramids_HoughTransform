# Image_Blending with Pyramids from scratch | detect intersecting lines with Hough Transform from scratch
Image blending with pyramids and detect two intersecting lines by using Hough transform technique

# Image Blending by use the consept of Pyramids
At first create mask

then create gaussian pyramid for apple and orange and mask (down sample for pyramid 6 times)

And then create Laplacian pyramid for orange and mask (upsample I th gaussian and subtract from i-1 gaussian)

Then multiple mask with apple and 1-mask for orange and then sum both of them

And at last reconstruct the summation of multiple apple and multiple 1-mask in orange and then add unsampled of pyramid to reconstructed image

over horizental and vertical

![image](https://user-images.githubusercontent.com/24508376/219148035-b8ed32b5-5c6d-4d87-a42e-b9a16ab768bb.png)

____________________________

over diagonal axis

![image](https://user-images.githubusercontent.com/24508376/219148181-93ae75e6-76ac-4368-bde5-af0488cef9f6.png)

# detect two intersecting lines by using the consept of Hough transform technique from scratch
At first give edge image to function

Then get the result for Hough transform probabilistic and simple Hough

![image](https://user-images.githubusercontent.com/24508376/219148748-7cbc6bf0-29fb-4c67-8946-24e617febef8.png)

