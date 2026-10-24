from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>web page</title>
    </head>
    <body>
        <h1 align=center>Tanishka-26018790</h1>
        <h2 align=center>My Laptop Configuration</h2>
        <table border="5" align=center cellpadding="10">
            <tr>
                <th>S.No</th>
                <th>Device Type</th>
                <th>Device Info</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>Device Name</td>
                <td>TL15-53M-G2</td>
            </tr>    
            <tr>
                <td>2.</td>
                <td>Processor</td>
                <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>Installed RAM</td>
                <td>16.0 GB (15.7 GB usable)</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>Graphics card</td>
                <td>Intel(R) Graphics (128 MB)</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>Storage</td>
                <td>128 GB of 477 GB used</td>
            </tr>
            <tr>
                <td>6.</td>
                <td>Device ID</td>
                <td>483E578A-CCB1-4B41-A766-9AAEE1654C33</td>
            </tr>
            <tr>
                <td>7.</td>
                <td>Product ID</td>
                <td>00342-42945-49126-AAOEM</td>
            </tr>
            <tr>
                <td>8.</td>
                <td>System type</td>
                <td>64-bit operating system, x64-based processor</td>
            </tr>
            <tr>
                <td>9.</td>
                <td>Pen and touch</td>
                <td>No pen or touch input is available for this display</td>
            </tr>
        </table>
    </body>
</html>  

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()