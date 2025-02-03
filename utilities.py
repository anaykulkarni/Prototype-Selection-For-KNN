import random

def random_sample(M, x_train, y_train):

    # Ensure the length of both lists is the same
    assert len(x_train) == len(y_train)

    # Generate random indices
    indices = random.sample(range(len(x_train)), M)

    # Sample the data and labels
    x_sample = [x_train[i] for i in indices]
    y_sample = [y_train[i] for i in indices]

    return x_sample, y_sample
