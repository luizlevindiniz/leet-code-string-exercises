from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "[]"
        encoded_str = "/@/".join(x for x in strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        if s == "":
            return [""]
        return s.split("/@/")
