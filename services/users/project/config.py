class BaseConfig:
    """Base configuration"""
    Testing = False


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing Configuration"""
    Testing = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""
    pass

