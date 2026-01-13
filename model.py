from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    """
    Train a simple RandomForest model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model


def dummy_model():
    from sklearn.dummy import DummyClassifier
    model = DummyClassifier(strategy="most_frequent")
    return model
