FROM minio/minio:latest

RUN apk update && apk add --no-cache bind-tools jq bash curl python

ADD minio-wrapper.sh /minio-wrapper.sh
ADD getdomainname.py /getdomainname.py

ENTRYPOINT ["/minio-wrapper.sh"]
