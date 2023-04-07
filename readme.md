# Simple async Python SMTP relay

Simple relay, accepts SMTP on specified ip/port, forwards to destination.

No authentication supported.

# Configuration
### Specify your local binding IP and port

```python
if __name__ == '__main__':
    port = 8080
    controller = aiosmtpd.controller.Controller(RelayHandler(), hostname='127.0.0.1', port=port)
```


### Specify destination SMTP server in TOML file
```python
[smtp]
server = "smtp"
port = 587
username = "someone@example.com"
password = "supersecret"
```