## Architecture

```text
                    INTERNET
                        |
                        v
                Load Balancer
                        |
                        v
                   Kubernetes
                        |
             +----------+----------+
             |                     |
             v                     v
          BLUE                  GREEN
           v1                    v2
             |                     |
             +----------+----------+
                        |
                        v
                   User Traffic
```