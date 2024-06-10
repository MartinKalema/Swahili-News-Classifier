### Swahili-News-Classifier

Swahili is spoken by 100-150 million people across East Africa. In Tanzania, it is one of two national languages (the other is English) and it is the official language of instruction in all schools. News in Swahili is an important part of the media sphere in Tanzania.

News contributes to education, technology, and the economic growth of a country, and news in local languages plays an important cultural role in many Africa countries. In the modern age, African languages in news and other spheres are at risk of being lost as English becomes the dominant language in online spaces.

The objective of this hackathon is to develop a multi-class classification model to classify news content according to their specific categories specified.The model can be used by Swahili online news platforms to automatically group news according to their categories and help readers find the specific news they want to read. In addition, the model will contribute to a body of work ensuring that Swahili is represented in apps and other online products in the future.

### System Architecture

<img src="static/architecture.png" />

### ULMFiT Model Training Pipeline

<img src="static/model_training_pipeline_large.png" />

### How to install

Clone the repository

```bash
git clone https://github.com/MartinKalema/Swahili-News-Classifier
```

Create a conda environment after opening the repository and activate it

```bash
conda create -n classifier python=3.8 -y
conda activate classifier
```

Install the requirements

```python
pip install -r requirements.txt
```

Create an AWS S3 Bucket and finally an environment file with the configurations below

```
AWS_ACCESS_KEY_ID='...'
AWS_SECRET_ACCESS_KEY='...'
REGION_NAME='...eg us-east-1"

```

Initiate the pipeline

```python
python main.py
```

### Unit Tests

To run the unit tests, run the command below.

```bash
pytest tests/test_file_name.py
```
