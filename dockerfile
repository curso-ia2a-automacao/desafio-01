
FROM python:3.10-slim

WORKDIR /app
COPY ./app /app
RUN pip install streamlit

EXPOSE 8501
CMD ["streamlit", "run", "streamlit_comparador.py", "--server.enableCORS=false"]
