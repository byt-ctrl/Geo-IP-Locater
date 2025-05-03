
#  Geo-IP-Locator 

🔍  **Geo-IP-Locator** is a Python-based IP geolocation tracker that retrieves network information and visualizes location data on an interactive map.

## - Features -
- Fetches IP geolocation and network details using `ip-api.com`
- Displays formatted information including country, city, ISP, and coordinates
- Saves IP data in a CSV file for further analysis
- Generates an interactive map using `folium`
- Supports tracking both personal and external IP addresses

## - Requirements -
Ensure you have the following dependencies installed :
```bash
pip install pandas 
pip install datetime
pip install folium
pip install requests
pip install webbrowser
```
## Example
```bash
🔍 Welcome to the IP Geolocation Tracker

1️⃣  Track your own IP
2️⃣  Track another IP
Choose an option (1 or 2): 2
Enter the target IP address / hostname ex(google.com) :- 130.245.74.31

================ IP Address Information ================

 IP :-            130.245.74.31
 Country :-       United States (US)
 Region :-        New York
 City :-          Stony Brook
 ZIP Code :-      11790
 Coordinates :    40.9076, -73.122
 Timezone :       America/New_York
 Local Time:-     2025-05-03 21:27:35
 ISP :-           State University of New York at Stony Brook
 Organization :-  State University of New York at Stony Brook
 ASN :-           AS5719 State University of New York at Stony Brook
 Reverse DNS :-   N/A
 CSV saved :-     ip_results.csv
 Map generated :  ip_location_map.html

 Open map in your browser? (y/n) :  
```

---

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to contribute! Fork the repository, make your changes, and submit a pull request. All contributions are welcome.

