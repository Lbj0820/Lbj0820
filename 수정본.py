def distribute_papers(papers, papers_len, K):
    # 초기화
    recipients = 0

    # 각 사람에게 종이를 나눠주면서 확인
    for i in range(papers_len):
        # 남은 종이 수와 현재 사람이 필요한 종이 수를 합산      #이걸 왜 더함?  남은 종이수에서 필요한 사람의 종이수 만큼 빼야지
        K = K - papers[i]

        # 현재 사람에게 줄 수 있는 종이 수 계산 (할 필요 없음)    
        #distributed_papers = min(total_papers, K)

        # 남은 종이 수 업데이트   -> 이건 위에서 했고  
        #remaining_papers = total_papers - distributed_papers

        # 종이를 받은 사람 수 증가  
        if K > 0:
            recipients += 1

    # 마지막 사람까지 확인 후 남은 종이를 받을 수 있다면 마지막 사람에게 주기 -> 위의 과정에서 이미 마지막 사람이 되는지 걸러냄
    # while remaining_papers > 0:
        # distributed_papers = min(remaining_papers, K)
        # remaining_papers -= distributed_papers
        # recipients += 1

    return recipients

# 예제 사용
papers = [2, 4, 3, 2, 1,2,5,3,5,3] #[2, 3, 1, 1, 4, 2]  # 각 사람이 필요로 하는 종이 수 예시
papers_len = len(papers)  # 리스트의 길이
K = 10  # 처음 앞사람에게 전달한 종이 수
result = distribute_papers(papers, papers_len, K)
print(f"{result} 명이 종이를 필요한 만큼 받았습니다.")

