from app import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

app = ProxyFix(create_app(), x_for=1, x_host=1, x_proto=1)


# /etc/nginx/nginx.conf

# events {
#     worker_connections 1024;
# }

# http {
    
#     server{

#         listen      80;
#         server_name localhost;

#         access_log /var/log/nginx/access.log;
#         error_log  /var/log/nginx/error.log;

#         location / {
#             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#             proxy_set_header X-Forwarded-Host $http_host;
#             proxy_set_header X-Forwarded-Proto $scheme;

#             proxy_pass http://127.0.0.1:8000;
#         }
#     }
# }