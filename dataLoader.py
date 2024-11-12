import os
from torch.utils.data import Dataset, DataLoader

REAL_NEWS_PATH = "./NeuralNews/dataset/real_arts"
FAKE_NEWS_PATH = "./NeuralNews/dataset/fake_arts"

class newsDataset(Dataset):

    def __init__(self, real_news_path, fake_news_path, caption_json):
        self.news_articles = self.load_articles(real_news_path) + self.load_articles(fake_news_path)
        self.labels = ['real' * len(self.load_articles(real_news_path)) + 'fake' * len(self.load_articles(real_news_path))]
        
    def load_articles(path):
            
        file_list = []
        
        for root, _, files in os.walk(path):
            for file in files:
                file_list.append(os.path.join(root, file))
        
        return file_list
    
    def __len__(self):
        return len(self.news_articles)
    
    def __getitem__(self, index):
        return self.news_articles[index], self.labels[index]
        
        
        
                
                
            
        
    