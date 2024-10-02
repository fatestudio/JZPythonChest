# trainer callback example
class Callback:

    def on_train_begin(self, logs=None):
        pass

    def on_train_end(self, logs=None):
        pass

    def on_epoch_begin(self, epoch, logs=None):
        pass

    def on_train_step_end(self, step, logs=None):
        pass

    def on_train_epoch_end(self, epoch, logs=None):
        pass


class PrintStepCallback(Callback):

    def on_train_step_end(self, step, logs=None):
        print(f"Step {step} completed.")


class PrintEpochCallback(Callback):

    def on_train_epoch_end(self, epoch, logs=None):
        print(f"Epoch {epoch} completed.")


class PrintTrainBeginCallback(Callback):

    def on_train_begin(self, logs=None):
        print("Training started.")


class PrintTrainEndCallback(Callback):

    def on_train_end(self, logs=None):
        print("Training finished.")


class Trainer:

    def __init__(self, model, callbacks=None):
        self.model = model
        self.callbacks = callbacks or []

    def train(self, epochs, steps_per_epoch):
        logs = {}

        # Call on_train_begin callbacks
        for callback in self.callbacks:
            callback.on_train_begin(logs)

        for epoch in range(epochs):
            # Call on_epoch_begin callbacks
            for callback in self.callbacks:
                callback.on_epoch_begin(epoch, logs)

            for step in range(steps_per_epoch):
                # Simulate a training step
                self.model.train_step()

                # Call on_train_step_end callbacks
                for callback in self.callbacks:
                    callback.on_train_step_end(step, logs)

            # Call on_train_epoch_end callbacks
            for callback in self.callbacks:
                callback.on_train_epoch_end(epoch, logs)

        # Call on_train_end callbacks
        for callback in self.callbacks:
            callback.on_train_end(logs)


# Example model class
class Model:

    def train_step(self):
        pass  # Implement your training step logic here


if __name__ == '__main__':
    # Usage
    model = Model()
    callbacks = [
        PrintTrainBeginCallback(),
        PrintStepCallback(),
        PrintEpochCallback(),
        PrintTrainEndCallback()
    ]
    trainer = Trainer(model, callbacks)
    trainer.train(epochs=5, steps_per_epoch=10)
