import os
# 内存共享

# 同步是需要加锁

# 进程池
# 额外成本 创建进程 cpu核数限制导致切换时性能损耗
# 构建数据结构（进程池）与cpu的核数相同
# 进程池中的进程不断拿任务执行任务
# p.apply
# p.apply_async
# 异步结果，未来结果的引用

print(os.cpu_count())

