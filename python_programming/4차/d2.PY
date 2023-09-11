def solution(papers, papers_len, k):
    sum=0
    for i in range(papers_len):
        k = k-papers[i]     #papers의 종이 수 만큼 k에서 뺌
        if k > 0:
            sum+=1
    print(sum)


papers = [2, 4, 3, 2, 1] 
papers_len = len(papers)
k = 14
solution(papers, papers_len, k)