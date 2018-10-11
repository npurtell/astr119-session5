import numpy as np

x = 1.0		#define a float
y = 2.0		#define another float

#numpy can do exponents and logarithms 
print(np.exp(x))		#e^x
print(np.log(x))		#ln x
print(np.log10(x))		#log_10 x
print(np.log2(x))		#log_2 x

#min/max/misc
print(np.fabs(x))		#absolute value as a float
print(np.fmin(x,y))		#min of x and y
print(np.fmax(x,y))		#max of x and y

#populate arrays
n = 100							#define an integer
z = np.arange(n,dtype=float)	#gives an array of floats [0.0,1,n-1]
z *= 2.0*np.pi /float(n-1)		#z = [0, 2*pi] gives an array of #s from 0 to2pi
sin_z = np.sin(z)				#z is an array ,will get an array sin at every z element

#interpolation
print(np.interp(0.75,z,sin_z))		#interpolate sin(0.75)
print(np.sin(0.75))

#declared z at discrete values between o and 2pi, pass through sinz, still get an array
#of values of 0 to 2pi but in sinz
#it will give you an estimate of the value of the function at any value we desire
#as long as it is in the range
#so we want the value of z=0.75 in the sin_z value array, and comparing it to 
#the actual value of sin0.75
#interpolation will take the values of z at each value in the array and graph it
#to basically make a function