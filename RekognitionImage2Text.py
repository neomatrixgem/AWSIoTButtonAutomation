import boto3
import json
if __name__ == "__main__":

    bucket='raspsensehat-staffuniv'
    photo='Car.png'

    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    title = response["TextDetections"][0]["DetectedText"]
    print(title) 
