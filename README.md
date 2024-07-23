# wired-brain
Developing an eCommerce app using Flask Python framework and Docker to containerize (Dockerize) the app.

Default http method for Flask's routes is GET.

An empty string is evaluated to false.

request.json retrieves the request body data sent to the API endpoint.

curl is a command client to make http requests.

To pass an argument with a space in it to a route, you need to URL-encode the space as %20

Flask automatically ports to 5000

curl commands are not interpreted exactly in a Powershell environment. When working in PowerShell is better to use the Invoke-WebRequest cmdlet. I found it impossible to execute a POST request using curl client in a PowerShell env, it worked only when I used Invoke-WebRequest command. However, if you want to user curl as a client, you should use the Windows command prompt terminal.

Every time the server is restarted due to a change and save in the source code, data is started, How should it behaves when working with a database?

Docker images are composed of layers, each representing a Docker file instruction.

When docker builds an image from a Docker file, it reconstructs the layers that it
needs to, but it the layer already exists, it doesn't have to reconstruct it. As a 
result, we placed the instructions that don't change frequently at the begining of
the file so Docker doesn't have to reconstruct it again.