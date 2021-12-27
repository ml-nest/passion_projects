from imports import *

if __name__ == "__main__":

    # Read training data
    df = pd.read_csv(config.INPUT_FILE)

    # map positive to 1 and negative to 0
    df[config.TARGET_COL] = df[config.TARGET_COL].apply(
    lambda x: 1 if x == config.POSITIVE_BINARY_CLASS else 0
    )

    # we create a new column called kfold and fill it with -1
    df["kfold"] = -1

    # fetch labels
    y = df[config.TARGET_COL].values

    # initiate the kfold class from model_selection module
    kf = model_selection.StratifiedKFold(n_splits=config.SPLITS, shuffle= config.SHUFFLE)
    # fill the new kfold column
    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)):
        df.loc[v_, 'kfold'] = f

    # save the new csv with kfold column
    df.to_csv(config.TRAINING_FILE, index=False)