Handwritten Number Recognition
====================
Functionality:
    • Upload image
    • Give recognization feedback
    • Record current time, filename and result in a table


Frameworks used to implement this program include:
    • Tensorflow
    • Flask
    • Docker
    • Cassandra


Usage steps:
    1. Start a Cassandra container (docker run -p 9142:9042 --name fan-cassandra -d cassandra:latest)
    2. Set up a network (docker network create -d bridge --subnet 172.25.0.0/16 mynet)
    3. Connect the Cassandra container to the network (docker network connect mynet fan-cassandra)
    4. Build the image (docker build -t myimage .)
    5. Start the container and connect it to the network (docker run --name myapp --network mynet -p 4000:80 myimage:latest)
    6. Access the webpage through http://0.0.0.0:4000 and follow the instructions to upload images
    7. Use exec -it fan-cassandra cqlsh to access the cassandra countainer
    8. Enter:
            USE mnist;
            select*from picdatabase;
    9. You should see a table containing all the logs
    
    



