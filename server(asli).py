from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2
import json

# Database connection configuration
DB_NAME = 'contact_manager'
DB_USER = 'postgres'
DB_PASSWORD = 'na66248568'
DB_HOST = 'localhost'
DB_PORT = 5648

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Function to execute SQL queries
def execute_query(query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        # Example: Fetch data from the database
        query = "SELECT * FROM karbar"
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        self.wfile.write(json.dumps(rows).encode())
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        print(data)
        
        self._set_response()
        # Example: Insert data into the database
        # phone = data.get('phone')
        phone=data['phone']
        contact_id=data['contact_id']
        phone_id=data['phone_id']

        if phone and contact_id and phone_id:
            query = f"INSERT INTO phone(phone_id,contact_id,number) VALUES ({phone_id},{contact_id},'{phone}')"
            execute_query(query)
            print(phone)
            self.wfile.write("Data added successfully".encode())
        else:
            self.wfile.write("phone is required".encode())

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()