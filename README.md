Lawrence (Consumer Lawyer Group 3) - Tech Challenge (UnternehmerTUM) [WI001188]

Lawrence is a comprehensive tool developed for the Tech Challenge (UnternehmerTUM) [WI001188], aimed at simplifying the process of finding legal assistance.
The project, due on January 23rd, 2024, is a collaborative effort by a skilled team consisting of Sarah Störzel, Mohammad Sahbi, Hafez Pirzadeh,
David Bayer, and Jonas Walcher.

We extend our heartfelt gratitude to Laura Herzer for her invaluable advice and support throughout the development process.

The uniqueness of our project approach lies in its dual-development approach. We created a Figma Prototype, which was showcased during the Finals,
to visually and interactively design the user experience. Alongside this, we developed a functional prototype using Python, CSS, HTML, and Flask.
This dual approach allowed us to meticulously test and refine the user interface and experience in Figma, while simultaneously ensuring robust back-end functionality
with our coded prototype. This strategy guarantees a comprehensive, efficient, and user-friendly tool that effectively connects individuals with legal professionals.

Features

User-Friendly Interface: Designed for seamless user experience, ensuring ease of navigation and interaction.
Advanced Search Filters: Enables users to find lawyers based on specific criteria like expertise, location, and budget.
Responsive Design: Ensures the application is accessible across various devices, maintaining functionality and aesthetics.
Efficient Data Processing: The backend, powered by Flask, efficiently handles data processing, offering quick and accurate lawyer matching.


Technical Implementation

The application's front-end was developed using HTML and CSS, with a focus on responsive design principles.
The back-end functionality is handled by Python with Flask, ensuring efficient data processing and user request handling.


Limitations

The current prototype of Lawrence, while functional and illustrative of our initial vision, does have certain limitations:

No Large Language Model (LLM) Integration: Unlike some advanced applications, our prototype does not yet use a large language model for natural
language processing or complex query handling as showcased in Figma. This means the interaction is more straightforward and does not support conversational AI features.
Furthermore this implies that we - for demonstration purposes - have to stick with the case of the neighbouring fence as the case at hand.

Geolocation Dependency: The prototype relies heavily on the geopy library and Nominatim geolocator for location-based services.
This dependency means that the accuracy and effectiveness of the lawyer matching are contingent on the reliability and precision of these third-party services.

Limited Lawyer Data Structure: Since we are in the very early stages of the development of Lawrence, we're merely working with 16 lawfirms we have stored simply within out script.

Front-End Constraints: The user interface, designed using HTML and CSS, is straightforward and user-friendly, but it lacks advanced interactive elements and
dynamic content that could enhance user experience - however, this is where our dual-approach comes in & leverage our Figma Prototype.

Scalability and Performance: Running on Flask's built-in server, the prototype is not optimized for high traffic or scalability. In a real-world scenario,
the application would require a more robust server setup and database management system to handle a large number of concurrent users and data queries.

Testing and Security: The current prototype has undergone basic testing, primarily for functionality. Comprehensive security measures, extensive testing for bugs,
and performance under different scenarios are areas that require further development.

These limitations highlight areas for future development and improvement. They also reflect the trade-offs made during the prototype phase to balance 
functionality with feasibility within the project's timeframe and resources.


Installation & Setup

Ensure Python is installed and up-to-date on your system [Python 3.9]
Install Flask and other required dependencies via pip.[pip3 install Flask]
Follow the provided setup instructions to get the application running locally for testing and demonstration purposes:

Open terminal > switch directory > python3 app.py
http://127.0.0.1:5000/ [port 5000]


Conclusion

We envision Lawrence as a platform that bridges the gap between legal professionals and those in need of legal services.
This project reflects our team's dedication, technical skills, and innovative approach to problem-solving.

