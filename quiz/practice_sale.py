# 최고·최저 매출 일자 파악하기
sales = [2000, 3000, 4000, 1000,
        1500, 3800, 200, 2900, 1300]

# 구조화 1 
# 변수 4개와 for 문 / if 문 사용
max_sales = -999
max_date = 0
min_sales = 9999999
min_date = 0

for idx in range(len(sales)):
    if sales[idx] > max_sales:
        max_sales = sales[idx]
        max_date = idx + 1
    
    if sales[idx] < min_sales:
        min_sales = sales[idx]
        min_date = idx + 1

print(f'최고 매출 : {max_date}일차, {max_sales}만원')
print(f'최저 매출 : {min_date}일차, {min_sales}만원')

# # 구조화 2
sales_summary = {'max_sales':sales[0],
                'max_date':1,
                'min_sales':sales[0],
                'min_date':1}
print(sales_summary)

for idx in range(1,len(sales)):
    if sales_summary['max_sales'] < sales[idx]:
        sales_summary['max_sales'] = sales[idx]
        sales_summary['max_date'] = idx + 1
    
    if sales_summary['min_sales'] > sales[idx]:
        sales_summary['min_sales'] = sales[idx]
        sales_summary['min_date'] = idx + 1

print(sales_summary)



# 구조화 3번째
sales_summary = {'max_sales':sales[0],
                'max_date':1,
                'min_sales':sales[0],
                'min_date':1}

for idx, sale in enumerate(sales):
    if sales_summary['max_sales'] < sale:
        sales_summary['max_sales'] = sale
        sales_summary['max_date'] = idx + 1
    if sales_summary['min_sales'] > sale:
        sales_summary['min_sales'] = sale
        sales_summary['min_date'] = idx + 1
    
print(sales_summary)