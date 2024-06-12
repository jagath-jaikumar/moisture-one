import sentry_sdk


def init(settings):
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        traces_sample_rate=1.0,
        profiles_sample_rate=0.2,
    )
