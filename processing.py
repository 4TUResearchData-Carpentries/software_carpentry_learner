import numpy
import matplotlib.pyplot as plt


def visualize(filename):
    # Import data
    data = numpy.loadtxt(fname=filename, delimiter=",")

    # Setup figure
    fig = plt.figure(figsize=(10, 3))

    # Add subplots
    axes1 = fig.add_subplot(1, 3, 1) # (nrows, ncols, position)
    axes2 = fig.add_subplot(1, 3, 2) # (nrows, ncols, position)
    axes3 = fig.add_subplot(1, 3, 3) # (nrows, ncols, position)

    # Do statistics
    axes1.plot(numpy.mean(data, axis=0))
    axes2.plot(numpy.max(data, axis=0))
    axes3.plot(numpy.min(data, axis=0))

    # Add labels
    axes1.set_ylabel("mean")
    axes2.set_ylabel("max")
    axes3.set_ylabel("min")
       
    plt.show()
    
def detect_problems(filename):
    data = numpy.loadtxt(fname=filename, delimiter=",")
    
    max_inflammation = numpy.max(data, axis=0)
    min_inflammation = numpy.min(data, axis=0)
    
    if (max_inflammation[0] == 0) and (max_inflammation[20] == 20):
        print("Suspicious looking maxima")
    elif numpy.sum(min_inflammation) == 0:
        print("Minima add up to zero")
    else:
        print("Data looks OK!")