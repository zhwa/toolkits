import numpy as np

class TwoLayerNet(object):
    """
    X: N * D
    W1: D * H
    W2: H * C
    b1: H
    b2: C
    """
    def __init__(self, input_size, hidden_size, output_size, std=1e-4):
        self.params = {}
        self.params["W1"] = std * np.random.randn(input_size, hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = std * np.random.randn(hidden_size, output_size)
        self.params["b2"] = np.zeros(output_size)


    def scores(self, X):
        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]
        hidden = np.maximum(0, X.dot(W1)+b1)
        scores = hidden.dot(W2)+b2
        return scores


    def loss(self, X, y=None, reg=0.0):

        # forward path
        scores = self.scores(X)

        if y == None: return scores

        # loss func
        logits = np.exp(scores)
        probs = logits / logits.sum(axis=1).reshape((-1,1))
        loss = -(1.0 / N) * np.log(probs[range(N), y]).sum() + 0.5 * reg * W1.square().sum() + 0.5 * reg * W2.square().sum()
        probs[range(n), y] -= 1

        # backward path
        grads = {}
        grads["W2"] = (1.0 / N) * hidden.T.dot(probs) + reg * W2
        grads["b2"] = np.mean(probs, axis=0)

        layer_1 = np.zeros_like(hidden)
        layer_1[hidden > 0] = 1
        layer_1 = layer_1 * grad["W2"]

        grads["W1"] = X.T.dot(layer_1)
        grads["b1"] = np.sum(layer_1, axis=0)

        return loss, grads


    def train(self, X, y, X_val, y_val, learning_rate=1e-3,
              learning_rate_decay=0.95, reg=1e-5,
              num_iter=100, batch_size=200, verbose=False):
        """ SGD"""
        num_train = X.shape[0]
        iterations_per_epoch = max(num_train / batch_size)

        loss_history = []
        train_acc_history = []
        val_acc_history = []

        # Use SGD to optimize the parameters
        for it in xrange(num_iters):

            # random mini-batch
            sample_index = np.random.randint(0, num_train, batch_size)
            X_batch = X[sample_index, :]
            y_batch = y[sample_index]
            loss, grads = self.loss(X_batch, y_batch, reg=reg)
            loss_history.append(loss)
            
            # update parameters
            self.params["W1"] -= learning_rate * grads["W1"]
            self.params["b1"] -= learning_rate * grads["b1"]
            self.params["W2"] -= learning_rate * grads["W2"]
            self.params["b2"] -= learning_rate * grads["b2"]

            if verbose and it % 100 == 0:
                print "iteration %d / %d: loss %f" % (it, num_iters, loss)

            if it % iterations_per_epoch == 0:
                train_acc = (self.perdict(X_batch) == y_batch).mean()
                val_acc = (self.predict(X_val) == y_val).mean()
                train_acc_history.append(train_acc)
                val_acc_history.append(val_acc)

                learning_rate *= learning_rate_decay

        return {
            "loss_history": loss_histroy
            "train_acc_history": train_acc_history
            "val_acc_history": val_acc_histroy
            }


    def predict(self, X):
        logits = self.probs(X)
        probs = logits / logits.sum(axis=1).reshape((-1,1))
        return np.argmax(probs, axis=1)
