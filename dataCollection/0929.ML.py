from bing_image_downloader import downloader

downloader.download("pomeranian", limit=20,  output_dir="dataset")
downloader.download("poodle", limit=20,  output_dir="dataset")
downloader.download("shih tzu", limit=20,  output_dir="dataset")
downloader.download("Yorkshire Terrier", limit=20,  output_dir="dataset")
downloader.download("Dachshund", limit=20,  output_dir="dataset")