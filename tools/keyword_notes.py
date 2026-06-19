from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SITE_URL = "https://mainaiyouxi.com.cn"
CORE_TAG = "爱游戏"
SAMPLE_NOTES = [
    "《爱游戏》是玩家心中的经典，记录了许多美好回忆。",
    "在 mainaiyouxi.com.cn 上，用户可以分享游戏攻略与心得。",
    "爱游戏社区鼓励玩家交流技巧、发布原创内容。",
    "2024年，爱游戏推出了多款跨平台联机作品。",
    "通过关键词“爱游戏”，可以找到大量游戏评测和推荐。",
]

@dataclass
class KeywordNote:
    """单个关键词笔记的数据结构"""
    title: str
    content: str
    keyword: str
    source_url: str
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    tags: List[str] = field(default_factory=list)

    def formatted_output(self) -> str:
        """返回格式化的笔记文本"""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"标题：{self.title}\n"
            f"关键词：{self.keyword}\n"
            f"来源：{self.source_url}\n"
            f"创建时间：{self.created_at}\n"
            f"标签：{tag_str}\n"
            f"内容：{self.content}\n"
        )

@dataclass
class NoteCollection:
    """管理一组关键词笔记的集合"""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        """添加一条笔记"""
        self.notes.append(note)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        """根据关键词筛选笔记"""
        return [n for n in self.notes if keyword.lower() in n.keyword.lower()]

    def export_formatted(self, keyword_filter: Optional[str] = None) -> str:
        """将所有笔记格式化为完整文本，可选按关键词筛选"""
        target_notes = self.filter_by_keyword(keyword_filter) if keyword_filter else self.notes
        if not target_notes:
            return "暂未找到匹配的笔记。"
        segments = []
        for i, note in enumerate(target_notes, 1):
            segments.append(f"--- 笔记 {i} ---")
            segments.append(note.formatted_output())
        return "\n".join(segments)

    def summary(self) -> str:
        """返回笔记集合的概览信息"""
        return f"笔记总数：{len(self.notes)}，关键词覆盖：{len(set(n.keyword for n in self.notes))} 个"

def build_sample_collection() -> NoteCollection:
    """使用示例数据构建一个笔记集合"""
    collection = NoteCollection()
    for idx, sample in enumerate(SAMPLE_NOTES, 1):
        note = KeywordNote(
            title=f"爱游戏笔记 #{idx}",
            content=sample,
            keyword=CORE_TAG,
            source_url=SITE_URL,
            tags=["游戏", "社区", "攻略"] if idx % 2 == 0 else ["评测", "推荐"]
        )
        collection.add_note(note)
    return collection

def display_all_notes(collection: NoteCollection) -> None:
    """打印所有笔记并显示摘要"""
    print(collection.export_formatted())
    print("=" * 40)
    print(collection.summary())

if __name__ == "__main__":
    notes_collection = build_sample_collection()
    display_all_notes(notes_collection)