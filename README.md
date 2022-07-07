# Bosch eBike Connect data fetch

I recently received my eBike, which is powered by a Bosch Performance CX motor and a Kiox display. Bosch pushes the data through an app on your phone to a portal, named "Bosch eBike Connect". I was curious to see if I was able to fetch the data that's available.

## Usage
1. Clone this repository
2. Rename the `config_example.json` file to `config.json`
3. Update the configuration (username and password)
4. Import `bec`

### Example
An example `statistics.py` file that prints the statistics.

```python
import bec

BoschEbikeConnect = bec.BoschEbikeConnect()
print(BoschEbikeConnect.get_statistics())
```

## Statistics
At the moment I can only fetch the statistics. These include the current month, previous month and all time statistics presented as JSON.

```json
{
    "current_month": {
        "month": 7,
        "distance": 0,
        "average_speed": 0.0,
        "calories_burned": 0,
        "elevation_gain": 0
    },
    "last_month": {
        "month": 6,
        "distance": 0,
        "average_speed": 0.0,
        "calories_burned": 0,
        "elevation_gain": 0
    },
    "total_statistics": {
        "distance": 0,
        "elevation_gain": 0
    }
}
```

## Activities
TODO.

## Future
I have no plans, yet. I was just curious to see if I was able to access the data. Perhaps I can fetch activities and add weather data to it, to calculate how often I encountered rainfall during my commutes.