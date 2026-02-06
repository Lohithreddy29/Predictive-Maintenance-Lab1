def detect_alerts(df, residuals, MinC, MaxC, T):
    df = df.copy()
    df["residual"] = residuals

    df["alert"] = 0
    df["error"] = 0

    count = 0
    for i in range(len(df)):
        if df["residual"].iloc[i] >= MaxC:
            count += 1
            if count >= T:
                df.at[i, "error"] = 1
        elif df["residual"].iloc[i] >= MinC:
            count += 1
            if count >= T:
                df.at[i, "alert"] = 1
        else:
            count = 0

    return df