def app(event, context):
    print("Se subió un archivo a S3")
    print(event)
    return {}