from django.shortcuts import render
import folium
from django.views.generic import TemplateView


class FoliumView(TemplateView):
    template_name = "trip/default.html"

    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        m = folium.Map(
            location=[53.890567, 27.550834],
            zoom_start=12,
            tiles='Stamen Terrain'
        )
        m.add_to(figure)

        folium.Marker(
            location=[53.890567, 27.550834],
            popup='Mt. Hood Meadows',
            icon=folium.Icon(icon='cloud')
        ).add_to(m)

        folium.Marker(
            location=[53.964098, 27.341206],
            popup='Timberline Lodge',
            icon=folium.Icon(color='green')
        ).add_to(m)

        folium.Marker(
            location=[53.941065, 27.346893],
            popup='Some Other Location',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        figure.render()
        return {"map": figure}

a = FoliumView()
print (a.get_context_data())



def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token }, 
                  )
    
