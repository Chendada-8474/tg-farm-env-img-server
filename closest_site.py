from pykml import parser
import geopy.distance


def closest_site(x, y, route):

    sites = []
    closest_site = None
    closest_dis = 99999999999

    for i in route.Placemark:
        sites.append(i.ExtendedData.SchemaData.SimpleData.text)
        coors = i.LineString.coordinates.text.split(" ")
        x_sum = 0
        y_sum = 0
        for j in coors:
            point = list(map(float,j.split(',')))
            x_sum = x_sum + point[0]
            y_sum = y_sum + point[1]
        x_cen = x_sum / len(coors)
        y_cen = y_sum / len(coors)
        dis = geopy.distance.distance((y_cen, x_cen), (y,x)).km
        if dis < closest_dis:
            closest_dis = dis
            closest_site = i.ExtendedData.SchemaData.SimpleData.text

    return closest_site, sites

if __name__ == '__main__':
    x = 120.612212
    y = 24.065179
    print(closest_site(x,y))
