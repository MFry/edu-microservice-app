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