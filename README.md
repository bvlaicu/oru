Oru calls the API of the Orange and Rockland Utility smart energy meter to return the current energy usage.

It requires the meter id.

Example usage:

```
meter = Meter("701139904")
energy_usage_wh = meter.last_read()
```

