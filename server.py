from http.server import BaseHTTPRequestHandler,HTTPServer
import psycopg2
import cgitb
cgitb.enable()

hostname='localhost'
database='contact_manager'
username='postgres'
pwd='na66248568'
port_id=5648



conn=psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

cur=conn.cursor()


class WebRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        # self.wfile.write(self.get_response().encode("utf-8"))
        cur.execute("select * from karbar")
        result=cur.fetchmany()

        print(result)
        list1=[str(item) for item in result]
        str1='-'.join(list1)
        self.wfile.write(bytes(f"{str1}", "utf-8"))
        

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "db")
        self.end_headers()

        cur.execute("insert into phone (,phone_id,contact_id,number) values (1,1,'09125555555')")
        conn.commit()
    


if __name__ == "__main__":
	webserver = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
	print("Server started")  #Server starts

	try:
		webserver.serve_forever()
	except KeyboardInterrupt:
		pass

	webserver.server_close()  #Executes when you hit a keyboard interrupt, closing the server
	print("Server stopped.")
