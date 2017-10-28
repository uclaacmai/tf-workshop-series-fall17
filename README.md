# Tensorflow Workshop Series

Code, Slides, &amp; Materials for our Tensorflow Workshop Series, Fall Quarter 2017

### Getting a Python and Machine Learning Environment Up and Running

Please complete these tasks before the workshop in order to hit the ground running! Don’t worry if you run into some errors though, we will have mentors on hand to help you through setup. We'll also be hosting office hours for installation help on Tuesday, 10/10 from 5-7pm in Sproul Lecture Room.

#### Mac & Linux Installation Instructions

If you don't have `brew`, install it by using the command available [here](https://brew.sh/). 

(Optional: We recommend a `python3` installation. Your mac currently likely comes with Python 2 as the default built-in.) 

If you don't have `python3` installed (check by typing `python3` in the terminal), run `brew install python3`. This will install `python3` and a package manager, `pip3` for you. This may take a while.
 
Run ```pip3 install numpy matplotlib tensorflow sklearn jupyter scipy``` if you are running Python3, otherwise run ```pip install numpy matplotlib tensorflow jupyter sklearn scipy```. This command may have to be prefaced with the `sudo` keyword. 

If you have installed any of these packages before, make sure to run `pip install [PACKAGE] --upgrade` to ensure that you have the latest version. 

Execute the following Python program:

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import sklearn
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
```

If it runs without any errors, then you're good to go!

#### Windows Installation Instructions

#### Highly recommended: Installing with the Anaconda Distribution

- Anaconda is a package managing tool for Python that can be installed for both Mac and Windows. We've found that going with Anaconda results in the least installation issues for those of you who are using Windows. 

First, download Anaconda at this link: https://www.anaconda.com/download/#windows. We recommend downloading the Python 3.6 installation. 

After Anaconda has downloaded, open it up and install it. The installation process takes a while, but after you should see a screen with the option "Register Anaconda as my default Python". Check this, and continue. 

Once the installation is finished, you should be able to open up the Anaconda prompt, and invoke `python`. In the `python` interpreter, the commands `import sklearn` `import matplotlib` `import numpy` should all work. 

Finally, install Tensorflow with the Anaconda package manager, known as `conda`: `conda install Tensorflow`. Now, you should be able to execute the following program without any issues: 

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
```

For additional details on Anaconda installation, see [this](https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444) helpful link.

#### Installing on Windows without Anaconda

If you don't want to use Anaconda, follow these steps to get your environment and tools up and running.

Source to refer: https://www.tensorflow.org/install/install_windows

Install Python 3.5 if it's not currently installed on your computer: https://www.python.org/downloads/release/python-352/

TensorFlow only supports version 3.5.x of Python on Windows. Note that Python 3.5.x comes with the pip3 package manager, which is the program you'll use to install TensorFlow. Note that this means you cannot use Python 2 if you have it installed. 

To install tensorflow, issue the following command: ```C:\> pip3 install --upgrade tensorflow```

Also issue the following commands for `jupyter`, `sklearn`, and `matplotlib`. 

```C:\> pip3 install --upgrade jupyter```

```C:\> pip3 install --upgrade matplotlib ```

```C:\> pip3 install --upgrade sklearn```

Next, invoke Python through the terminal:

```C:> python ```

In the terminal, execute the following python program: 

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
```

If it runs without errors, you're good to go!
