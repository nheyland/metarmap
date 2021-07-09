import requests as r


def data() -> object:
    json = {}
    raw = r.get(
        "https://www.aviationweather.gov/adds/dataserver_current/current/metars.cache.csv").text

    for i in raw.splitlines():
        key = i.split(",")
        if(len(key)) == 44:
            json[key[1]] = {
                "raw_text": key[0],
                "station_id": key[1],
                "observation_time": key[2],
                "latitude": key[3],
                "longitude": key[4],
                "temp_c": key[5],
                "dewpoint_c": key[6],
                "wind_dir_degrees": key[7],
                "wind_speed_kt": key[8],
                "wind_gust_kt": key[9],
                "visibility_statute_mi": key[10],
                "altim_in_hg": key[11],
                "sea_level_pressure_mb": key[12],
                "corrected": key[13],
                "auto": key[14],
                "auto_station": key[15],
                "maintenance_indicator_on": key[16],
                "no_signal": key[17],
                "lightning_sensor_off": key[18],
                "freezing_rain_sensor_off": key[19],
                "present_weather_sensor_off": key[20],
                "wx_string": key[21],
                "sky_cover": key[22],
                "cloud_base_ft_agl": key[23],
                "sky_cover": key[24],
                "cloud_base_ft_agl": key[25],
                "sky_cover": key[26],
                "cloud_base_ft_agl": key[27],
                "sky_cover": key[28],
                "cloud_base_ft_agl": key[29],
                "flight_category": key[30],
                "three_hr_pressure_tendency_mb": key[31],
                "maxT_c": key[32],
                "minT_c": key[33],
                "maxT24hr_c": key[34],
                "minT24hr_c": key[35],
                "precip_in": key[36],
                "pcp3hr_in": key[37],
                "pcp6hr_in": key[38],
                "pcp24hr_in": key[39],
                "snow_in": key[40],
                "vert_vis_ft": key[41],
                "metar_type": key[42],
                "elevation_m": key[43]
            }
    return json
