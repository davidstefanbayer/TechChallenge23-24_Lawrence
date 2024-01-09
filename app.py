from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

app = Flask(__name__)

class Lawyer:
    def __init__(self, name, budget, location, expertise):
        self.name = name
        self.budget = budget
        self.location = location
        self.expertise = expertise

    def __repr__(self):
        return f"Lawyer(Name: {self.name}, Hourly Fee: {self.budget}, Location: {self.location}, Expertise: {self.expertise})"

# Property Lawyers
lawyer_1 = Lawyer("Pfordte Bosbach Rechtsanwälte", 250, "Oskar-Schlemmer-Straße 3, 80807 München", "property")
lawyer_2 = Lawyer("DMS Rechtsanwälte Duchon, Meißner, Schütrumpf", 300, "Finkenstr. 5, 80333 München", "property")
lawyer_9 = Lawyer("Berger & Stein Rechtsanwälte", 275, "Leopoldstraße 244, 80807 München", "property")
lawyer_10 = Lawyer("Kanzlei Schwarz & Partner", 320, "Maximilianstraße 35, 80539 München", "property")

# Tax Lawyers
lawyer_3 = Lawyer("Rose & Partner", 200, "Fürstenfelder Straße 5, 80331 München", "tax")
lawyer_4 = Lawyer("McDermott Will & Emery Rechtsanwälte ", 350, "Nymphenburger Str. 3, 80335 München", "tax")
lawyer_11 = Lawyer("Bauer & Müller Steuerkanzlei", 210, "Sonnenstraße 19, 80331 München", "tax")
lawyer_12 = Lawyer("Kanzlei Weiss & Lang", 330, "Theresienstraße 1, 80333 München", "tax")

# Family Lawyers
lawyer_5 = Lawyer("Garlipp & Kollegen Rechtsanwälte", 150, "Nymphenburger Str. 185, 80634 München", "divorce")
lawyer_6 = Lawyer("Vera Templer & Parnter", 275, "Sebastiansplatz 8, 80331 München", "divorce")
lawyer_13 = Lawyer("Kanzlei Fischer & Sohn", 165, "Ludwigstraße 8, 80539 München", "divorce")
lawyer_14 = Lawyer("Müller & Wagner Familienrecht", 280, "Schellingstraße 109, 80798 München", "divorce")

# Environmental Lawyers
lawyer_7 = Lawyer("Graf von Wesphalen & Partner", 225, "Nymphenburger Straße 64, 80335 München", "environmental")
lawyer_8 = Lawyer("Environmental Lawyer Name 2", 300, "Elisenstraße 3, 80335 München", "environmental")
lawyer_15 = Lawyer("Kanzlei Grün & Partner", 240, "Lindwurmstraße 10, 80337 München", "environmental")
lawyer_16 = Lawyer("Baum & Wald Umweltrecht", 315, "Brienner Straße 55, 80333 München", "environmental")


class LawyerMatcher:
    def __init__(self, lawyers):
        self.lawyers = lawyers

    def get_coordinates(self, address):
        location = geolocator.geocode(address)
        return (location.latitude, location.longitude) if location else None

    def find_matching_lawyers(self, max_fee, user_location, expertise_needed):
        user_coordinates = self.get_coordinates(user_location)
        matching_lawyers = []

        for lawyer in self.lawyers:
            if lawyer.expertise == expertise_needed and lawyer.budget <= max_fee:
                lawyer_coordinates = self.get_coordinates(lawyer.location)
                if user_coordinates and lawyer_coordinates:
                    distance = geodesic(user_coordinates, lawyer_coordinates).km
                    distance = round(distance, 2)  #two decimal places
                    matching_lawyers.append((lawyer, distance))

        matching_lawyers.sort(key=lambda x: x[1])
        return matching_lawyers

# Initialize geolocator
geolocator = Nominatim(user_agent="TUMConsumerLawyerTC")

# List of all lawyers
all_lawyers = [lawyer_1, lawyer_2, lawyer_3, lawyer_4, lawyer_5, lawyer_6, lawyer_7, lawyer_8, lawyer_9, lawyer_10, lawyer_11, lawyer_12, lawyer_13, lawyer_14, lawyer_15, lawyer_16]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        max_fee = float(request.form['max_fee'])
        user_location = request.form['user_location']
        expertise_needed = request.form['expertise_needed']

        matcher = LawyerMatcher(all_lawyers)
        matching_lawyers = matcher.find_matching_lawyers(max_fee, user_location, expertise_needed)

        return render_template('results.html', matching_lawyers=matching_lawyers, user_location=user_location)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
