ome_validator = 'https://ome.github.io/ome-ngff-validator/'
sample_validator_url = f'{ome_validator}?source={s3_https_url}'

from IPython.display import display, Markdown
display(Markdown(f'[Visit {sample_validator_url}]({sample_validator_url})'))
