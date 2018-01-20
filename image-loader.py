import matplotlib.pyplot as plt
import scipy
import numpy

bug = scipy.imread('stinkbug1.png')

# if you want to inspect the shape of the loaded image
# uncomment the following line
# print bug.shape

# the original image is RBG having values for all three
# channels separately. For simplicity, we convert that to greyscale image
# by picking up just one channel

# convert to gray
bug = bug[:,:,0]

plt.figure()
plt.gray()

plt.subplot(121)
plt.imshow(bug)

# show 'zoomed' region
zbug = bug[100:350, 140:350]

plt.subplot(122)
plt.imshow(zbug)

plt.show()
