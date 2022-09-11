/*
Author:		Fredy Lopez
Created:	Spring Semester 2020
Class:		IoT
*/
//Title: Data Bucket (in Javascript)

var port = 81;
var server;
var count = 0;

function setup() {
	// create server
	server = new TCPServer();
	
	// when new client is connected
	server.onNewClient = function(client) {
	
		Serial.println("new client: " + client.remoteIP()
			+ ":" + client.remotePort());
			
		// when the client state changes
		client.onConnectionChange = function(type) {
			Serial.println("connection changed: " + type);
		};
		
		// when receiving data from client
		client.onReceive = function(data) {
			// print it and then disconnect
			Serial.println("received: " + client.remoteIP()
				+ ":" + client.remotePort() + ", " + data);
			//client.close();
			saveData(data);
		};
		
		// send a msg to client
		//client.send("hello " + (count++));
	};
	
	// start listening on port
	Serial.println(server.listen(port));
}

function saveData(d) {
	// write to disk
	console.log("Saving door status ",d," to disk...");
	//console.log(FileSystem.exists("/door_status.txt"));
	var file = FileSystem.open('/door_status.txt',
	File.WRITE | File.READ);
	file.println(d);
	file.close();
}


