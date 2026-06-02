import sys 

def existProduct(productList, target) :

    pl = 0 
    pr = len(productList) - 1

    # 피벗을 기준으로 교차하거나 동일한 경우에만 진행한다. 
    while pl <= pr :
        mid = (pl + pr) // 2

        if productList[mid] < target :
            pl = mid + 1

        elif productList[mid] > target :
            pr = mid - 1
        
        else :
            return True
    
    return False


def solution() :

    storeProductCount = int(sys.stdin.readline().rstrip())     
    storeProductList = list(map(int, sys.stdin.readline().split()))

    storeProductList.sort()

    customerProductOrderCount = int(sys.stdin.readline().rstrip())
    customerProductOrderList = list(map(int, sys.stdin.readline().split()))

    for currentProductNumber in customerProductOrderList :

        
        if existProduct(storeProductList, currentProductNumber) :
            print("yes", end = " ")
        else :
            print("no", end = " ")

solution()