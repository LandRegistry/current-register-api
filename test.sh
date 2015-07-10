export SETTINGS="config.DevelopmentConfig"

py.test --junitxml=TEST-current-register-api.xml --cov-report term-missing --cov application tests
