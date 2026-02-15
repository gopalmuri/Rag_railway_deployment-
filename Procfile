web: cd mainfolder/backend && python manage.py migrate && gunicorn rag_project.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
