from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='chatgpt',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="sample of minimum package",  # 説明
    author='prgckwb',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT',  # ライセンス
    install_requires=[
        'openai',
        'tiktoken',
        'rich'
    ]
)