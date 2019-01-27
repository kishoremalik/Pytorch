## Autoencoders
So far, we have described the application of neural networks to supervised learning, in which we have labeled training examples.
Now suppose we have only a set of unlabeled training examples {x(1),x(2),x(3),…}, where x(i)∈Rn. 
An autoencoder neural network is an unsupervised learning algorithm that applies backpropagation, 
setting the target values to be equal to the inputs. I.e.,
it uses y(i)=x(i).
<p align="center">
    <img src="Image/autoencoder2.PNG" width="750"\>
</p>
