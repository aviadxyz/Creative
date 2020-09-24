import numpy as np
import matplotlib.pyplot as plt

from fractions import gcd
import random


# r = np.arange(0, 2, 0.01)
# theta = 2 * np.pi * r
#
# ax = plt.subplot(111, projection='polar')
# ax.plot(theta, r)
# ax.set_rmax(2)
# ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
# ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
# ax.grid(True)
#
# ax.set_title("A line plot on a polar axis", va='bottom')
# plt.show()

#
# k = np.pi/2
#
# r = 1
# theta = np.arange(0, 2*np.pi*8, 0.01)
# ax = plt.subplot(111)
# ax.set_aspect(1)
# for i in range(2, 9, 1):
# 	f = i*1.0/10
# 	# f = 0.5
# 	x = r*(k-1)*np.cos(theta) + f*r*(np.cos(theta*(k-1)))
# 	y = r*(k-1)*np.sin(theta) - f*r*(np.sin(theta*(k-1)))
# 	ax.plot(x, y)
# plt.show()


def create_circle():
	circle = plt.Circle((0, 0), radius=5)
	return circle


def create_ladybug(x, y, r):
	patches = []

	patches.append(plt.Circle((x, y), radius=r, color=random_color()))
	patches.append(plt.Circle((x+r/3.0, y+r/1.7), radius=r/4.0, color='white'))
	patches.append(plt.Circle((x-r/3.0, y+r/1.7), radius=r/4.0, color='white'))

	# random.randint(0, 1)
	patches.append(plt.Circle((x+r/2.1, y-r/2.0), radius=r/4.0, color='black'))
	patches.append(plt.Circle((x, y-r/5.0), radius=r/6.0, color='black'))
	patches.append(plt.Circle((x-r/2.1, y-r/2.0), radius=r/4.0, color='black'))

	return patches


def create_ladybug_rec(x, y, r):
	print str(r)
	patches = []
	if r < 1:
		return create_ladybug(x, y, r)

	patches.append(plt.Circle((x, y), radius=r, color='darkred'))
	patches.append(plt.Circle((x+r/3.0, y+r/1.7), radius=r/4.0, color='white'))
	patches.append(plt.Circle((x-r/3.0, y+r/1.7), radius=r/4.0, color='white'))
	patches += create_ladybug_rec(x+r/3.0, y+r/1.7, r/4.0)
	patches += create_ladybug_rec(x-r/3.0, y+r/1.7, r/4.0)

	# random.randint(0, 1)
	patches.append(plt.Circle((x+r/2.1, y-r/2.0), radius=r/4.0, color='black'))
	patches.append(plt.Circle((x, y-r/5.0), radius=r/6.0, color='black'))
	patches.append(plt.Circle((x-r/2.1, y-r/2.0), radius=r/4.0, color='black'))

	return patches


def create_ladybug_rec2(x, y, r, N, R):
	patches = []
	if r < 1:
		return create_ladybug_circle(x, y, r, N, R)

	patches += create_ladybug_circle(x, y, r, N, R)

	patches += create_ladybug_rec2(x+R/3.0, y+R/2.5, r/4.0, N, r)
	patches += create_ladybug_rec2(x-R/3.0, y+R/2.5, r/4.0, N, r)
	#
	# # random.randint(0, 1)
	# patches += create_ladybug_rec2(x+R/2.1, y-R/3.0, R/7.0, N, r)
	# patches += create_ladybug_rec2(x-R/2.1, y-R/3.0, R/7.0, N, r)
	# patches += create_ladybug_rec2(x      , y-R/5.0, R/9.0, N, r)

	patches.append(plt.Circle((x+R/2.1, y-R/3.0), radius=R/7.0, color='black'))
	patches.append(plt.Circle((x      , y-R/5.0), radius=R/9.0, color='black'))
	patches.append(plt.Circle((x-R/2.1, y-R/3.0), radius=R/7.0, color='black'))

	return patches


def create_ladybug_circle(X, Y, r, N, R):
	patches = []
	for n in range(N):
		phi = n*2*np.pi/N
		x = R*np.sin(phi) + X
		y = R*np.cos(phi) + Y
		patches = patches + create_ladybug(x, y, r)

	return patches


def show_shape(patch):
	ax = plt.gca()
	ax.add_patch(patch)
	plt.axis('scaled')
	plt.show()


def random_color():
	# rgbl = [1, 0, 0]
	# random.shuffle(rgbl)
	# random.randint(0, 10)/10
	return random.randint(0, 10)/10.0, random.randint(0, 10)/10.0, random.randint(0, 10)/10.0


if __name__ == '__main__':
	patches = []
	N = 20
	r = 25
	R = 100

	# patches += create_ladybug_rec2(0, 0, r, N, R)
	for n in range(1000):
		patches += create_ladybug(random.randint(0, 200), random.randint(0, 100), random.randint(0, 5) + 5)

	ax = plt.gca()
	for p in patches:
		ax.add_patch(p)
	plt.axis('scaled')
	plt.show()
