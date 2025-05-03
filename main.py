import pandas as pd
from datetime import datetime
import requests
import folium
import webbrowser


def fetch_ip_data(target_ip=None) :

    """getting geolocation and network info from ip-api.com"""

    base_url="http://ip-api.com/json/"
    try :

        response=requests.get(base_url+(target_ip or ""))
        data=response.json()
        if data['status']!='success' :
            print(f" Error : {data.get('message','Unknown error')}")
            return None
        return data
    except Exception as error :
        print(f" Request failed : {error}")
        return None

def show_ip_info(ip_data) :


     #displays formatted IP geolocation information

    print("\n================ IP Address Information ================")
    print()
    print(f" IP :-            {ip_data.get('query')}")
    print(f" Country :-       {ip_data.get('country')} ({ip_data.get('countryCode')})")
    print(f" Region :-        {ip_data.get('regionName')}")
    print(f" City :-          {ip_data.get('city')}")
    print(f" ZIP Code :-      {ip_data.get('zip')}")
    print(f" Coordinates :    {ip_data.get('lat')}, {ip_data.get('lon')}")
    print(f" Timezone :       {ip_data.get('timezone')}")


    try :
        current_time=datetime.now().astimezone().astimezone().strftime('%Y-%m-%d %H:%M:%S')
        print(f" Local Time:-     {current_time}")
    except Exception:
        pass

    print(f" ISP :-           {ip_data.get('isp')}")
    print(f" Organization :-  {ip_data.get('org')}")
    print(f" ASN :-           {ip_data.get('as')}")
    print(f" Reverse DNS :-   {ip_data.get('reverse', 'N/A')}")


def save_data_csv(ip_data, filename="ip_results.csv") :

    """export IP data to CSV file"""
    df=pd.DataFrame([ip_data])
    df.to_csv(filename,index=False)
    print(f" CSV saved :-     {filename}")

def generate_map(ip_data,output_file="ip_location_map.html") : 

    """create interactive map using folium and save as HTML"""
    latitude=ip_data.get("lat")
    longitude=ip_data.get("lon")

    if latitude and longitude :

        ip_map=folium.Map(location=[latitude,longitude],zoom_start=10)
        popup_info=f"{ip_data.get('query')}-{ip_data.get('city')} , {ip_data.get('country')}"
        folium.Marker(
            [latitude,longitude],
            popup=popup_info,
            tooltip="IP Location",
            icon=folium.Icon(color="red")
        ).add_to(ip_map)

        ip_map.save(output_file)
        print(f" Map generated :  {output_file}")
        
        print()
        open_map = input(" Open map in your browser? (y/n) : ").strip().lower()
        if open_map == "y":
            webbrowser.open(output_file)
    else:
        print(" Coordinates missing. Cannot generate map.")

def ip_geolocation_tracker() :
    """Main control flow of the IP geolocation tracker"""
    print("========= Welcome to the IP Geolocation Tracker ========= \n")
    print("1️ Track your own IP (Enter 1)")
    print("2️ Track another IP  (Enter 2)")

    while True:
        user_choice=input("Choose an option (1 or 2): ").strip()
        if user_choice=="1":
            target_ip=None
            break
        elif user_choice=="2":
            target_ip=input("Enter the target IP address / hostname ex(google.com) :- ").strip()
            break
        else:
            print(" Invalid selection. Please type 1 or 2.")

    ip_info = fetch_ip_data(target_ip)

    if ip_info :
        show_ip_info(ip_info)
        save_data_csv(ip_info)
        generate_map(ip_info)
    else:
        print(" Could not retrieve valid IP data.")



ip_geolocation_tracker()

# END
        
