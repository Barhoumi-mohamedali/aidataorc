from pyspark.ml import PipelineModel

from sparkocr.transformers import *

imagePath = "path to image files"

# Read image files as binary file
df = spark.read \
  .format("binaryFile") \
  .load(imagePath)

# Transform binary content to image
binaryToImage = BinaryToImage() \
  .setInputCol("content") \
  .setOutputCol("image")

# OCR
ocr = ImageToText() \
  .setInputCol("image") \
  .setOutputCol("text")

# Define Pipeline
pipeline = PipelineModel(stages=[
  binaryToImage,
  ocr
])

data = pipeline.transform(df)

data.show(
