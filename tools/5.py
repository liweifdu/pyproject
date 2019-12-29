import tensorflow as tf
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", [None,10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
init = tf.initialize_all_variables()
x_axix=[]
train_acys=[]
test_acys=[]
saver=tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #saver = tf.train.import_meta_graph("model1\\model.ckpt.meta")
    #saver.restore(sess, tf.train.latest_checkpoint("model1"))
    for i in range(1000):
        x_axix.append(i)
        batch_xs, batch_ys = mnist.train.next_batch(100)
        train_accuracy = accuracy.eval(feed_dict={x: batch_xs, y_: batch_ys})
        test_accuracy = accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels})
        train_acys.append(train_accuracy)
        test_acys.append(test_accuracy)
        print("step %d, training accuracy %g" % (i, train_accuracy))
        print("step %d, test accuracy %g" % (i, train_accuracy))
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    print("test accuracy %g" %accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    saver.save(sess, "model1\\model.ckpt")

plt.title('Result Analysis')
plt.plot(x_axix, train_acys, color='green', label='training accuracy')
plt.plot(x_axix, test_acys, color='red', label='testing accuracy')
plt.legend()  # 显示图例

plt.xlabel('iteration times')
plt.ylabel('rate')
plt.show()