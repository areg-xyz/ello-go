import azure.functions as func
import json
import logging

app = func.FunctionApp()

# Simple in-memory storage for demonstration purposes
# In a real production scenario, use Redis, CosmosDB, or Table Storage
_VISITOR_COUNT = 0
_UNIQUE_VISITORS = set()

@app.route(route="visitors", auth_level=func.AuthLevel.ANONYMOUS)
def visitors(req: func.HttpRequest) -> func.HttpResponse:
    global _VISITOR_COUNT
    
    logging.info('Visitor function processed a request.')

    method = req.method

    if method == "POST":
        # Increment unique visitor count
        # For simplicity, we'll just increment a counter. 
        # In a real app, we'd track IP hashes or session IDs.
        try:
            req_body = req.get_json()
            visitor_id = req_body.get('visitor_id')
            if visitor_id and visitor_id not in _UNIQUE_VISITORS:
                _UNIQUE_VISITORS.add(visitor_id)
                _VISITOR_COUNT += 1
        except ValueError:
            # If no JSON body, just increment for demo
            _VISITOR_COUNT += 1
            
        return func.HttpResponse(
            json.dumps({"count": _VISITOR_COUNT}),
            mimetype="application/json",
            status_code=200
        )

    elif method == "GET":
        return func.HttpResponse(
            f"{_VISITOR_COUNT}",
            status_code=200
        )

    else:
        return func.HttpResponse(
            "Method not allowed",
            status_code=405
        )

# Local development stub
if __name__ == "__main__":
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import sys

    class LocalHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.handle_request("GET")
        
        def do_POST(self):
            self.handle_request("POST")

        def do_OPTIONS(self):
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()

        def handle_request(self, method):
            if self.path == '/api/visitors':
                # Read body for POST
                body = None
                if method == "POST":
                    content_length = int(self.headers.get('Content-Length', 0))
                    body = self.rfile.read(content_length)

                # Construct Azure Request
                req = func.HttpRequest(
                    method=method,
                    body=body,
                    url=self.path,
                    params={}
                )

                # Call the function
                resp = visitors(req)

                # Send Response
                self.send_response(resp.status_code)
                self.send_header('Content-type', resp.mimetype or 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(resp.get_body())
            else:
                self.send_response(404)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

    port = 7071
    print(f"Starting local server on http://localhost:{port}")
    server = HTTPServer(('localhost', port), LocalHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
        server.socket.close()
