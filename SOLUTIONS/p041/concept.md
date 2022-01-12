# calculate_itinerary(flights, start) -> route | null

`calculate_itinerary(flights [(origin :airport, destination :airport)], start :airport) -> [airport] | null`

A algorithm to find an itinerary of flights tuple `(origin :airport, destination :airport)`. Starting by `start`, return a route, which is a connected path by using all flights. The retrun value is a "time" ordered list of the airports. If not such itinerary exists return `null`. If more than one exist return the lexicographical first one.

## Good to know and somehow not noticed by the first read

You can take a flight just once. So there is a limit, because yo cannot get lost into a loop. (To recognise this, it took me so much time..., I thought more of an classic Travelling Salesperson Problem variant)

## dictionary

- **Lexicographic order**: Phone book order, alphapetical `a<b<c...`, length does not matter.`"Abraham" < "Adam"`.
- **itinerary**: the route of a journey.

## algorithm ideas

First we sort the flight lexicographically, than the first founded route is the wanted.

```pseudo
calculate_itinerary(flights: [(origin :airport, destination :airport)], start :airport):
  if flights are empty:
    return [start]
  for each flight in flights:
     if flight.origin == start:
        route = calculate_itinerary(flights without flight, flight.destination):
        if route is not null:
          return [start] + route
  return null 
```

[code](solution.py)

## hence

python 3.9: typing imports for generic types no more needed.
