### Python Setup

```
 curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

  export PATH="~/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  pyenv install 3.6.4
```

`cd` into the `vagrant/` directory and setup virtual env.

```
 pip install virtualenv
 python -m virtualenv env --always-copy
 source env/bin/activate
```

To run the CLI where `__init__.py` is the flask app and `manage.py` is the CLI wrapper.

```
  FLASK_APP=project/__init__.py
  python manage.py run --host='0.0.0.0'
```

To set CLI in debug mode

```
  export FLASK_DEBUG=1
```

## Docker

To set docker `env` variables, after running

```
docker-machine env dev-machine -shell cmd
```

run the last `REM` line without the `REM`
