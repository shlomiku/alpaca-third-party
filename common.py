import os


def get_alpha_vantage_credentials(alpha_vantage_key: str = None) -> str:
    key_id = alpha_vantage_key or os.environ.get('ALPHAVANTAGE_API_KEY')
    if key_id is None:
        raise ValueError('Key ID must be given to access Alpha Vantage API'
                         ' (env: ALPHAVANTAGE_API_KEY)')
    return key_id
