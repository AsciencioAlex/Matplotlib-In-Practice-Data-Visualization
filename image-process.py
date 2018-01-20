import scipy.misc
import matplotlib.pyplot as plt

# load already prepared ndarray from scipy
ascent = scipy.misc.ascent()

# set the default colormap to gray
plt.gray()

plt.imshow(ascent)
plt.colorbar()
plt.show()

print ascent.shape
print ascent.max()
print ascent.dtype
