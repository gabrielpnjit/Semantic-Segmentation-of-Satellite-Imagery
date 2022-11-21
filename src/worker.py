import numpy
import time
import keras
import keras_metrics
import ConfigSpace as CS
import ConfigSpace.hyperparameters as CSH
import segmentation_models as sm
from hpbandster.core.worker import Worker
from simple_multi_unet_model import multi_unet_model, jacard_coef 

# def get_model():
#     return multi_unet_model(n_classes=6, IMG_HEIGHT=IMG_HEIGHT, IMG_WIDTH=IMG_WIDTH, IMG_CHANNELS=IMG_CHANNELS)

class KerasWorker(Worker):

    def __init__(self, X_train, X_test, y_train, y_test, img_height, img_width, img_channels, sleep_interval=0, **kwargs):
        super().__init__(**kwargs)

        self.batch_size = 1
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.IMG_HEIGHT = img_height
        self.IMG_WIDTH = img_width
        self.CHANNELS = img_channels

    def compute(self, config, budget, working_directory, *args, **kwargs):

        metrics=['accuracy', jacard_coef, keras.metrics.Precision(), keras.metrics.Recall()]
        model = multi_unet_model(n_classes=6, IMG_HEIGHT=self.IMG_HEIGHT, IMG_WIDTH=self.IMG_WIDTH, IMG_CHANNELS=self.CHANNELS)
        optimizer = keras.optimizers.Adam(lr=config['lr'])
        weights = [0.1666, 0.1666, 0.1666, 0.1666, 0.1666, 0.1666]
        dice_loss = sm.losses.DiceLoss(class_weights=weights) 
        focal_loss = sm.losses.CategoricalFocalLoss()
        total_loss = dice_loss + (1 * focal_loss)
        model.compile(optimizer=optimizer, loss=total_loss, metrics=metrics)
        # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=metrics)
        model.summary()

        history1 = model.fit(self.X_train, self.y_train, 
                    batch_size =self.batch_size,
                    verbose=1, 
                    epochs=int(budget), 
                    validation_data=(self.X_test, self.y_test), 
                    shuffle=False)

        train_score = model.evaluate(self.X_train, self.y_train, verbose=0)
        test_score = model.evaluate(self.x_test, self.y_test, verbose=0)
        val_score = test_score

        #import IPython; IPython.embed()
        return ({
                'loss': 1-val_score[1],
                'info': {       'test accuracy': test_score[1],
                                        'train accuracy': train_score[1],
                                        'number of parameters': model.count_params(),
                                }

        })
    
    @staticmethod
    def get_configspace():
        cs = CS.ConfigurationSpace()
        lr = CSH.UniformFloatHyperparameter('lr', lower=1e-6, upper=1e-1, default_value='1e-2', log=True)
        cs.add_hyperparameters([lr])

        return cs