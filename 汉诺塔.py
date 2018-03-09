# 1.把 n-1 号盘子移动到缓冲区
# 2.把1号从起点移到终点
# 3.然后把缓冲区的n-1号盘子也移到终点

# 固定： 第一个开始，第二个缓冲区，第三个目的地
def move(n,start,buffer,to):
    if n==1:
        print('Move',start,'--->',to)
    else:
		# 把最上面的移到缓冲区
        move(n-1,start,to,buffer)
		# 然后把下面的一个送到终点
        move(1,start,buffer,to)
		# 最后把缓冲区的移到终点，这时候 start 是 0，可以当作缓冲区
        move(n-1,buffer,start,to)

move(3,'A','B','C')

# 要从a到b 那c就是缓冲 move(n-1,from,to,buffer) 
# 要从a到c 那b就是缓冲 move(1,from,buffer,to)     
# 要从b到c 那a就是缓冲 move(n-1,buffer,from,to) 