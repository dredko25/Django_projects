from django.shortcuts import render

def main(request):
    # Render the main page.
    return render(request, 'bus_station/main.html')

def routes(request):
    # Render the routes page.
    return render(request, 'bus_station/routes.html', {'routes': routes_data})

def prices(request):
    # Render the prices page.
    return render(request, 'bus_station/prices.html', {'prices': prices_data})

def contacts(request):
    # Render the contacts page.
    return render(request, 'bus_station/contacts.html')

# Create routes list.
routes_data = [
  {
    "departure_station": "Київ",
    "destination": "Львів",
    "departure_frequency": "щоденно",
    "carrier": "Мерседес-18",
    "departure_time": "08:00",
    "arrival_time": "15:30"
  },
  {
    "departure_station": "Харків",
    "destination": "Одеса",
    "departure_frequency": "щоденно",
    "carrier": "Мерседес 50",
    "departure_time": "8:30",
    "arrival_time": "21:00"
  },
  {
    "departure_station": "Київ",
    "destination": "Херсон",
    "departure_frequency": "щоденно",
    "carrier": "Автолюкс",
    "departure_time": "12:00",
    "arrival_time": "18:30"
  },
  {
    "departure_station": "Київ",
    "destination": "Полтава",
    "departure_frequency": "щоденно",
    "carrier": "Мерседес-18",
    "departure_time": "09:30",
    "arrival_time": "12:00"
  },
  {
    "departure_station": "Одеса",
    "destination": "Харків",
    "departure_frequency": "щоденно",
    "carrier": "Автолюкс",
    "departure_time": "9:00",
    "arrival_time": "21:30"
  }
]

# Create prices list.
prices_data = [
  {
    "departure_station": "Київ",
    "destination": "Львів",
    "departure_time": "08:00",
    "arrival_time": "15:30",
    "price": "500грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Одеса",
    "departure_time": "15:30",
    "arrival_time": "21:00",
    "price": "400грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Херсон",
    "departure_time": "12:00",
    "arrival_time": "18:30",
    "price": "500грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Полтава",
    "departure_time": "09:30",
    "arrival_time": "12:00",
    "price": "300грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Харків",
    "departure_time": "9:00",
    "arrival_time": "21:30",
    "price": "200грн"
  }
]