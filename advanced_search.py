import sys


if __name__ == "__main__":
    args = sys.argv[1:]
    print(args)


#def main(args):
import pandas as pd
import os
import re

import torch
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import xlsxwriter

# 코드별 질문 리스트 불러오기

question_list = {"해시태그": args}
print(question_list)
print("test")
# 환자별 행동 특성 데이터 불러오기

# Check if CUDA is available and set the device accordingly
device = 'cuda' if torch.cuda.is_available() else 'cpu'

trait_data = pd.read_csv(r"advanced_search_test_file.csv")
trait_data.head()

# 모든 텍스트 소문자로 전환하기

def preprocess_text(text):
    return " ".join([word.lower() for word in text.split()]) # 입력받은 텍스트를 소문자화합니다

# 행동 특성의 이름과 질문 텍스트 소문자화
trait_data['Processed_Hashtag'] = trait_data['해시태그'].apply(preprocess_text)

# 질문 텍스트 vectorization

# sentence transformer 모델 불러오기
model = SentenceTransformer('all-MiniLM-L6-v2') # sentence transfomers 모델 불러오기
model = model.to(device)  

# 행동 특성 텍스트 데이터 vectorization
X_full = model.encode(trait_data['Processed_Hashtag'].tolist(), convert_to_tensor=True) 
X_full = X_full.to(device)

# 질문 텍스트 vectorization 적용한 후 

# Function to find best matches in dataset based on the processed text and include rank
def match_question_to_data_detailed(question, trait_data, top_n=None):
    
    # 질문 텍스트 vectorization 
    question_vec = model.encode([question], convert_to_tensor=True)
    question_vec = question_vec.to(device)
    
    # 각가의 질문과 행동 특성 사이의 유사도(similarity) 계산
    cosine_similarities = cosine_similarity(question_vec, X_full).flatten()  # Compute cosine similarity on CPU
    
    # 유사도(similarity)가 높은 순서대로 결과 정렬
    if top_n:
        related_docs_indices = cosine_similarities.argsort()[-top_n:][::-1]
    else:
        related_docs_indices = cosine_similarities.argsort()[::-1]
    matched_data = trait_data.iloc[related_docs_indices]
    matched_data['Question']= question
    matched_data['Matching Rank/Probability'] = cosine_similarities[related_docs_indices]
    return matched_data

# Find the best matches for each question with detailed information
question_matches_detailed_ranked = {}
for idx, question in enumerate(question_list['해시태그']):
    matched_data = match_question_to_data_detailed(question, trait_data) # 각각의 질문 내용과 행동 특성들을 비교
    question_matches_detailed_ranked[f"advanced_search_result {idx}"] = matched_data

output_filepath_questions_detailed_ranked = r"advanced_search_result.xlsx"
writer = pd.ExcelWriter(output_filepath_questions_detailed_ranked, engine='xlsxwriter')
for q_key, matched_data in question_matches_detailed_ranked.items():
    # Add the question as a separate row before the matches
    dataframe = pd.DataFrame([[None, None, None, None, None]], columns=['이름', '해시태그', 'Processed_Hashtag', 'Question',
    'Matching Rank/Probability'])
    dataframe = pd.concat([dataframe, matched_data], ignore_index=True)
    dataframe.to_excel(writer, sheet_name=q_key, index=False)

# Use close() instead of save()
writer.close()
