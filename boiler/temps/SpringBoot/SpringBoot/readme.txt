Local installation

make sure you have installed:
 java 11
 maven : https://maven.apache.org/install.html


using command line, navigate to project folder.
and use foollwoing commands:

-------------------
mvn clean install spring-boot:run

------------------------
your application wil be running on http://localhost:5000/


Using with Frontend:
you can secure the by allowing cross origin requests to specific routes 
and specific origins in controller

@CrossOrigin("http://example.com")