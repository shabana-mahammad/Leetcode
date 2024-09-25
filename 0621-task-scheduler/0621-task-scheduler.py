class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f=Counter(tasks)
        max_f=max(f.values())
        max_f_count=list(f.values()).count(max_f)
        cycles=max_f-1
        cycles_len=n-(max_f_count-1)
        empty_slots=cycles*cycles_len
        available_tasks=len(tasks)-(max_f*max_f_count)
        idele=max(0,empty_slots-available_tasks)
        return len(tasks)+idele
        