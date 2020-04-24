FROM python:3.6
WORKDIR /app
COPY xor_contiguous_subset.py .

ENTRYPOINT ["python", "xor_contiguous_subset.py"]