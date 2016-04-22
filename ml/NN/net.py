class FullyConnectedNet(object):
    """ {affine - [batch norm] - relu - [dropout]} x (L - 1) - affine - softmax """

    def __init__(self, hidden_dims, input_dim=3*32*32, num_classes=10,
                 dropout=0, use_batchnorm=False, reg=0.0,
                 weight_scale=1e-2, dtype=np.float32, seed=None):

        self.use_batchnorm = use_batchnorm
        self.use_dropout = dropout > 0
        self.reg = reg
        self.num_layers = 1 + len(hidden_dims)
        self.dtype = dtype
        self.params = {}

        for i_layer, hidden_dim in enumerate(hidden_dims):
            if i_layer == 0:
                prev_dim = input_dim
            else:
                prev_dim = hidden_dims[i_layer-1]

            self.params["W"+str(i_layer+1)] = weight_scale * np.random.randn(prev_dim, hidden_dim)
            self.params["b"+str(i_layer+1)] = np.zeros(hidden_dim)

        self.params["W"+str(i_layer+2)] = weight_scale * np.random.randn(hidden_dims[-1], num_classes)
        self.params["b"+str(i_layer+2)] = np.zeros(num_classes)

        # drop out
        self.dropout_param = {}
        if self.use_dropout: self.dropout_param = {"mode": "train", "p": droupout}
        for k, v in self.params.iteritems():
            self.params[k] = v.astype(dtype)


    def loss(self, X, y=None):
        X = X.astype(self.dtype)
        mode = "test" if y is None else "train"

        # params
        if self.dropout_param is not None:
            self.dropout_param["mode"] = mode
        if self.use_batchnorm:
            for bn_param in self.bn_params:
                bn_param[mode] = mode

        
        h = []
        cache = []
        h.append(X)
        cache.append(None)

        for i_layer in np.arange(1, self.num_layers+1):

            if i_layer == self.num_layers:
                h_temp, cache_temp = affine_forward(h[i_layer+1], self.params["W"+str(i_layer+1)], self.params["b"+str(i_layer+1)])
                h.append(h_temp)
                cache.append(cache_temp)

            else:
                h_temp, cache_temp = affine_relu_forward(h[i_layer+1], self.params["W"+str(i_layer+1)], self.params["b"+str(i_layer+1)])
                h.append(h_temp)
                cache.append(cache_temp)

        scores = h[self.num_layers]

        if mode == "test": return scores

        grads = {}
        loss, dscores = softmax_loss(scores, y)

        for i_layer in np.arange(self.num_layers, 0, -1):
            W = self.params["W"+str(i_layer+1)]
            loss += 0.5 * self.reg * np.square(W).sum()

        dh = dscores.copy()

        for i_layer in np.arange(self.num_layers, 0, -1):

            if i_layer == self.num_layers:
                dh, dW, db = affine_backward(dh, cache[i_layer])
                grads["W"+str(i_layer+1)] = dW
                grads["b"+str(i_layer+1)] = dh

            else:
                dh, dW, db = affine_relu_backward(dh, cache[i_layer])
                grads["W"+str(i_layer+1)] = dW
                grads["b"+str(i_layer+1)] = dh

        for i_layer in np.arange(self.num_layers, 0, -1):
            W = self.params["W"+str(i_layer)]
            grads["W"+str(i_layer)] += self.reg * W

        return loss, grads


                
        
