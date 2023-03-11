import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Remainder",
        message=" It's time to start brushing up ur mind with learned concepts by practicing",

        # displaying time
        timeout=5
    )
    # waiting time
    time.sleep(7)