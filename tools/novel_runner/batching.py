"""故事单元章节范围的确定性 3～5 章分批。"""

from __future__ import annotations

from dataclasses import dataclass


class BatchingError(RuntimeError):
    """章节范围不能按策略分批。"""


@dataclass(frozen=True, slots=True)
class ChapterBatch:
    start: int
    end: int

    @property
    def size(self) -> int:
        return self.end - self.start + 1


def partition_chapters(
    start: int,
    end: int,
    *,
    minimum: int = 3,
    maximum: int = 5,
    preferred: int = 4,
) -> tuple[ChapterBatch, ...]:
    if start <= 0 or end < start:
        raise BatchingError("故事单元章节范围无效")
    total = end - start + 1
    best: list[int] | None = None
    best_score: tuple[int, int] | None = None

    def search(remaining: int, sizes: list[int]) -> None:
        nonlocal best, best_score
        if remaining == 0:
            score = (sum(abs(size - preferred) for size in sizes), len(sizes))
            if best_score is None or score < best_score:
                best = list(sizes)
                best_score = score
            return
        for size in range(maximum, minimum - 1, -1):
            if size > remaining:
                continue
            sizes.append(size)
            search(remaining - size, sizes)
            sizes.pop()

    search(total, [])
    if best is None:
        raise BatchingError(f"无法把 {total} 章拆成每批 {minimum}～{maximum} 章")
    batches: list[ChapterBatch] = []
    cursor = start
    for size in best:
        batches.append(ChapterBatch(cursor, cursor + size - 1))
        cursor += size
    return tuple(batches)
