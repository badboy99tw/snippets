# Systemd Service in Python

## Install

Install Python 3.7 and Virtualenv

```
apt update -y
apt install -y \
    python3.7 \
    python3-pip \
    python3-virtualenv
```

Setup Virtualenv

```
export WORKING_DIR=/path/to/code
export VIRTUAL_ENV=$WORKING_DIR/.venv
mkdir -p $VIRTUAL_ENV
python3 -m virtualenv --python=/usr/bin/python3.7 $VIRTUAL_ENV
```

Install dependencies

```
$VIRTUAL_ENV/bin/pip install -r $WORKING_DIR/requirements.txt
```

Install systemd service

```
cp $WORKING_DIR/my_service.service /etc/systemd/system/
```

## Run

```
systemctl start my_service
```

## References

* [Writing a systemd Service in Python](https://github.com/torfsen/python-systemd-tutorial)
