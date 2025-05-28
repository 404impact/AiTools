from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from services import generate_summary, parse_url
from utils import load_env
from typing import Dict, Any

# Load environment variables
load_env()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Flask-RestX API with Swagger UI
api = Api(
    app,
    version='1.0',
    title='WebSummary API',
    description='API for summarizing web page content',
    doc='/api/docs',  # Swagger UI will be available at this endpoint
    prefix='/api'
)

# Create namespaces for organizing endpoints
main_ns = api.namespace('', description='Main operations')
summary_ns = api.namespace('summary', description='Web summarization operations')

# Define models for request/response documentation
url_model = summary_ns.model('UrlInput', {
    'url': fields.String(required=True, description='The URL to summarize', 
                         example='https://en.wikipedia.org/wiki/Artificial_intelligence')
})

summary_model = summary_ns.model('SummaryOutput', {
    'result': fields.String(description='Summarized content from the URL')
})

error_model = summary_ns.model('ErrorResponse', {
    'error': fields.String(description='Error message')
})

# API endpoints with Swagger documentation
@summary_ns.route('')
class WebSummary(Resource):
    @summary_ns.doc('get_summary_with_query_param')
    @summary_ns.param('url', 'The URL to summarize', _in='query')
    @summary_ns.response(200, 'Success', summary_model)
    @summary_ns.response(400, 'Invalid Input', error_model)
    def get(self) -> Dict[str, Any]:
        """Get a summary of a web page using query parameter."""
        url = request.args.get('url')
        
        if not url:
            return {"error": "No URL provided"}, 400
            
        print(f"Processing URL (GET): {url}")
        return generate_summary(url)
    
    @summary_ns.expect(url_model)
    @summary_ns.response(200, 'Success', summary_model)
    @summary_ns.response(400, 'Invalid Input', error_model)
    def post(self) -> Dict[str, Any]:
        """Get a summary of a web page using JSON body."""
        data = request.json
        url = data.get('url')
        
        if not url:
            return {"error": "No URL provided"}, 400
            
        print(f"Processing URL (POST): {url}")
        return generate_summary(url)

# Legacy route for backward compatibility
@app.route('/submit/', methods=['GET'])
def submit():
    """Legacy endpoint for backward compatibility."""
    url = request.args.get('query')
    print(f"Legacy endpoint called with URL: {url}")
    
    if not url:
        return {"result": "No URL provided"}
        
    summary = generate_summary(url)
    return summary

if __name__ == '__main__':
    # Enable debug mode to see detailed error messages
    app.run(debug=True, port=5001)