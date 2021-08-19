# smart_system_for_industries
Security is becoming necessary nowadays as the possibilities of intrusion are increasing day by day. So, to increase the security of industries. We have designed a system that will count the person in the room and store number of people in room on database when number changes. An area can be set to restricted and if any person enters that area and alert will be generated and data will be stored in database. It will also identify smoke, fire and hazardous gas.
We first developed a circuit and code for detecting person, smoke, fire and hazardous gas using NodeMCU (ESP8266). Then we created APIs to get data from NodeMCU and store it in MySQL database which was hosted on 000webhost. Then we used APIs to get data from server-side database and display on our web application. 
We used Python for back-end programing and Django framework to display live data on client side.
For front-end we used HTML, CSS and Bootstrap to design attractive UI.
